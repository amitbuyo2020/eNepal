from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    lis_display = ('title', 'slug', 'status', 'date_posted')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
