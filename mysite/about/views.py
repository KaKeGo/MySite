from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from .models import About, Skills
from .forms import SkillCreateForm
# Create your views here.


class AboutView(generic.ListView):
    def get(self, request, *args, **kwargs):
        template = 'about/about.html'
        abouts = About.objects.all()
        context = {
            'abouts': abouts,
        }
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = SkillCreateForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = SkillCreateForm()
        return redirect('about:about')
