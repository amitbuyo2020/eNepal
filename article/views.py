from django.shortcuts import render
from .models import Article
from django.views.generic import (ListView, DetailView,
                                  UpdateView, DeleteView)

class ArticleList(ListView):
    queryset = Article.objects.filter(status=1).order_by('-date_posted')
    template_name = 'article/blog-home.html'

class ArticleDetail(DetailView):
    model = Article
    template_name = 'article/article_detail.html'

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query)

            results= Article.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'article/search.html', context)

        else:
            return render(request, 'article/blog-home.html')

    else:
        return render(request, 'article/blog-home.html')
