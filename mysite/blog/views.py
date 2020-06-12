from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required


# Create your views here.
def blog(request):
    if request.user.id == None:
        return render(request, 'blog/blog.html')
    else:
        return render(request, 'blog/blogLogin.html', {'username': request.user})

@login_required
def post(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        Post.objects.create(
            author_id=request.user.id,
            title=form.cleaned_data['title'],
            tag=form.cleaned_data['tag'],
            text=form.cleaned_data['text'],
        )
        print('a')
        return redirect('../blogLogin')
    return render(request, 'blog/post.html', {'form': form,'username': request.user})

#@login_required
def User(request):
    print(request.user.id)
    return redirect('login')