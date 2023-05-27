from django.shortcuts import render, redirect
from . import models
from .models import Jobs
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,DeleteView
from django.contrib.auth.decorators import login_required
# Create your views here.
# def add(request):
#     if request.POST:
#         activity = request.POST['Activity']
#         description = request.POST['Description']
#         models.Jobs.objects.create(activity=activity,description=description)
#         return redirect(reverse('jobs:list'))
#     else:
#         return render(request,'jobs/jobs_form.html')
# def list(request):
#     all_jobs = models.Jobs.objects.all()
#     context={'all_jobs':all_jobs}
#     return render(request,'jobs/jobs_list.html', context=context)
# @login_required
class JobsCreateView(CreateView):
    model = Jobs
    fields = '__all__'
    success_url = '/jobs/jobs_list/'

class JobsListView(ListView):
    model = Jobs
    context_object_name = 'jobs_list'

class JobsDetailView(DetailView):
    models = Jobs
    queryset = Jobs.objects.all()

class JobsDeleteView(DeleteView):
    models = Jobs
    success_url = reverse_lazy('jobs:jobs_list')
    queryset = Jobs.objects.all()