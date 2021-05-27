from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
urlpatterns = [
   path('',PostListView.as_view(),name="home page"),
   path('post/<int:pk>/',PostDetailView.as_view(),name="post page"),
   path('user/<str:username>/',UserPostListView.as_view(),name="User Post"),
   path('about/',views.about,name="About us"),
   path('post/new/',PostCreateView.as_view(),name="blog page"),
   path('post/<int:pk>/update',PostUpdateView.as_view(),name="post update"),
   path('post/<int:pk>/delete',PostDeleteView.as_view(),name="post delete")
]
