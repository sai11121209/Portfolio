from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import Contact
# Create your views here.

def portfolio(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
        return redirect('portfolio')
    else:
        form = ContactForm()
        return render(request, 'portfolio/portfolio.html', {'form': form})