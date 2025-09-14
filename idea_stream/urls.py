from django.urls import path

from idea_stream.views import ArticleCreateView, ArticleListView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    # function based view
    # path('', home, name="home"),
    # path('articles/create/', create_article, name="article-create"),
    #class based view
    path('', ArticleListView.as_view(), name="home"),
    path('create/', ArticleCreateView.as_view(), name="article-create"),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name="article-update"),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name="article-delete"),

]