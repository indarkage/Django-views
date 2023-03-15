from django.views.generic import ListView, DetailView
from .models import New, Category
from datetime import datetime

class NewsList(ListView):
    model = New  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = New.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

# создаём представление, в котором будут детали конкретного отдельного товара
class NewsDetail(DetailView):
    model = New # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'new.html' # название шаблона будет product.html
    context_object_name = 'new' # название объекта
