from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from .models import Recipe, Comment


class RecipeForm(forms.ModelForm):
    title = forms.CharField(
        label='Имя',
        widget=forms.Textarea(),
        required=False
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(attrs={'placeholder': 'Введите краткое описание рецепта'}),
        required=False
    )
    ingredients = forms.CharField(
        label='Ингредиенты',
        widget=forms.Textarea(attrs={'placeholder': 'Введите ингредиенты, каждый с новой строки'}),
        required=False
    )
    steps = forms.CharField(
        label='Этапы приготовления',
        widget=forms.Textarea(attrs={'placeholder': 'Введите этапы приготовления, каждый с новой строки'}),
        required=False
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'image']
        labels = {
            'title': 'Имя',
            'description': 'Описание',
            'ingredients': 'Ингредиенты',
            'steps': 'Этапы приготовления',
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

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('text', css_class='form-control', rows=3),
            Submit('submit', 'Post Comment', css_class='btn btn-primary')
        )