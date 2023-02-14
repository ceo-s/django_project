from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ClientForm
from .models import SportTag, ClientRequest, CoachPosts, Students, Coaches

# Create your views here.

def main_page(request):
    return render(request, "coaching/index.html")

class MyContextMixin(ContextMixin):
    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['coach']= 'Соколов Алексей'
        return context

class RequestListView(ListView, MyContextMixin):
    model = ClientRequest
    template_name = "coaching/requests.html"

class PostDetailView(UserPassesTestMixin, DetailView):
    model = ClientRequest
    template_name = "coaching/posts.html"

    def test_func(self):
        if self.request.user.is_superuser:
            return super().test_func()
        else:
            return False

class FormCreateView(LoginRequiredMixin, CreateView):
    model = ClientRequest
    form_class = ClientForm
    success_url = reverse_lazy("coaching:requests")
    template_name = "coaching/contact.html"

    
        

class UpdateFormView(UpdateView):
    model = ClientRequest
    form_class = ClientForm
    success_url = reverse_lazy("coaching:requests")
    template_name = "coaching/update_req.html"

class DeleteFormView(DeleteView):
    model = ClientRequest
    success_url = reverse_lazy("coaching:requests")
    template_name = "coaching/delete_req.html"

