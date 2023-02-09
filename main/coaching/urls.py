from django.urls import path
from coaching import views

app_name = 'coaching'

urlpatterns = [
    path("", views.main_page, name="main"),
    path("posts/", views.posts, name="posts"),
    path("form/", views.form, name="form"),
    path("requests/", views.requests, name="requests"),
]