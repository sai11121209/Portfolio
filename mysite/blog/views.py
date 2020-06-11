from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html')


def register(request):
    return render(request, 'blog/register.html')


def login(request):
    return render(request, 'blog/login.html')


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print('a')
        if form.is_valid():
            form.save()
            print('a')
            return redirect('post')
        return redirect('post')
    else:
        form = PostForm()
    return render(request, 'blog/post.html', {'form': form})
