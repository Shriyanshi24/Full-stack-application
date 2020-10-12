## 8.2 
## generate braintree token for user

from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

import braintree

# Create your views here.
gateway = braintree.BraintreeGateway
(
    braintree.Configuration
    (
        braintree.Environment.Sandbox,
        merchant_id="3338fchtxbb3ncq6",
        public_key="3n86cypxfz886gkj",
        private_key="ebadfbe8ec8532632c4c06321d1491a1"
    )
)
## to check user is signed up or not
def validated_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        else:
            return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
## generating token
def generate_token(request,id,token):
    if not validated_user_session(id,token):
        return JsonResponse({'error': 'invalid session, please login again!'})

    return JsonResponse({'clientToken': gateway.client_token.generate(), 'success': True})

@csrf_exempt
## 8.3 process payment from backend
def process_payment(request,id,token):
    if not validated_user_session(id,token):
        return JsonResponse({'error': 'invalid session, please login again!'})
    
    nonce_from_the_client = request.POST['paymentMethodNonce']
    amount_from_the_client = request.POST['amount']

    result = gateway.transaction.sale({
        "amount": amount_from_the_client,
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement":True
        }
    })

    if result.is_success:
        return JsonResponse
        (
            {
            'success': result.is_success,
            'transaction': {'id': result.transaction.id, 'amount': result.transaction.amount}
            }
        )
    else:
        return JsonResponse({"error": True, 'success':False})

