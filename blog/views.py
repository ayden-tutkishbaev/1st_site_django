from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .models import *
from .forms import *


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()

    context = {
        'title': 'Main page',
        'categories': categories,
        'articles': articles
    }

    return render(request, 'blog/index.html', context)


def category_page_view(request, category_id):
    articles = Article.objects.filter(category=category_id).order_by('-created_at')
    trends = Article.objects.all().order_by('-views')

    context = {
        'title': f'Категория: {Category.objects.get(id=category_id)}',
        'articles': articles,
        'trends': trends
    }

    return render(request, 'blog/category_page.html', context)


def about_me_page(request):
    return render(request, 'blog/about_me_page.html')


def works_page(request):
    return render(request, 'blog/works_page.html')


def article_detail_page_view(request, article_id):
    article = Article.objects.get(id=article_id)
    last_articles = Article.objects.all().order_by('-created_at')

    if article.author != request.user:
        article.views += 1
        article.save()

    context = {
        'title': f'{article.title}',
        'article': article,
        'last_articles': last_articles
    }

    return render(request, 'blog/article_detail.html', context)


def add_article_view(request):
    if request.method == 'POST':
        form = AddArticleForm(data=request.POST,
                              files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', article.pk)
        else:
            pass

    elif request.method == 'GET':
        form = AddArticleForm()

    context = {
        'title': 'Add article',
        'form': form
    }

    return render(request, 'blog/add_article.html', context)


def register_user(request):
    if request.method == 'POST':
        form = RegisterUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            pass
    else:
        form = RegisterUser()

    context = {
        'title': 'User registration',
        'form': form
    }

    return render(request, 'blog/register_user.html', context)


def log_in_user(request):
    if request.method == 'POST':
        form = LoginUser(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('index')
            else:
                pass
        else:
            pass
    else:
        form = LoginUser()

    context = {
        'title': 'User registration',
        'form': form
    }

    return render(request, 'blog/login.html', context)


def log_out_user(request):
    logout(request)
    return redirect('index')
