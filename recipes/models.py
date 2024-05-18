from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# Create your models here.
class RecipeCategory(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    
    def __str__(self):
        return str(self.title)
    
class Recipe(models.Model):
    user = models.ForeignKey(User, related_name='recipe_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    instructions = models.TextField(max_length=10000, null=False, blank=False)
    ingredients = models.TextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size = [400, None],
        quality=75,
        upload_to="recipes/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    recipe_category = models.ForeignKey(RecipeCategory, related_name='recipe_category', on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)