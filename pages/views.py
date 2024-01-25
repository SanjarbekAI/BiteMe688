from django.shortcuts import render

from foods.models import FoodsModel
from pages.models import EventsModel


def home_page_view(request):
    special_food = FoodsModel.objects.filter(is_special=True).first()
    popular_foods = FoodsModel.objects.all()
    events = EventsModel.objects.filter(status=True)[:2]
    context = {
        'abs': popular_foods,
        'special_food': special_food,
        'events': events
    }
    return render(request, 'index.html', context)
