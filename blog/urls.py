from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', category_page_view, name='category_page'),
    path('about_me_page/', about_me_page, name='about_me_page'),
    path('works_page/', works_page, name='works_page'),
    path('article/<int:article_id>/', article_detail_page_view, name='article_detail'),
    path('add_article/', add_article_view, name='add_article'),
    path('register/', register_user, name='register'),
    path('login/', log_in_user, name='login'),
    path('logout/', log_out_user, name='logout')
]

