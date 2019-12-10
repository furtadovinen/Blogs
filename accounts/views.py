from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        i_form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid() and i_form.is_valid():
            form.save()
            i_form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}. You can now Login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
        i_form = ProfileUpdateForm()

    context = {
        'form': form,
        'i_form': i_form
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updates.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)
