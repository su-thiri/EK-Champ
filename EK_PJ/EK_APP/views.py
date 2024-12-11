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
from .models import Driver, SearchLog, Round
from .serializers import DriverSerializer, RoundSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from .models import Driver, SearchLog
from .serializers import DriverSerializer
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User



# View to fetch account info (GET request)
class EK_Champ_GetView(APIView):
    def get(self, request):
        # Fetch account info (if the user is authenticated)
        if request.user.is_authenticated:
            info = EKPJ.objects.all().values()  # Modify this as per your logic
            return Response({"Your Account Info": info})
        else:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)


# View to handle POST requests for creating a user (registering)
@method_decorator(csrf_exempt, name='dispatch')
class EK_Champ_PostView(APIView):
    def post(self, request):
        # Use serializer to validate incoming data
        serializer_post_project = EKPJSerializer(data=request.data)
        if serializer_post_project.is_valid():
            # Create a new user with hashed password
            username = serializer_post_project.validated_data.get("username")
            password = serializer_post_project.validated_data.get("password")
            
            # Check if the user already exists
            if User.objects.filter(username=username).exists():
                return Response({"error": "User with this username already exists."}, status=status.HTTP_400_BAD_REQUEST)

            # Create new user and hash the password
            user = User.objects.create_user(username=username, password=password)
            user.save()

            return Response({"message": "Account created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer_post_project.errors, status=status.HTTP_400_BAD_REQUEST)


# View for login (POST request) to authenticate the user and provide JWT token
class EK_Champ_LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user using the provided credentials
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        # If credentials are valid, generate a JWT token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            'message': 'Login successful!',
            'token': access_token  # Return the JWT token
        }, status=status.HTTP_200_OK)

@api_view(['POST'])
def refresh_token(request):
    refresh_token = request.data.get('refresh')
    if not refresh_token:
        return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        refresh = RefreshToken(refresh_token)
        access_token = str(refresh.access_token)
        return Response({
            'access_token': access_token
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class DriverListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        search_term = request.GET.get('search', '')
        sort_by = request.GET.get('sort_by', 'Driver_ID')
        order = request.GET.get('order', 'asc')

        # Search functionality
        drivers = Driver.objects.all()
        if search_term:
            drivers = drivers.filter(
                Q(name_en__icontains=search_term) |
                Q(name_th__icontains=search_term) |
                Q(nickname__icontains=search_term) |
                Q(qr_code__icontains=search_term) |
                Q(age__icontains=search_term)
            )

        # Sorting functionality
        if order == 'desc':
            sort_by = f'-{sort_by}'

        drivers = drivers.order_by(sort_by)
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([permissions.IsAuthenticated])
class DriverCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Driver created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def edit_driver(request, pk):
    try:
        driver = Driver.objects.get(pk=pk)
    except Driver.DoesNotExist:
        return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = DriverSerializer(driver, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Driver updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_driver(request, pk):
    try:
        driver = Driver.objects.get(pk=pk)
        driver.delete()
        return Response({"message": "Driver deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    except Driver.DoesNotExist:
        return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class RoundListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Retrieve search term and filtering parameters from the request
        search_term = request.GET.get('search', '')
        sort_by = request.GET.get('sort_by', 'round_id')
        order = request.GET.get('order', 'asc')

        # Log the search term if provided
        if search_term:
            SearchLog.objects.create(term=search_term)

        # Initial queryset to retrieve all rounds
        rounds = Round.objects.all()

        # ----------- Search Functionality -----------
        if search_term:
            try:
                # Check if the search term is an integer and filter by round_id
                search_int = int(search_term)
                rounds = rounds.filter(round_id=search_int)
            except ValueError:
                # If not an integer, continue searching by string fields
                rounds = rounds.filter(
                    Q(round_name__icontains=search_term) |
                    Q(round_date__icontains=search_term) |
                    Q(round_base_weight__icontains=search_term) |
                    Q(round_max_weight__icontains=search_term) |
                    Q(round_changes__icontains=search_term) |
                    Q(round_pit_lane__icontains=search_term) |
                    Q(champion_id__icontains=search_term) |
                    Q(track_id__icontains=search_term) |
                    Q(race_status__icontains=search_term) |
                    Q(durition_min__icontains=search_term)
                )

        # ----------- Filtering (Ordering) Functionality -----------
        if order == 'desc':
            sort_by = f'-{sort_by}'

        # Apply sorting by different field types
        valid_sort_fields = [
            'round_id', 'round_name', 'round_date', 'round_base_weight',
            'round_max_weight', 'round_changes', 'round_pit_lane',
            'champion_id', 'track_id', 'race_status', 'durition_min'
        ]

        if sort_by.lstrip('-') in valid_sort_fields:
            rounds = rounds.order_by(sort_by)
        else:
            rounds = rounds.order_by('round_id')  # Default to sorting by 'round_id'

        # Serialize the data and return as a JSON response
        serializer = RoundSerializer(rounds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@method_decorator(csrf_exempt, name='dispatch')
class RoundCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = RoundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Round created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def edit_round(request, pk):
    try:
        round = Round.objects.get(pk=pk)
    except Round.DoesNotExist:
        return Response({"error": "Round not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = RoundSerializer(round, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Round updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_round(request, pk):
    try:
        round = Round.objects.get(pk=pk)
        round.delete()
        return Response({"message": "Round deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    except Round.DoesNotExist:
        return Response({"error": "Round not found"}, status=status.HTTP_404_NOT_FOUND)
#>>>>>>> Stashed changes
