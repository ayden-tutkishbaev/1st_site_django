from django.contrib import admin

from .models import *


class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'created_at')


admin.site.register(Category)
admin.site.register(Article, AdminArticle)

# Register your models here.
