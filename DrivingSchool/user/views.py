from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('user-register') #this is temparary redirect change it later
    else:
        form = UserCreationForm()
    context ={
        'form': form
    }
    return render(request,'user/register.html',context)

@login_required
def dashboard(request):
    if request.user.is_authenticated and Profile.objects.get(user=request.user).is_customer:
        return redirect('customer-index')
    elif request.user.is_authenticated and Profile.objects.get(user=request.user).is_staff:
        return redirect('staff-index')
    elif request.user.is_authenticated and Profile.objects.get(user=request.user).is_owner:
        return redirect('owner-index')