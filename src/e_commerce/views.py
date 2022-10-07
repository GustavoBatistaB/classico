from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from products.models import Product


def index(request):
    context = {
        "title": "Inicio",
        "object": Product.objects.featured()
    }
    if request.user.is_authenticated:
        context["premium_content"] = f"Seja Bem Vindo (a) {request.user}"
    return render(request, 'index.html', context)


def about_page(request):
    context = {
        "title": "Página Sobre",
        "content": "Bem vindo a pagina sobre",
    }
    return render(request, "about/view.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contatos",
        "content": "Entre em contato conosco",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)
