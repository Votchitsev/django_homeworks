from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def get_recipe(request, dish):
    ingredients = DATA[dish]
    quantity = int(request.GET.get('quantity', 1))
    ingredients_based_on_quantity = {ingredient[0]: ingredient[1] * quantity for ingredient in ingredients.items()}
    context = {'recipe': ingredients_based_on_quantity}
    return render(request, 'calculator/index.html', context=context)
