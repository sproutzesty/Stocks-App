from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages
#from django.conf import settings
from decouple import config
#MYKEY = getattr(settings, "SECRET_KEY")
SECRET_KEY = config ('SECRET_KEY')
NEWS_KEY=config ('NEWS_KEY')
#print ("THIS IS MY SECRET KEY: "+MYKEY)
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
#Browser request for home page, pass into dict

def home(request):
        import requests
        import json

        if request.method =='POST':
            ticker = request.POST['ticker']
            # pass in url that calls the api
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token="+SECRET_KEY)
            #api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token="+SECRET_KEY)
			
            try:
                api = json.loads(api_request.content)
            except Exception as e:
                api = "Error..."

            return render(request, 'home.html', {'api': api, 
                'error':"Could not access the api"})
        
        else:
        
            return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})

def buyStock(request):
    	import requests
        import json

    	if api_request
			
			symbol=api.symbol
			price= api.latestPrice
			quantitiy= api.quantitiy
			res= (input(setQuantity, init:{}))

            try:
                api = json.loads(api_request.content)
			if 
		let res= await fetch(input:'http:/localhost:8000/home', init:{
			method:'POST'
			body:JSON.stringify(body)
		})
		let data= await res.json()
		console.log ('this is the data,' data )

    	return render(request, 'about.html', {})


def about(request):
    	return render(request, 'about.html', {})


def add_stock(request):
	import requests
	import json

	if request.method == 'POST':
		form = StockForm(request.POST or None)
	
		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added to your portfolio!"))				
			return redirect('add_stock')
		else:
    			messages.error("Stock could not be added")

	else:	
		ticker = Stock.objects.all()
		# save ticker info from api output into python list ('output list')
		output = []
		# modify to pull multiple stock tickers at the same time
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token="+SECRET_KEY)
			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."	

		return render(request, 'add_stock.html', {'ticker': ticker, 'output':  output})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id) # call database by primary key for id #
	item.delete()
	messages.success(request, ("Stock Has Been Deleted From Portfolio!"))
	return redirect(add_stock)

def news(request):
	import requests
	import json
	
	# News API
	#api_request = requests.get('http://newsapi.org/v2/everything?q=stocks&apiKey=</>')
	
	# BASIC - Stock News API
	api_request = requests.get('https://stocknewsapi.com/api/v1/category?section=general&items=50&token='+NEWS_KEY)
	
	# PREMIUM - Stock News API
	#api_request = requests.get('https://stocknewsapi.com/api/v1/category?section=alltickers&items=50&token='+ NEWS_KEY)
	api = json.loads(api_request.content)
	return render(request, 'news.html', {'api': api}) 
	messages.success(request, ("Stock Has Been Deleted"))
	return redirect(add_stock)

