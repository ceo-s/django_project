from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import User
from coaching.models import Students, Coaches
from. forms import RegisterUser
# Create your views here.

class LogInUser(LoginView):
    template_name = "login.html"
    pass

class RegisterUserView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUser
    success_url = reverse_lazy('users:login')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if self.request.user.type == "ADMIN":
            pass
        elif self.request.user.type == "STUDENT":
            Students.objects.create(pk=self.request.user.pk)
        elif self.request.user.type == "COACH":
            Coaches.objects.create(pk=self.request.user.pk)

        return super().form_valid(form)


"""class CabinetListView(ListView):
    model = Students
    template_name = "cabinet.html"""


class CabinetDetailView(UserPassesTestMixin, DetailView):
    template_name = "cabinet.html"

    def test_func(self):
        if self.request.user.type == "STUDENT":
            self.model = Students
            return True
        elif self.request.user.type == "COACH":
            self.model = Coaches
            return True
        else:
            return False  