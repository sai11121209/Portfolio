from django.shortcuts import render, redirect
from .forms import ContactForm
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