from django.shortcuts import render

from .models import Paper


from django.http import HttpResponse


def index(request):
	return HttpResponse('Paper')