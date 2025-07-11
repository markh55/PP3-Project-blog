from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .models import Post, Comment
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import CommentForm


# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

# CreateView - User to be able to post own blog
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/post/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = 'PB'
        return super().form_valid(form)

# user to update their blog post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/post/post_form.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = 'PB'
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# DeleteView - user to be able to delete their blog
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, status=Post.Status.PUBLISHED)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    else:
        comment_form = CommentForm()

    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post,
            'comments': comments,
            'comment_count': comment_count,
            "comment_form": comment_form,
        }
    )

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully.")
            return HttpResponseRedirect(reverse('blog:post_detail', kwargs={'pk': comment.post.id}))
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)

    if request.method == "POST":
        post_id = comment.post.id
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
        return HttpResponseRedirect(reverse('blog:post_detail', kwargs={'pk': post_id}))

    return render(request, 'blog/delete_comment.html', {'comment': comment})

def home_view(request):
    return render(request, 'blog/home.html')
