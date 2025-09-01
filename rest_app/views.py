from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets
# Create your views here.
# class based
class crudoperation(APIView):
    def post(self,request):
        serializer=student_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"Data Added Successfully","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,student_id=None):
        try:
            if student_id==None:
                students=student_table.objects.all()
                serializer=student_serializer(students,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                student=student_table.objects.get(id=student_id)
                serializer=student_serializer(student)
                return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,student_id):
        try:
            if student_id:
                student=student_table.objects.get(id=student_id)
                serializer=student_serializer(student,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response("Student id must")
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,student_id):
        try:
            if student_id:
                student=student_table.objects.get(id=student_id)
                student.delete()
                return Response("Data deleted successfully")
            else:
                return Response("student id must")
        except Exception as e :
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
# function based
# @api_view(["GET","POST"])
# def crudfunction(request):
#     if request.method=="POST":
#         serializer=student_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"Data added suceesfully","data":serializer.data},status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_200_OK)
# generic based
# class getandpostgenerics(generics.ListCreateAPIView):
#     queryset=student_table.objects.all()
#     serializer_class=student_serializer
# class retrivegenerics(generics.RetrieveUpdateDestroyAPIView):
#     queryset=student_table.objects.all()
#     serializer_class=student_serializer

# viewset
class setview(viewsets.ModelViewSet):
    queryset=student_table.objects.all()
    serializer_class=student_serializer