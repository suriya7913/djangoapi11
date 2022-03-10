from urllib import response
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drfapp.serializers import StudentSerializer
from drfapp.models import Student
from rest_framework.permissions import IsAuthenticated

class TesView(APIView):

  permission_classes=(IsAuthenticated,)

  def get(self, request, *args , **kwargs):
    qs=Student.objects.all()
    student1 =qs.first()
    serializer=StudentSerializer(qs, many=True)

    return Response(serializer.data)
  def post(self,request, *args, **kwargs):
    serialzer=StudentSerializer(data=request.data)
    if serialzer.is_valid():
      serialzer.save()
      return Response(serialzer.data)
    else:
      return Response(serialzer.errors)
