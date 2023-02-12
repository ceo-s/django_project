from django.urls import path
from coaching import views

app_name = 'coaching'

urlpatterns = [
    path("", views.main_page, name="main"),
    path("posts", views.main_page, name="govno"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="posts"),
    path("form/", views.FormCreateView.as_view(), name="form"),
    path("requests/", views.RequestListView.as_view(), name="requests"),
    path("update_request/<int:pk>", views.UpdateFormView.as_view(), name="upd"),
    path("delete/<int:pk>", views.DeleteFormView.as_view(), name="del"),
]