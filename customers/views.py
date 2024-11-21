from django.shortcuts import render, redirect

from customers.forms import CustomerForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')

    else:
        form = CustomerForm()
    return render(request, 'contact.html', {'form':form})
