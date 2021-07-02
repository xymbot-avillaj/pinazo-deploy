from django.shortcuts import render, redirect
import logging
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

@login_required(login_url='login')
def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        logger.error(form)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Usuario ' + user+ ' creado')
        else:
            messages.success(request, 'El usuario no se ha podido crear correctamente, verifica que las contraseñas coinciden y su longitud es mayor de 8.')
    context = {'form': form}
    return render(request, ["register.html"], context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'login.html', context)    

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def production_view(request):
    form = ProductionForm(request.POST or None)
    show_table = ProductionTable.objects.raw("SELECT * FROM public.production_production WHERE date_from > now() AT TIME ZONE 'Europe/Madrid' AT TIME ZONE 'UTC' ORDER BY date_to desc")
    
    if form.is_valid():        
        form.save()
        form = ProductionForm()
        return redirect('.')
    else:
        print(form.errors)
    
    context = {
        'form': form,
        'show_table': show_table 
    }
    return render(request, "index.html", context)

@login_required(login_url='login')
def updateOrder(request, pk):
    order = Production.objects.get(id=pk)
    form = ProductionForm(instance=order)
    if request.method == 'POST':
        form = ProductionForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'update.html', context)

