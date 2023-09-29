from django.urls import path, include
from . import views
from .views import  HomeView, DetailsView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [

    # path("", views.home, name="home"),
    # path("new/", views.index)

    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", DetailsView.as_view(), name="article-detail"),
    path("add_post/", AddPostView.as_view(), name ="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),

]
