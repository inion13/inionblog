from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Ingredient
from .forms import RecipeForm, RecipeDeleteForm


def is_superuser(user):
    return user.is_superuser


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


# @login_required
def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def recipe_list(request):
    lst_recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'lst_recipes': lst_recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.steps = recipe.steps.split('\n')
    return render(request, 'recipe_detail.html', {'recipe': recipe})


@user_passes_test(is_superuser, login_url='/registration/')
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('recipe_detail', recipe_id=instance.pk)
    else:
        form = RecipeForm()

    return render(request, 'create_recipe.html', {'form': form})


def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe})


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm_delete']:
            recipe.delete()
            return redirect('recipe_list')
    else:
        form = RecipeDeleteForm()
    return render(request, 'delete_recipe.html', {'form': form, 'recipe': recipe})
