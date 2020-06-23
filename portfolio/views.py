from django import forms
from django.shortcuts import render, redirect
from .forms import ContactForm, ContactLoginForm
from .models import Contact
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
# Create your views here.

def Portfolio(request):
    if request.user.id == None:
        form = ContactForm(request.POST or None)
    else:
        form = ContactLoginForm(request.POST or None)
    with open('requirements.txt', encoding='utf-16') as f:
        url = ['https://img.shields.io/pypi/v/', '?label=']
        requirements = [url[0]+requirement[0:requirement.find('==')]+url[1]+requirement[0:requirement.find('==')] for requirement in f.readlines()]
    para = {'form': form, 'requirements': requirements}
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
        return redirect('portfolio:home')
    return render(request, 'portfolio/portfolio.html', para)

@login_required
def ContactDetail(request, pk, username):
    if get_object_or_404(Contact, pk=pk).name == str(request.user):
        contact = get_object_or_404(Contact, pk=pk)
        if request.method == 'POST':
            if 'edit' in request.POST:
                print('a')
                return redirect('portfolio:edit', pk=pk, username=username)
            if 'del' in request.POST:
                Contact.objects.filter(pk=pk).delete()
                return redirect('mypage')
            return redirect('mypage')
        return render(request, 'portfolio/contactdetail.html', {'username': request.user, 'contact': contact})
    return redirect('portfolio:home')

@login_required
def ContactEdit(request, pk, username):
    if get_object_or_404(Contact, pk=pk).name == str(request.user):
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactLoginForm(request.POST or None, instance=contact)
        if request.method == 'POST' and form.is_valid():
            contact.update()
            return redirect('mypage')
        return render(request, 'portfolio/contactedit.html', {'username': request.user, 'contact': contact, 'form': form})
    return redirect('portfolio:home')
