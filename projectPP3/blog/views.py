from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.core.mail import send_mail

from .models import Post, Comment
from .forms import CommentForm, EmailPostForm, RecommendPostForm

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/post/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = 'PB'
        return super().form_valid(form)

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
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def post_detail(request, year, month, day, post):
    post_obj = get_object_or_404(
        Post,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        status=Post.Status.PUBLISHED,
    )

    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post_obj
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval')
            return HttpResponseRedirect(reverse('blog:post_detail', kwargs={
                'year': post_obj.publish.year,
                'month': post_obj.publish.month,
                'day': post_obj.publish.day,
                'post': post_obj.slug,
            }))
    else:
        comment_form = CommentForm()

    if request.user.is_authenticated:
        comments = post_obj.comments.filter(
            Q(approved=True) | Q(author=request.user)
        ).distinct().order_by('created_on')
    else:
        comments = post_obj.comments.filter(approved=True).order_by('created_on')

    comment_count = post_obj.comments.filter(approved=True).count()

    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post_obj,
            'comments': comments,
            'comment_count': comment_count,
            'comment_form': comment_form,
        }
    )

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    post = comment.post

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully.")
            publish = post.publish or post.created or timezone.now()
            return HttpResponseRedirect(reverse('blog:post_detail', kwargs={
                'year': publish.year,
                'month': publish.month,
                'day': publish.day,
                'post': post.slug,
            }))
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {
        'form': form,
        'comment': comment,
        'post_url': reverse('blog:post_detail', kwargs={
            'year': post.publish.year,
            'month': post.publish.month,
            'day': post.publish.day,
            'post': post.slug,
        }),
    })

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    post = comment.post

    if request.method == "POST":
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
        publish = post.publish or post.created or timezone.now()
        return HttpResponseRedirect(reverse('blog:post_detail', kwargs={
            'year': publish.year,
            'month': publish.month,
            'day': publish.day,
            'post': post.slug,
        }))

    return render(request, 'blog/delete_comment.html', {
        'comment': comment,
        'post_url': reverse('blog:post_detail', kwargs={
            'year': post.publish.year,
            'month': post.publish.month,
            'day': post.publish.day,
            'post': post.slug,
        }),
    })

def post_share(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} ({cd['email']}) recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['comments']}"
            send_mail(
                subject,
                message,
                from_email=None,
                recipient_list=[cd['to']],
            )
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {
        'post': post,
        'form': form,
        'sent': sent,
    })

def home_view(request):
    latest_posts = Post.published.all()[:3]
    return render(request, 'blog/home.html', {'latest_posts': latest_posts})

def custom_404(request, exception):
    return render(request, '404.html', status=404)
