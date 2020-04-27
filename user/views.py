from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account Created Successfully")
            return redirect('home')

    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required(login_url='login')
def profile(request):
    context = {
    'title': 'Profile',
    }
    return render(request, 'user/profile.html', context)

@login_required(login_url='login')
def update_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST)
        p_form = ProfileUpdateForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile updated Successfully')
            return redirect('profile')

    else:
        u_form = UserUpdateForm()
        p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user/profile_update.html', context)
