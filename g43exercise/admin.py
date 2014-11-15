from django.contrib import admin
from g43exercise.models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'category', 'pub_date', 'hero_image', 'optional_image')
	list_filter = ['pub_date']

# Register your models here.
admin.site.register(Article, ArticleAdmin)