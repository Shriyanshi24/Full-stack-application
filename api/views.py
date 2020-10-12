from django.http import JsonResponse


def home(request):
    return JsonResponse({'info': 'Django react course','name': 'shriyanshi'})
# Create your views here.
