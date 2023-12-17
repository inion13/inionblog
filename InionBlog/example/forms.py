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
        label='Ингредиенты',
        widget=forms.Textarea(attrs={'placeholder': 'Введите ингредиенты, каждый с новой строки'}),
        required=False
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'image']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'steps': 'Шаги',
            'image': 'Изображение',
        }

    def clean_ingredients(self):
        ingredients_data = self.cleaned_data['ingredients']
        ingredients_list = [ingredient.strip() for ingredient in ingredients_data.split('\n') if ingredient.strip()]
        return ingredients_list

    def save(self, commit=True):
        instance, created = super().save(commit=False), False

        if not instance.pk:
            created = True

        if commit:
            instance.save()

        ingredients_list = self.cleaned_data.get('ingredients', [])

        for ingredient_name in ingredients_list:
            ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_name)
            instance.ingredients.add(ingredient)

        return instance
