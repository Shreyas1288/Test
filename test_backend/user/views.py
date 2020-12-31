from django.shortcuts import render
# 
from user.models import Dataset
from user.serializers import DatasetSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
# Create your views here.

class DataList(APIView):
    def get(self, request, format = None):
        datum = Dataset.objects.all()
        serializer = DatasetSerializer(datum , many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DatasetSerializer(data  = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DataDetail(APIView):
    def get_object(self, pk):
        try:
            return Dataset.objects.get(pk=pk)
        except Dataset.DoesNotExist:
            raise HTTP404
    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = DatasetSerializer(data)
        return Response(serializer.data)
    def put(self, request, pk, format = None):
        data =  self.get_object(pk)
        serializer  = DatasetSerializer(data, data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_204_NO_CONTENT)     
    def delete(self, request, pk, format=None):
        data  = self.get_object(pk)
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)





#-----------below is using function view in rest framework----------
# from rest_framework.decorators import api_view
# @api_view(['GET', 'POST'])
# def data_list(request, format=None):
#     if request.method == 'GET':
#         datum = Dataset.objects.all()
#         serializer = DatasetSerializer(datum, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
        
#         serializer = DatasetSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status =status.HTTP_201_CREATED)
#         return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def data_detail(request, pk, format=None):
#     try :
#         data = Dataset.objects.get(pk =pk)
#     except Dataset.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DatasetSerializer(data)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         # updated_data = JSONParser().parse(request)
#         serializer = Dataset.Serializer(data, data =request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         data.delete()
#         return Response(status =status.HTTP_204_NO_CONTENT)

#---------below is the method one----------
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# @csrf_exempt
# def data_list(request):
#     if request.method == 'GET':
#         datum = Dataset.objects.all()
#         serializer = DatasetSerializer(datum, many=True)
#         return JsonResponse(serializer.data, safe = False)

#     elif request.method == 'POST':
#         data  = JSONParser().parse(request)
#         serializer = DatasetSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status = 201)
#         return JsonResponse(serializer.errors, status = 400)

# @csrf_exempt
# def data_detail(request, pk):
#     try :
#         data = Dataset.objects.get(pk =pk)
#     except Dataset.DoesNotExist:
#         return HttpResponse(status = 404)

#     if request.method == 'GET':
#         serializer = DatasetSerializer(data)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         updated_data = JSONParser().parse(request)
#         serializer = Dataset.Serializer(data, data = updated_data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         data.delete()
#         return HttpResponse(status = 204)
