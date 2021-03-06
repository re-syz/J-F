"""
131072
201118 - initial
helloworld/view.py



"""


# =============

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
import random
from account.models import Geo, Taste
import requests
import json
import math


# def geo_locate(request):
#
#     if request.user.is_authenticated:
#         _user = request.user
#
#         _lat = 0.000000
#         _lng = 0.000000
#
#         API_key = {'key': None}
#         API_key['key'] = getattr(settings, 'GOOGLE_MAPS_API_KEY', None)
#
#         if API_key['key'] is not None:
#             r = requests.post('https://www.googleapis.com/geolocation/v1/geolocate', params=API_key)
#
#             if r.status_code == requests.codes.ok:
#                 geo_info = json.loads(r.text)
#
#                 _lat = geo_info['location']['lat']
#                 _lng = geo_info['location']['lng']
#
#                 if _lat != 0.000000 and _lng != 0.000000 and _lat is not None and _lng is not None:
#                     if Geo.objects.filter(user=_user).count() == 0:
#                         _username = request.user.username
#                         Geo.objects.create(lat=_lat, lng=_lng, username=_username, user=_user)
#
#                     else:
#                         current_user = Geo.objects.get(user=_user)
#                         current_user.lat = _lat
#                         current_user.lng = _lng
#                         current_user.save()

def geo_locate(request):

    if request.user.is_authenticated:
        _user = request.user

        _lat = 0.000000
        _lng = 0.000000

        if request.method == 'POST':
            geo_info = json.loads(request.body)

            _lat = geo_info['location']['lat']
            _lng = geo_info['location']['lng']

            if _lat != 0.000000 and _lng != 0.000000 and _lat is not None and _lng is not None:
                if Geo.objects.filter(user=_user).count() == 0:
                    _username = request.user.username
                    Geo.objects.create(lat=_lat, lng=_lng, username=_username, user=_user)

                else:
                    current_user = Geo.objects.get(user=_user)
                    current_user.lat = _lat
                    current_user.lng = _lng
                    current_user.save()



def index(request):

    return render(request, 'index.html', locals())


def geo(request):

    geo_locate(request)

    return render(request, 'geo.html', locals())


def match(request):
    # user_list = User.objects.all()
    # taste = Taste.objects.all()
    # info = []
    # for i in range(len(taste)):
    #     indi = ""
    #     user_info = {}
    #     indi = str(taste[i])
    #     indi = indi.split(',')
    #     user_info = {'id': int(indi[0]),
    #                  'username': indi[1],
    #                  'self_attr': [float(indi[2]), float(indi[3]), float(indi[4]), float(indi[5]), float(indi[6])],
    #                  'prtn_attr': [float(indi[7]), float(indi[8]), float(indi[9]), float(indi[10]), float(indi[11])]
    #     }
    #     user_info["self_diff"] = "%.2f" % float(math.sqrt(sum(user_info["self_attr"])))
    #     user_info["prtn_diff"] = "%.2f" % float(math.sqrt(sum(user_info["prtn_attr"])))
    #     info.append(user_info)

    # print(info);
    # index = [1,2,3,4];
    # array = {"4.6":'admin2',"3.2":'admin3', "2.1":'admin1',"1.9":"admin4"}

    test = [2, 4, 3,1];
    test.sort();

    return render(request, 'match.html',locals())


def test(request):

    geo_locate(request)

    return render(request, 'test.html', locals())
