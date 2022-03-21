from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import About, Skills
from .forms import SkillCreateForm
# Create your views here.


class AboutView(generic.ListView):
    template_name = 'about/about.html'
    model = About
    context_object_name = 'abouts'

class SkillCreateView(generic.CreateView):
    template_name = 'about/add_skill.html'
    form_class = SkillCreateForm
    model = Skills
    success_url = reverse_lazy('about:about')
