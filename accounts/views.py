from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register_user(request):
    if request.method == 'POST'
       form = UserCreationForm(request.POST)
        # Create user
        if form.is_valid():
            # save user to database
            user = form.save()
            # Log in the user
            login(request, user)
            return redirect('home')

    else:
        # Render an empty form
    form = UserCreationForm()
    return render(request,
        'accounts/register.html',{'userfreationform': form})
