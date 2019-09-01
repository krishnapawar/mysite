from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('second/',views.count, name='first'),
    path('',views.main,name='main'),
    
]