from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import *
from .serializers import *


class EK_Champ_RegisterationView(APIView):
    serializer_project = EKPJSerializer

    def get(self, request):
        info = EKPJ.objects.all().values()
        return Response({"Your Account Info": info})

    def post(self, request):
        serializer_post_project = EKPJSerializer(data=request.data)
        if serializer_post_project.is_valid():
            # Check if the username already exists
            if EKPJ.objects.filter(username=serializer_post_project.data.get("username")).exists():
                return Response({"Notification": "Username already exists!"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Create a new user
            EKPJ.objects.create(
                username=serializer_post_project.data.get("username"),
                password=serializer_post_project.data.get("password"),
            )
            return Response({"Notification": "Your information is Added!"}, status=status.HTTP_201_CREATED)

        # Handle invalid data
        return Response({"error": "Invalid data", "details": serializer_post_project.errors}, status=status.HTTP_400_BAD_REQUEST)


class EK_Champ_LoginView(APIView):
    serializer_project = EKPJSerializerLogin

    def post(self, request):
        serializer_post_project = EKPJSerializerLogin(data=request.data)
        if serializer_post_project.is_valid():
            # Check if the user exists and passwords match
            user = EKPJ.objects.filter(username=serializer_post_project.data.get("username")).first()
            if user and user.password == serializer_post_project.data.get("password"):
                return Response({"Notification": "Your Login is Successful!"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid username or password!"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Handle invalid data
        return Response({"error": "Invalid data", "details": serializer_post_project.errors}, status=status.HTTP_400_BAD_REQUEST)


class Driver_Overview(APIView):
    serializer_project = DriverSerializer

    def get(self, request):
        # Get the search query parameter
        search_query = request.query_params.get('search', None)

        # Filter drivers based on the search query
        if search_query:
            drivers = Driver.objects.filter(
                Q(name_en__icontains=search_query) |
                Q(name_th__icontains=search_query) |
                Q(nickname__icontains=search_query)
            )
        else:
            drivers = Driver.objects.all()

        # Serialize the driver data
        driver_data = DriverSerializer(drivers, many=True).data

        # Define the column names (including id now)
        columns = ["ID", "Name (EN)", "Name (TH)", "Nickname", "Date of Birth", "QR Code", "Age"]

        # Prepare the response data
        data = {"columns": columns, "drivers": []}

        # Add driver data along with "edit" URLs
        for driver in driver_data:
            driver_info = {
                "id": driver['id'],
                "name_en": driver['name_en'],
                "name_th": driver['name_th'],
                "nickname": driver['nickname'],
                "dob": driver['dob'],
                "qr_code": driver['qr_code'],
                "age": driver['age'],
                "edit_url": f"/drivers/edit/{driver['id']}/"
            }
            data["drivers"].append(driver_info)

        return Response(data)



class Driver_Create(APIView):
    def post(self, request):
        # Check if the driver ID already exists
        driver_id = request.data.get('id')
        if Driver.objects.filter(id=driver_id).exists():
            return Response({"error": "Driver ID already exists!"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            driver = serializer.save()  # Save the new driver
            return Response({"message": "Driver created successfully", "driver": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response({"error": "Invalid data", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class Driver_Edit(APIView):
    def put(self, request, pk):
        try:
            driver = Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)

        # If the request data has the "driver" key, use it, otherwise use the whole request body
        driver_data = request.data.get("driver", request.data)

        serializer = DriverSerializer(driver, data=driver_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Driver updated successfully", "driver": serializer.data})

        return Response({"error": "Invalid data", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
