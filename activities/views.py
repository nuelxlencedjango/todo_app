from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request ,'index.html' ,{'todo_items' :todo_items})

#@csrf_exempt
def add_todo(request):
    #print(request.POST)
    current_date=timezone.now()
    content = request.POST['content']
    created_obj=Todo.objects.create(added_date=current_date ,text =content)
    #print(created_obj)
    #print(created_obj.id)
    length_of_todo = Todo.objects.all().count()
    #print(length_of_todo)
    return HttpResponseRedirect('/')



def delete_todo(request ,todo_id):
    dele = Todo.objects.get(id=todo_id).delete()
    #print("deleted id:" ,dele)
    return HttpResponseRedirect('/')