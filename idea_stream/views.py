from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

# from idea_stream.forms import CreateArticleForm
from idea_stream.models import Article

## function based views
# def home(request):
#     articles = Article.objects.all()
#     context = {
#         'articles': articles
#     }
#     return render(request, 'idea_stream/home.html', context)


# def create_article(request):
#     if request.method == "POST":
#         form = CreateArticleForm(request.POST)
#         if form.is_valid():
#             form_data = form.cleaned_data
#             new_article = Article(
#                 title = form_data['title'],
#                 status = form_data['status'],
#                 content = form_data['content'],
#                 word_count = form_data['word_count'],
#                 x_post = form_data['x_post'],
#             )
#             new_article.save()
#             return redirect("home")
#     else:
#         form = CreateArticleForm()
#     return render(request, "idea_stream/article_form.html", {"form": form})



## class based views
class ArticleListView(ListView):
    model = Article
    template_name = "idea_stream/home.html"
    context_object_name = 'articles'

class ArticleCreateView(CreateView):
    model = Article
    fields = ["title", "status", "content", "word_count", "x_post"]
    success_url = reverse_lazy("home")

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ["title", "status", "content", "word_count", "x_post"]
    success_url = reverse_lazy("home")


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("home")



