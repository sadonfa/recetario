from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category as mCategoria
from .serializers import CategorySerializer
from django.http.response import JsonResponse, Http404
from http import HTTPStatus
from django.utils.text import slugify
# Create your views here.

class Category(APIView):


    def get(self, request):
        data = mCategoria.objects.order_by('-id').all()
        data_json = CategorySerializer(data, many=True)

        # return JsonResponse(data_json.data, safe=False)
        return JsonResponse({"data": data_json.data}, status=HTTPStatus.OK)
    
    def post(self, request):
        
        try:
            mCategoria.objects.create(name=request.data['nombre'])
            return JsonResponse({'estado': 'ok', 'mensaje':'producto creado con exito.'}, status=HTTPStatus.CREATED)
        except Exception as e:
            raise Http404
    

class CategoryParametros(APIView):


    def get(self, request, id):
        try:
            data = mCategoria.objects.filter(pk=id).get()

            return JsonResponse({ 'data': {'id':id, 'nombre': data.name, 'slug': data.slug}}, status=HTTPStatus.OK)
        except mCategoria.DoesNotExist:
            raise Http404
        
    def put(self, request, id):

        if request.data.get('name')==None:
            return JsonResponse({'status':'error', 'message':'El campo nombre es obligatorio'}, status=HTTPStatus.BAD_REQUEST)
        if not request.data.get('name'):
            return JsonResponse({'status':'error', 'message':'El campo nombre es obligatorio'}, status=HTTPStatus.BAD_REQUEST)
        

        try:
            data = mCategoria.objects.filter(pk=id).get()
            mCategoria.objects.filter(pk=id).update(name=request.data.get('name'), slug=slugify(request.data.get('name')))

            return JsonResponse({ 'status': 'ok', 'message':'Se modifico el registro exitosamente'}, status=HTTPStatus.OK)
        except mCategoria.DoesNotExist:
            raise Http404


    def delete(self, request, id):

        try:
            data = mCategoria.objects.filter(pk=id).get()
            mCategoria.objects.filter(pk=id).delete()

            return JsonResponse({ 'status': 'ok', 'message':'Se elimino el registro exitosamente'}, status=HTTPStatus.OK)
        except mCategoria.DoesNotExist:
            raise Http404