import os.path

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from customers.forms import CustomerForm
from customers.models import Customer


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    data = Customer.objects.all()
    context = {'data': data}
    return render(request, 'about.html',context)

def contact(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')

    else:
        form = CustomerForm()
    return render(request, 'contact.html', {'form':form})

def update(request,id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

            if 'image' in request.FILES:
                file_name = os.path.basename(request.FILES['image'].name)
                messages.success(request, message=f'Customer updated successfully! {file_name} uploaded')
            else:
                messages.error(request, message='Customer details updated successfully')
            return redirect('about')
        else:
            messages.error(request, message='Please confirm your changes')
    else:
        form = CustomerForm(instance=customer)
    return render(request, template_name='update.html', context={'form': form, 'customer': customer})
