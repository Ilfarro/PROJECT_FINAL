from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import News

def news(request):
    news_post = News.objects.all()
    paginator = Paginator(news_post, 3)

    page = request.GET.get('page')
    news = paginator.get_page(page)
    return render(request, 'news/news.html', {'news_posts': news})

def news_detail(request, news_id):
    news = News.objects.get(pk=news_id)
    return render(request, 'news/news_detail.html', {'news':news})