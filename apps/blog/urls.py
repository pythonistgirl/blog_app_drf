from django.urls import path
from .views import PostView, RetrivePostsView

urlpatterns = [
    path('create', PostView.as_view(),),
    path('all', RetrivePostsView.as_view(),),
]