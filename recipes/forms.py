from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','description','ingredients','instructions','image','image_alt','recipe_category']
        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
            "ingredients": forms.Textarea(attrs={"rows": 5}),
            "instructions": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Recipe Title",
            "recipe_category": "Recipe Ctegory",
            "description": "Description",      
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "image": "Recipe Image",
            "image_alt": "Describe Image",
            
        }