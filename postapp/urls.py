from .views import hello, greet, greet2, PostDetailView, PostListView, PostCreateView, DeletePost, UpdatePost
from django.urls import path

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('greet/', greet, name='greeting'),
    path('greet2/', greet2, name='greeting2'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('', PostListView.as_view(), name="home"),
    path('new/', PostCreateView.as_view(), name="new_post"),
    path('delete/<int:pk>/', DeletePost.as_view(), name="delete_post"),
    path('<int:pk>/edit', UpdatePost.as_view(), name="update")
]
