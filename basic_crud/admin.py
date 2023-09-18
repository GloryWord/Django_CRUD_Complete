from django.contrib import admin
from .models import *

class BoardAdmin(admin.ModelAdmin):
    search_fields = ['subject','content']

admin.site.register(Board, BoardAdmin) # Board는 내가 만든거고 그걸 admin 페이지에 등록한다.
admin.site.register(Comment)