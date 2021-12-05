from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from dataclasses import dataclass

from pagination.settings import BUS_STATION_CSV


@dataclass
class Station:
    Name: str
    Street: str
    District: str


read_stations = csv.DictReader(open(BUS_STATION_CSV, newline='', encoding='utf-8'))
stations_list = [Station(i['Name'], i['Street'], i['District']) for i in read_stations]


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = request.GET.get('page', 1)
    stations = Paginator(stations_list, 10)
    page = stations.get_page(int(page_number))
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context=context)
