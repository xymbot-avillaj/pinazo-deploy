from django.shortcuts import render, redirect
from .models import ProductionTable
from .forms import ProductionForm


def user_view(request):
    return render(request, ["user.html"], {})

def login_view(request):
    return render(request, ["login.html"], {})

def production_view(request):    

    form = ProductionForm(request.POST or None)
    show_table = ProductionTable.objects.raw('select * from public.production_production order by date_to desc')
    
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

