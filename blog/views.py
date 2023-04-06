from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .forms import CommentForm
from .models import Post, Comment


def main_page(request):
    post_list = Post.objects.order_by('pub_date')  # В порядку зростання по даті
    paginator = Paginator(post_list, 4)  # показуємо 4 пости на сторінці
    page = request.GET.get('page')  # беремо номер сторінки з параметру запиту
    posts = paginator.get_page(page)  # витягуємо пости для поточної сторінки
    return render(request, 'main.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    else:
        form = CommentForm()
    return render(request, 'post.html', {'post': post, 'form': form})
