from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
<<<<<<< Updated upstream
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from .models import Driver
from .serializers import DriverSerializer
=======
from .models import Driver, SearchLog, Round
from .serializers import DriverSerializer, RoundSerializer
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.tokens import RefreshToken
>>>>>>> Stashed changes


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

<<<<<<< Updated upstream
    def post(self, request):
        serializer_post_project = EKPJSerializerLogin(data=request.data)
        if serializer_post_project.is_valid():
            EKPJ.objects.create(
                username=serializer_post_project.data.get("username"),
                password=serializer_post_project.data.get("password"),
            )
=======
        # Log search term if provided
        if search_term:
            SearchLog.objects.create(term=search_term)

        # Filter and sort drivers
        drivers = Driver.objects.all()

        # Apply search filters (for name_en, name_th, nickname, qr_code, and age)
        if search_term:
            try:
                # Check if the search term is an integer and filter by round_id
                search_int = int(search_term)
                drivers = drivers.filter(id=search_int)
            except ValueError:
                rounds = rounds.filter(
                    Q(name_en__icontains=search_term) |
                    Q(name_th__icontains=search_term) |
                    Q(nickname__icontains=search_term) |
                    Q(qr_code__icontains=search_term) |  # If qr_code is stored as a string or number
                    Q(age__icontains=search_term)  # If age is numeric but you want to search by it
                )
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
    
@api_view(['PUT'])
=======

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
>>>>>>> Stashed changes
def edit_driver(request, pk):
    try:
        driver = Driver.objects.get(pk=pk)
    except Driver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

<<<<<<< Updated upstream
    if request.method == 'PUT':
        serializer = DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
=======
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

user = User.objects.get(username="newuser365")

# Check if entered password matches the hashed password
if user.check_password('password135'):
    print("Password is correct")
else:
    print("Password is incorrect")


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
>>>>>>> Stashed changes
