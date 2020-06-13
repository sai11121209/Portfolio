from django.shortcuts import render, redirect
from .forms import ContactForm, ContactLoginForm
from .models import Contact
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
# Create your views here.

def Portfolio(request):
    if request.user.id == None:
        template = 'portfolio'
        form = ContactForm(request.POST or None)
    else:
        template = 'portfolioLogin'
        form = ContactLoginForm(request.POST or None)
    para = {'form': form}
    para['username'] = request.user
    if request.method == 'POST' and form.is_valid():
        if request.user.id == None:
            form.save()
        else:
            Contact.objects.create(
                name=request.user,
                email=request.user.email,
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
            )
        return redirect('portfolio')
    return render(request, f'portfolio/{template}.html', para)

@login_required
def ContactDetail(request, pk):
    if get_object_or_404(Contact, pk=pk).name == str(request.user):
        contact = get_object_or_404(Contact, pk=pk)
        print(request.method)
        if request.method == 'POST':
            print('b')
            Contact.objects.filter(pk=pk).delete()
            return redirect('accounts:mypage')
        return render(request, 'portfolio/contactdetail.html', {'username': request.user, 'contact': contact})
    return redirect('portfolio:portfolio')