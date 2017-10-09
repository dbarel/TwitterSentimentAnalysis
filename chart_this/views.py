from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from .sentiment_calc import sentiment_calc


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)  # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        month, day, hour = sentiment_calc('chart_this\\sentiment.csv')
        labels = ["Negative", "Positive", "Neutral"]
        data = {
            "labels": labels,
            "hour": [hour['-1'], hour['1'], hour['0']],
            "day": [day['-1'], day['1'], day['0']],
            'mounth': [month['-1'], month['1'], month['0']]

        }
        return Response(data)
