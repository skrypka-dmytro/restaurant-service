from django.http import HttpResponse
from django.shortcuts import render

from restaurant.models import DishType, Cook, Dish


def index(request) -> HttpResponse:
    num_dish_type = DishType.objects.count()
    num_cook = Cook.objects.count()
    num_dish = Dish.objects.count()

    context = {
        "num_dish_type": num_dish_type,
        "num_cook": num_cook,
        "num_dish": num_dish,
    }

    return render(request, "taxi/index.html", context=context)
