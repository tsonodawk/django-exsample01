from django.views import generic
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm


class TodoListView(generic.ListView):
    model = Todo
    paginate_by = 5


class TodoDetailView(generic.DetailView):
    model = Todo


class TodoCreateView(generic.CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')


class TodoUpdateView(generic.UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')


class TodoDeleteView(generic.DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:list')
