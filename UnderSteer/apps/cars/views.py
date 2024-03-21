from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

car_dict = {
    'Toyota Mark II': '123',
    'Mitsubishi Lancer Evolution IX': '321',
}


def index(request):
    return render(request, "cars/carlist.html", {'car_dict': car_dict})


def detail(request, car):
    data = car_dict[car]
    return render(request, 'cars/detail.html', {'data': data})
