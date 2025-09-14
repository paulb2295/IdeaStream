from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from idea_stream.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "idea_stream/home.html"
    context_object_name = 'articles'


class ArticleCreateView(CreateView):
    model = Article
    fields = ["title", "status", "content", "x_post"]
    success_url = reverse_lazy("home")


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ["title", "status", "content", "x_post"]
    success_url = reverse_lazy("home")


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("home")
