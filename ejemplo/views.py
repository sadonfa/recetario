from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse, Http404
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import os

# Create your views here.

class ClassEjemplo(APIView):

    def get(self, request):
        return JsonResponse({"status": "ok", "menssage":" Hola mundo desde get "}, status=200)
    
    def post(self, request):

        correo =  request.data.get('correo')
        password = request.data.get('password')

        if correo == None or password == None:
            raise Http404
        return JsonResponse({"status": "ok", "menssage":f"metodo post | correo: {correo} | contraseña: {password} "}, status=201)
        #return HttpResponse("Metodo post")
    
class ClassEjemploParametros(APIView):

    def get(self, request, id):
        return JsonResponse({"status": "ok", "menssage":f" Hola mundo desde get con id - {id} "})

    def put(self, request, id):
        return HttpResponse(f"Hola mundo desde put con id - {id}")
    
    def delete(self, request, id):
        return HttpResponse(f"Hola mundo desde delete con id - {id}")
    
   
class ClassEjemploUpload(APIView):

    def post(self, request):
        fs = FileSystemStorage()
        fecha = datetime.now()
        foto = f"{datetime.timestamp(fecha)}{os.path.splitext(str(request.FILES['file']))[1]}"
        fs.save(f"ejemplo/{foto}", request.FILES['file'])
        fs.url(request.FILES['file'])

        return JsonResponse({"status":"ok", "message":"se subio el archivo"})