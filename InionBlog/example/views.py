from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Recipe, Comment
from .forms import RecipeForm, RecipeDeleteForm, CommentForm
from .utils import is_superuser


def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})


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
    return render(request, 'main.html')


# @login_required
def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def recipe_list(request):
    lst_recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'recipe_list.html', {'lst_recipes': lst_recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.description = recipe.description.split('\n')
    recipe.ingredients = recipe.ingredients.split('\n')
    recipe.steps = recipe.steps.split('\n')
    comments = Comment.objects.filter(recipe=recipe).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
            redirect_url = reverse('recipe_detail', kwargs={'recipe_id': recipe_id})
            redirect_url += '#comments-section'
            return redirect(redirect_url)
    else:
        form = CommentForm()

    return render(request, 'recipe_detail.html',
                  {'recipe': recipe, 'comments': comments, 'form': form})


@user_passes_test(is_superuser, login_url='/registration/')
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect('recipe_detail', recipe_id=instance.pk)
    else:
        form = RecipeForm()

    return render(request, 'create_recipe.html', {'form': form})


@user_passes_test(is_superuser, login_url='/registration/')
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe})


@user_passes_test(is_superuser, login_url='/registration/')
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


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == comment.user or request.user.is_superuser:
        comment_recipe_id = comment.recipe.pk
        comment.delete()
        redirect_url = reverse('recipe_detail', kwargs={'recipe_id': comment_recipe_id})
        redirect_url += '#comments-section'
        return redirect(redirect_url)

    return redirect('recipe_detail', recipe_id=comment.recipe.pk)
