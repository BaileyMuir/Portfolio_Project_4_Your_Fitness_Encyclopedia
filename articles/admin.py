from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Article)
class PostAdmin(SummernoteModelAdmin):

    summernote_field = ('article_content')

