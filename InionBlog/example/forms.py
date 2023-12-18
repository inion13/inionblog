from django import forms
from .models import Recipe, Comment


class RecipeForm(forms.ModelForm):
    ingredients = forms.CharField(
        label='Ингредиенты',
        widget=forms.Textarea(attrs={'placeholder': 'Введите ингредиенты, каждый с новой строки'}),
        required=False
    )
    steps = forms.CharField(
        label='Шаги',
        widget=forms.Textarea(attrs={'placeholder': 'Введите шаги приготовления, каждый с новой строки'}),
        required=False
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'image']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'ingredients': 'Ингредиенты',
            'steps': 'Шаги',
            'image': 'Изображение',
        }

    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.cleaned_data.get('image'):
            instance.image = self.cleaned_data['image']

        if commit:
            instance.save()
        return instance


class RecipeDeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='Подтвердите удаление'
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
