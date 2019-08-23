from django.contrib import admin

from .models import Article, Category, Comment, UserAccount


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(UserAccount)
