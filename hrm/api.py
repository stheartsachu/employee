from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hrm.serializer import Userserializer,bulbserializer,readingserializer
from hrm.models import Users,bulbstatus

class UserList(APIView):
    def get(self,request):
        model = Users.objects.all()
        serializer = Userserializer(model,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class Bulbdata(APIView):
    def get(self,request):
        model = bulbstatus.objects.all()
        serializer = bulbserializer(model, many=True)
        return Response(serializer.data)

class temperature_reading(APIView):
    def post(self,request):
        serializer = readingserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
