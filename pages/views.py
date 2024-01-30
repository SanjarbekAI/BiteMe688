from django.http import HttpResponse
from django.shortcuts import render, redirect

from foods.models import FoodsModel
from pages.forms import EmailForm, OrderForm
from pages.models import EventsModel, FeedbacksModel, EmailModel
from staff.models import ChefsModel


def home_page_view(request):
    special_food = FoodsModel.objects.filter(is_special=True).first()
    popular_foods = FoodsModel.objects.all()
    events = EventsModel.objects.filter(status=True)[:2]
    feedbacks = FeedbacksModel.objects.all()
    members = ChefsModel.objects.all().order_by('-pk')
    context = {
        'abs': popular_foods,
        'special_food': special_food,
        'events': events,
        'feedbacks': feedbacks,
        'members': members
    }
    return render(request, 'index.html', context)


def create_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            email_model = EmailModel.objects.filter(email=email).first()
            if not email_model:
                form.save()
                return redirect('/')
            else:
                pass
        else:
            return redirect(request, '/')
    else:
        return render(request, '/')


def create_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse(form.errors, status=400)

