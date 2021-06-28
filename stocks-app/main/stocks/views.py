from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from stocks.models import Stock
from stocks.serializers import StockSerializer

@csrf_exempt
def stock_list(request):
    """
    List all code stocks, or create a new stock.
    """
    if request.method == 'GET':
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def stock_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        stock = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StockSerializer(stock)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StockSerializer(stock, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        stock.delete()
        return HttpResponse(status=204)