
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserData


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user_data = UserData.objects.get(username=username)
            if user_data.password == password:
                messages.success(request, 'Login successful.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid password.')
        except UserData.DoesNotExist:
            messages.error(request, 'User does not exist.')
    
    return render(request, 'giftlogin.html')


def registration_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        date_of_birth = request.POST['date_of_birth']
        country = request.POST['country']

        UserData.objects.create(
            username=username,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            country=country
        )

        messages.success(request, 'Registration successful.')
        return redirect('login')

    return render(request, 'giftregister.html')