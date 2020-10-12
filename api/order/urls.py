## 7.5
## urls for order and auth token in django

from django.urls import path,include
from rest_framework import routers

from . import views
router = routers.DefaultRouter()
router.register(r'', views.OrderViewSet)

urlpatterns=[
    path('add/<str:id>/<str:token>/', views.add, name='order.add'),
    path('',include(router.urls))
]
