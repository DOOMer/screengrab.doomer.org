# -*- encoding: utf-8 -*-
# Create your views here.

# newsline class based views

from django.views.generic import ListView
from apps.newsline.models import NewsLine

# наследуем класс от стандартного лист-виева
class News(ListView):
    # Нижеуказанные параметры можно также передать данному отображению через метод as_view()
    # url(r'^$', News.as_view(context_object_name='news', template_name='news.html))
    
    # model for our views
    model = NewsLine
    
    # Под данным именем наш список статей будет доступен в шаблоне
    context_object_name = "news"
    
    #наш шаблн
    template_name = "newsline/news.html"
    
    # Количество объектов на 1 страницу
    paginate_by = 10
    
    # получаем кверисет
    def get_queryset(self):
        qs = NewsLine.objects.all().order_by('-pub_date')
        #if not self.request.user.is_authenticated():
        #return qs.exclude(is_private=True)
        return qs
        