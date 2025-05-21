from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe, RecipeCategory

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = RecipeCategory.objects.create(name="Desserts")

        # Створюємо 15 рецептів
        for i in range(15):
            Recipe.objects.create(
                title=f"Recipe {i}",
                description="Опис рецепта",
                category=self.category
            )

    def test_main_view_returns_10_or_less(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertLessEqual(len(response.context['recipes']), 10)

    def test_category_detail_view(self):
        response = self.client.get(reverse('category_detail', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')
        self.assertEqual(response.context['category'], self.category)
        self.assertEqual(len(response.context['recipes']), 15)
