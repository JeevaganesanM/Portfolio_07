from django.views.generic import DetailView, ListView
from .models import Article
class ArticleListView(ListView):
    template_name = "articles/list.html"
    context_object_name = "articles"
    paginate_by = 9
    def get_queryset(self): return Article.objects.published()
class ArticleDetailView(DetailView):
    template_name = "articles/detail.html"
    context_object_name = "article"
    def get_queryset(self): return Article.objects.published()
