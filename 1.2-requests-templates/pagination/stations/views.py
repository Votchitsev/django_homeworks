from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.settings import BUS_STATION_CSV


class Station:

    def __init__(self, Name, Street, District):
        self.Name = Name
        self.Street = Street
        self.District = District


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    page_number = int(request.GET.get('page', 1))

    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as st:

        read_stations = csv.DictReader(st)

        stations_list = [Station(i['Name'], i['Street'], i['District']) for i in read_stations]

    stations = Paginator(stations_list, 10)

    page = stations.get_page(page_number)

    context = {
            'bus_stations': page,
            'page': page,
        }

    return render(request, 'stations/index.html', context)
