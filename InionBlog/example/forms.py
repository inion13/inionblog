from django import forms
from .models import Recipe, Ingredient


class RecipeDeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='Подтвердите удаление'
    )


class RecipeForm(forms.ModelForm):
    ingredients = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Введите ингредиенты, каждый с новой строки'}),
        required=False
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'image']

    def clean_ingredients(self):
        ingredients_data = self.cleaned_data['ingredients']
        ingredients_list = [ingredient.strip() for ingredient in ingredients_data.split('\n') if ingredient.strip()]
        return ingredients_list

    def save(self, commit=True):
        # Создаем или получаем объекты Ingredient и связываем их с рецептом
        ingredients_list = self.cleaned_data.get('ingredients', [])

        # Исключаем ингредиенты из данных, чтобы они не попали в get_or_create
        cleaned_data = self.cleaned_data.copy()
        cleaned_data.pop('ingredients', None)

        instance, created = Recipe.objects.get_or_create(**cleaned_data)  # Получаем или создаем объект

        if created:
            # Если объект был создан, связываем ингредиенты
            for ingredient_name in ingredients_list:
                ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_name)
                instance.ingredients.add(ingredient)

        if commit:
            instance.save()

        return instance
