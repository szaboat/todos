from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from todo.forms import TodoItemForm
from todo.models import TodoItem

def index(request):
    todos = TodoItem.objects.all()
    context = {'todos': todos}
    return TemplateResponse(request, template='index.html', context=context)

def edit(request, id=None):
    if id:
        action = 'edit'
        todo = get_object_or_404(TodoItem, pk=id)
    else:
        action = 'new'
        todo = TodoItem()

    if request.POST:
        form = TodoItemForm(request.POST, initial=todo)
        if form.is_valid():
            todo.name = form.cleaned_data.get('name')
            todo.done = form.cleaned_data.get('done')
            todo.save()
            redirect_url = reverse(index)
            return HttpResponseRedirect(redirect_url)
    else:
        form = TodoItemForm(initial={'name': todo.name, 'done': todo.done })

    context = {
        'form': form,
        'action': action,
    }
    return TemplateResponse(request, 'edit.html', context=context)

