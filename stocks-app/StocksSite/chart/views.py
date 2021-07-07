from django.shortcuts import render
from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response
   
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chartjs/index.html')

