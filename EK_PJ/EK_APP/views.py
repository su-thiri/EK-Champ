from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from .models import Driver
from .serializers import DriverSerializer


class EK_Champ_GetView(APIView):
    def get(self, request):
        info = EKPJ.objects.all().values()
        return Response({"Your Account Info": info})

# View for POST requests
class EK_Champ_PostView(APIView):
    def post(self, request):
        serializer_post_project = EKPJSerializer(data=request.data)
        if serializer_post_project.is_valid():
            EKPJ.objects.create(
                username=serializer_post_project.validated_data.get("username"),
                password=serializer_post_project.validated_data.get("password"),
            )
            return Response({"message": "Account created successfully!"})
        return Response(serializer_post_project.errors, status=400)

class EK_Champ_LoginView(APIView):
    serializer_project = EKPJSerializerLogin

    def get(self, request):
        info = EKPJLogin.objects.all().values()
        return Response({"Your Account Info": info})

    def post(self, request):
        serializer_post_project = EKPJSerializerLogin(data=request.data)
        if serializer_post_project.is_valid():
            EKPJ.objects.create(
                username=serializer_post_project.data.get("username"),
                password=serializer_post_project.data.get("password"),
            )

        project = EKPJ.objects.filter(username=request.data["username"]).values()
        return Response({"Notification": "Your Login is Successful!", "Project": project})


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

# View for GET requests to list drivers
class DriverListView(APIView):
    def get(self, request):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response({"drivers": serializer.data}, status=status.HTTP_200_OK)

# View for POST requests to create a new driver
class DriverCreateView(APIView):
    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Driver created successfully!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def edit_driver(request, pk):
    try:
        driver = Driver.objects.get(pk=pk)
    except Driver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)