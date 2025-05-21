import random
from django.shortcuts import render
from .models import Recipe

def main(request):
    # Отримуємо усі рецепти
    recipes = list(Recipe.objects.all())
    
    # Обираємо рандомні 10
    random_recipes = random.sample(recipes, min(len(recipes), 10))
    
    # Передаємо їх до main
    return render(request, 'main.html', {'recipes': random_recipes})


from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipeCategory

def category_detail(request, category_id):
    # Отримуємо категорії за ID
    category = get_object_or_404(RecipeCategory, id=category_id)
    
    # Отримуэмо усі рецепти з категорії
    recipes = Recipe.objects.filter(category=category)
    
    # Передаємо дані
    return render(request, 'category_detail.html', {
        'category': category,
        'recipes': recipes
    })

