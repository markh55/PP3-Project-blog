from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import Post


# Create your views here.
@login_required
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

@login_required
def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post,
            'comments': comments,
            'comment_count': comment_count,
        }
    )

def home_view(request):
    return render(request, 'blog/home.html')

