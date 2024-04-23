from django.shortcuts import render
from .models import TodoItem
import logging


def todo_list(request):
    logger = logging.getLogger(__name__)
    logger.warning("test")
    todos = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def remove_todo(request):
    logger = logging.getLogger(__name__)
    logger.warning("test")
    if request.method == 'POST':
        todo_id = request.POST.get('todo_id')
        try:
            todo_item = TodoItem.objects.get(id=todo_id)
            todo_item.delete()
            return JsonResponse({'success': True})
        except TodoItem.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'To-do item does not exist'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})