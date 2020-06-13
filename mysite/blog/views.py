from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Posts
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


# Create your views here.
def Blog(request):
    if request.user.id == None:
        return render(request, 'blog/blog.html')
    else:
        return render(request, 'blog/blogLogin.html', {'username': request.user})

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
    return render(request, 'blog/postdetail.html', {'post': post, 'username': request.user})

#@login_required
def User(request):
    print(request.user.id)
    return redirect('login')