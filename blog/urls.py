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
    path('logout/', log_out_user, name='logout'),
    path('search/', search, name='search'),
    path('edit_article/<int:article_id>', article_edit, name='article_edit'),
    path('delete_article/<int:article_id>', article_delete, name='article_delete'),
    path('profile/<int:user_id>', profile, name='user_profile'),
    path('edit_profile/<int:user_id>', edit_profile, name='edit_profile'),
    path('about_site/', about_site, name='about_site')
]

