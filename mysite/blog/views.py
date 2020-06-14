from django.shortcuts import render, redirect
from django import forms
from .forms import PostForm
from .models import Posts
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


# Create your views here.
def Blog(request):
    postlists = Posts.objects.order_by('create_date').reverse()[:10]
    return render(request, 'blog/blog.html', {'username': request.user, 'postlists': postlists, 'time': timezone.now()})

@login_required
def Post(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        Posts.objects.create(
            author_id=request.user.id,
            title=form.cleaned_data['title'],
            tag=form.cleaned_data['tag'],
            text=form.cleaned_data['text'],
        )
        return redirect('blog:home')
    return render(request, 'blog/post.html', {'form': form,'username': request.user})

def PostList(request):
    postlists = Posts.objects.all()
    return render(request, 'blog/postlist.html', {'postlists': postlists, 'username': request.user})


def PostDetail(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if post.author == request.user:
        if request.method == 'POST':
            return redirect('blog:edit', pk=pk)
    return render(request, 'blog/postdetail.html', {'post': post, 'username': request.user})

@login_required
def PostEdit(request, pk):
    if get_object_or_404(Posts, pk=pk).author == request.user:
        form = PostForm(request.POST or None)
        post = get_object_or_404(Posts, pk=pk)
        form.fields['title'].widget = forms.TextInput(attrs={'value':post.title})
        form.fields['tag'].widget = forms.TextInput(attrs={'value':post.tag})
        form.fields['text'].widget = forms.TextInput(attrs={'value':post.text})
        if request.method == 'POST' and form.is_valid():
            if 'edit' in request.POST:
                post.title = form.cleaned_data['title']
                post.tag = form.cleaned_data['tag']
                post.text = form.cleaned_data['text']
                post.update()
                return redirect('blog:detail', pk=pk)
            if 'del' in request.POST:
                post.delete()
                return redirect('blog:list')
        return render(request, 'blog/postedit.html', {'form': form, 'username': request.user})
    return redirect('blog:detail',pk=pk)

#@login_required
def User(request):
    print(request.user.id)
    return redirect('login')