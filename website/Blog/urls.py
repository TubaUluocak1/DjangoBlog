from django.urls import path
from django.views.generic import TemplateView
from . import views



urlpatterns = [
    path('',views.index,name="home"),
    path('home',views.index,name="home"),
    path('pages1',views.pages1,name="pages1"),
    path('categories1',views.categories1,name="categories1"),
    path('games',views.games,name="games"),
    path('contact',views.contact,name="contact"),
    path('post',views.post,name="post"),
    path('<slug>',views.PostDetailView.as_view(),name="post"),
]