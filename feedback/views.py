from django.shortcuts import render, redirect
from .forms import FeedBackForm
from django.views.generic import View, ListView, TemplateView
from django.shortcuts import render
from .models import FeedBack
from django.http import HttpResponse
from django.template import loader



class FeedBackView(View):
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/main")
