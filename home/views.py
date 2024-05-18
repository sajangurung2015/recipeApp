from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from recipes.models import Recipe

# Create your views here.
class index(ListView):
    template_name = 'index.html'
    model = Recipe
    context_object_name = 'recipes'
    
    def get_queryset(self):
        return self.model.objects.all()[:3]