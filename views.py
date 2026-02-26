from django.shortcuts import render
from django.http import HttpResponse

def receive_message(request):
    return HttpResponse("Webhook received")

def verify_webhook(request):
    return HttpResponse("Webhook verified")

def message_list(request):
    return render(request, "messages.html")

def privacy_policy(request):
    return render(request, "privacy_policy.html")

def terms(request):
    return render(request, "terms.html")

def index(request):
    context = {
        'phone_number': '919790563993',
        'display_phone': '+91 9790563993'
    }
    return render(request, "home.html", context)
