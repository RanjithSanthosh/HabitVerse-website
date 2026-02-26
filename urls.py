
from django.urls import path
import views

urlpatterns = [
    path('webhook/', views.receive_message),
    path('verify/', views.verify_webhook),
    path('messages/', views.message_list),
    path('privacy-policy/', views.privacy_policy),
    path('terms/', views.terms),
    path('', views.index),
]
