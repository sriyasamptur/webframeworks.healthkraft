from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def atkins(request):
    return render(request, 'atkins.html', {})

def ketogenic(request):
    return render(request, 'ketogenic.html', {})

def vegan(request):
    return render(request, 'vegan.html', {})

def vegetarian(request):
    return render(request, 'vegetarian.html', {})

def raw(request):
    return render(request, 'raw.html', {})

def zone(request):
    return render(request, 'zone.html', {})

def salads(request):
    return render(request, 'salads.html', {})

def soups(request):
    return render(request, 'soups.html', {})

def smoothies(request):
    return render(request, 'smoothies.html', {})

def food(request):
    return render(request, 'image.html', {})

def proteins1(request):
    return render(request, 'proteins1.html', {})

def carb(request):
    return render(request, 'carb.html', {})

def fats(request):
    return render(request, 'fats.html', {})

def micronutrients(request):
    return render(request, 'micronutrients.html', {})

def energy(request):
    return render(request, 'energy.html', {})

def aboutus(request):
    return render(request, 'aboutus.html', {})

def fitness(request):
    return render(request, 'fitness.html', {})