from django.urls import path

from . import views

app_name = 'superhero'
urlpatterns = [
    path('', views.index, name='index'),
]