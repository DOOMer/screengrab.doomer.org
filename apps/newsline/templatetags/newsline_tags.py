# -*- encoding: utf-8 -*-

from newsline.models import NewsLine
from django import template
register = template.Library()

def get_news_lines(parser, token):
    try:
        tag_name, count_lines = token.split_contents()
    except:
        raise template.TemplateSyntaxError, "%r tag requires exactly one argument" % token.contents.split()[0]
    
    # пепедаем count_lines в инит-метод класса  NewsLineObjectNode
    return NewsLineObjectNode(count_lines)

class NewsLineObjectNode(template.Node):
    def __init__(self, count_lines):
        # set count of get lines
        if int(count_lines) == 0:
            count_lines = NewsLine.objects.count()
        
        self.num_lines = count_lines
        
    def render(self, context):
        # add newslines item to context map
        context['newslines'] = get_lines(self.num_lines)
        # return empty strin, whe template tag set contex var
        return ''
        
def get_lines(count):
    # list of returned lines
    lines = []
    
    for i in NewsLine.objects.all().order_by('-pub_date')[:count]:
        lines.append({'date': i.pub_date, 'text': i.text,})
    
    return lines
    

# обственно регистрация тега
register.tag("newslines", get_news_lines)