from django.contrib import admin
from .models import Article
from .models import Like, Comments, Profile
# Register your models here.

admin.site.register(Like)


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ['article_title']
    prepopulated_fields = {'slug': ('article_title',)}


admin.site.register(Article, ArticleAdmin)

admin.site.register(Comments)
admin.site.register(Profile)