from django.template.response import TemplateResponse 
from todo.models import TodoItem

def index(request):
    todos = TodoItem.objects.all()
    context = {'todos': todos}
    return TemplateResponse(request, template='index.html', context=context)
