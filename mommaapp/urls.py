from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("health-index/", views.health_index,
         name="health_index"),
    path("home-this-week/", views.home2, name= "home2"),
    path("search-results/",views.search_results,name="search_results"),
    path("about/",views.about,name="about"),
    path("blog",views.blog,name="blog")




    ]



