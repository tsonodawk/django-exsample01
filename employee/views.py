from django.urls import reverse_lazy
from django.views import generic
from .models import Employee
from pure_pagination.mixins import PaginationMixin


class IndexView(PaginationMixin, generic.ListView):
    model = Employee
    paginate_by = 5
    ordering = ['-createddate']
    template_name = 'employee/index.html'


class DetailView(generic.DetailView):
    model = Employee
    fields = '__all__'  # or ['colmunname', 'colmunname', 'colmunname']
    template_name = 'employee/detail.html'


class CreateView(generic.edit.CreateView):
    model = Employee
    fields = '__all__'  # or ['colmunname', 'colmunname', 'colmunname']
    success_url = reverse_lazy('employee:index')
    template_name = 'employee/create.html'


class UpdateView(generic.edit.UpdateView):
    model = Employee
    fields = '__all__'  # or ['colmunname', 'colmunname', 'colmunname']
    success_url = reverse_lazy('employee:index')
    template_name = 'employee/update.html'


class DeleteView(generic.edit.DeleteView):
    model = Employee
    success_url = reverse_lazy('employee:index')
    template_name = 'employee/delete.html'
