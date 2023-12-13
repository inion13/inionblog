from django.shortcuts import render
from django.http import HttpResponse


lst_recipes = [
    {'id': 1, 'title': 'Гороховый суп с ветчиной и бараньими ребрышками',
     'description': 'Всем привет! Гороховый суп, '
                    'наряду с борщом, - один из самых любимых в нашей семье. Особенно его обожают дети. '
                    'Я готовлю его уже много лет. А вот баранина всего пару лет назад плотно закрепилась '
                    'в нашем рационе. Вначале дети не хотели признавать новый продукт, но после перловки с бараниной, '
                    'томленой баранины в духовке и ленивого плова из баранины стали есть её с удовольствием. Логичным '
                    'продолжением кулинарных экспериментов было объединение этих двух продуктов в одном блюде. Так '
                    'появился гороховый суп с бараньими ребрышками. Не забудьте поставить лайк этой публикации и '
                    'подписаться на канал, если этот рецепт вам понравился. Так вы поможете его развитию. Вам не '
                    'трудно, а мне приятно :) И не бойтесь экспериментировать на кухне, а потом делиться своими '
                    'рецептами.'},
    {'id': 2, 'title': ' ', 'description': ' '},
    {'id': 3, 'title': ' ', 'description': ' '},
    {'id': 4, 'title': ' ', 'description': ' '},
    {'id': 5, 'title': ' ', 'description': ' '}
]


def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def recipes(request):
    global lst_recipes
    context = {'lst_recipes': lst_recipes}
    return render(request, 'recipes.html', context)


def recipe(request, recipe_id):
    global lst_recipes
    result = {}
    for i in lst_recipes:
        if i['id'] == recipe_id:
            result['title'] = i['title']
            result['description'] = i['description']
            break
    return render(request, 'recipe.html', result)


'''def create_item(request):
    item = Item(name='Молоко', quantity=5, price=500)
    item.save()
    result = f'{item.name} Количество {item.quantity} Цена {item.price}'
    return HttpResponse(result)


def read_item(request, item_id):
    item = Item.objects.filter(pk=item_id).first()
    result = f'{item.name} Количество {item.quantity} Цена {item.price}'
    return HttpResponse(result)


def update_item(request, item_id):
    item = Item.objects.filter(pk=item_id).first()
    item.name = 'Гвозди'
    item.save()
    result = f'{item.name} Количество {item.quantity} Цена {item.price}'
    return HttpResponse(result)


def delete_item(request, item_id):
    item = Item.objects.filter(pk=item_id).first()  # pk - это primary key
    item.delete()
    return HttpResponse('Успешно')
'''