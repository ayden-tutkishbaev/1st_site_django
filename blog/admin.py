from django.contrib import admin

from .models import *


class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'created_at')
    readonly_fields = ('views',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user

        super(AdminArticle, self).save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(Article, AdminArticle)
admin.site.register(Profile)

# Register your models here.
