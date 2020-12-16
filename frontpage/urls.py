from django.contrib import admin
from django.urls import path
from frontpage import views

#URL dispatching here -> Manual Comment

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about_devs'),
    path('start', views.start, name='start'),
    path('results', views.results, name='results'),
    path('submit_form', views.submit_form, name='submit')
]