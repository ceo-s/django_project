from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path("login/", views.LogInUser.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterUserView.as_view(), name="register"),
    path("cabinet/<int:pk>/", views.CabinetDetailView.as_view(), name="cabinet"),
]