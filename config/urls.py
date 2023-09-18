from django.contrib import admin
from django.urls import path, include
from basic_crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic_crud/', include('basic_crud.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),

]
