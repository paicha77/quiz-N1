from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def products(request):
    product = [
        {'name': 'Laptop', 'price': 2500},
        {'name': 'Gaming Laptop', 'price': 4200},
        {'name': 'Desktop PC', 'price': 3500},
        {'name': 'MacBook Air', 'price': 5000},
        {'name': 'Mouse', 'price': 80},
        {'name': 'Wireless Mouse', 'price': 120},
        {'name': 'Keyboard', 'price': 150},
        {'name': 'Mechanical Keyboard', 'price': 300},
        {'name': 'Mouse Pad', 'price': 40},
        {'name': 'Webcam', 'price': 220},
        {'name': 'Monitor', 'price': 700},
        {'name': 'Gaming Monitor', 'price': 1200},
        {'name': 'Projector', 'price': 1800},
        {'name': 'Headphones', 'price': 180},
        {'name': 'Gaming Headset', 'price': 350},
        {'name': 'Bluetooth Speaker', 'price': 250},
        {'name': 'Microphone', 'price': 400},
        {'name': 'Game Controller', 'price': 200},
        {'name': 'Gaming Chair', 'price': 900},
        {'name': 'Gaming Console', 'price': 2200},
    ]

    return render(request, 'products.html', {'products': product})