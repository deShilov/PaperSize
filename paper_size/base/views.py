from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.urls import reverse_lazy
from .models import Paper


class Home(ListView):
	template_name = 'base/home.html'
	model = Paper
	context_object_name = 'papers'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['papers'] = context['papers'].filter(public=True)
		return context


class PaperList(LoginRequiredMixin, ListView):
	template_name = 'base/PaperList.html'
	model = Paper
	context_object_name = 'papers'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['papers'] = context['papers'].filter(user=self.request.user)
		return context

 
class PaperDetail(DetailView):
	model = Paper
	context_object_name = 'paper'
	template_name = 'base/PaperDetail.html'


class PaperCreate(LoginRequiredMixin, CreateView):
	template_name = 'base/PaperCreate.html'
	model = Paper
	fields = ['title', 'description', 'paper', 'public']
	success_url = reverse_lazy('papers')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(PaperCreate, self).form_valid(form)


class PaperUpdate(LoginRequiredMixin, UpdateView):
	template_name = 'base/PaperCreate.html'
	model = Paper
	fields = ['title', 'description', 'paper', 'public']
	success_url = reverse_lazy('papers') 


class PaperDelete(LoginRequiredMixin, DeleteView):
	template_name = 'base/PaperDelete.html'
	model = Paper
	context_object_name = 'paper'
	success_url = reverse_lazy('papers')


class LoginView(LoginView):
	template_name = 'base/LoginView.html'
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('papers')


class RegisterView(FormView):
	template_name = 'base/RegisterView.html'
	form_class = UserCreationForm
	redirect_authenticated_user = True
	success_url = reverse_lazy('papers')

	def form_valid(self, form):
		user = form.save()
		if user is not None:
			login(self.request, user)
		return super(RegisterView, self).form_valid(form)

	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('papers')
		return super(RegisterView, self).get(*args, **kwargs)
