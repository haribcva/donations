from django.shortcuts import render
from django.http import HttpResponse
from donations.models import RoomDetails
from donations.models import CoinsDonated
from django.core.exceptions import ObjectDoesNotExist

import math

def total_coins(coin_info):
    # floating point arithmentic has rounding errors, need to fix it
    total = coin_info.numPenny * (0.01) + coin_info.numNickel * (0.05) + coin_info.numDime * (0.10) + coin_info.numQuaters * (0.25) + coin_info.numDollars;
    dollars = math.trunc(total)
    cents = total - dollars
    cents = math.trunc(cents * 100)
    total = dollars + (cents/100) 

    return (total)

# Create your views here.
def all_room_detail(request):
   rooms = RoomDetails.objects.all()
   school_total = 0.0
   room_total = 0.0

   for room in rooms:
       coin_info_list = CoinsDonated.objects.filter(room_id=room.id)
       room_total = 0.0
       for coin_info in coin_info_list:
           room_total = room_total + total_coins(coin_info)
           school_total = school_total + room_total
       room.room_total = room_total

   context = {'rooms_list': rooms, 'total': school_total}
   return render(request, 'donations/room_details.html', context)

def room_detail(request, room_name):
    coin_info_list = []
    try:
        room = RoomDetails.objects.get(name=room_name)
        coin_info_list = CoinsDonated.objects.filter(room_id=room.id)
        # a list is returned with date & coins collected.
        for coin_info in coin_info_list:
            coin_info.total = total_coins(coin_info)
    except ObjectDoesNotExist:
        pass

    context = {'details_list':coin_info_list, 'room_name':room_name}
    return render(request, 'donations/details_of_a_room.html', context)
