from django import forms
from idea_stream.models import Article

# for function based views
# class CreateArticleForm(forms.Form):
#     ARTICLE_STATUS = (
#         ("draft", "draft"),
#         ("in_progress", "in progress"),
#         ("published", "published")
#     )
#     title = forms.CharField(max_length=100)
#     content = forms.CharField(widget=forms.Textarea)
#     word_count = forms.IntegerField()
#     x_post = forms.CharField(widget=forms.Textarea, required=False)
#     status = forms.ChoiceField(choices=ARTICLE_STATUS)


# equivalent to the class above, pick one:
# class CreateArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ("title", "status", "content", "word_count", "x_post")
