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

# Registration GET and POST Views
class RegisterGetView(APIView):
    def get(self, request):
        # Retrieve all users and display only usernames
        users = User.objects.all().values('username', 'password')
        return Response({"users": list(users)}, status=status.HTTP_200_OK)

    
@method_decorator(csrf_exempt, name='dispatch')
class RegisterPostView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "User already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Create new user and manually set password
        user = User.objects.create(username=username)
        user.set_password(password)  # This hashes the password before saving
        user.save()  # Save the user to the database

        # Verify that the password was hashed and stored correctly
        if user.check_password(password):
            print("Password is correct and has been hashed properly!")
        else:
            print("Password verification failed!")

        return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
            
# Login POST View
# Disable CSRF protection for Login view only
class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to log in

    def post(self, request):
        # Get username and password from request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Validate input
        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        # Log the user in (this is useful if you're using session authentication)
        login(request, user)

        # Create a JWT token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # Return the JWT token
        return Response({
            'message': 'Login successful!',
            'token': access_token  # Return the token to the client
        }, status=status.HTTP_200_OK)
            
# Driver GET and POST Views
@method_decorator(csrf_exempt, name='dispatch')
class DriverListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        search_term = request.GET.get('search', '')
        sort_by = request.GET.get('sort_by', 'id')
        order = request.GET.get('order', 'asc')

        # Log search term if provided
        if search_term:
            SearchLog.objects.create(term=search_term)

        # Filter and sort drivers
        drivers = Driver.objects.all()

        # Apply search filters (for name_en, name_th, nickname, qr_code, and age)
        if search_term:
            drivers = drivers.filter(
                Q(name_en__icontains=search_term) |
                Q(name_th__icontains=search_term) |
                Q(nickname__icontains=search_term) |
                Q(qr_code__icontains=search_term) |  # If qr_code is stored as a string or number
                Q(age__icontains=search_term)  # If age is numeric but you want to search by it
            )

        if order == 'desc':
            sort_by = f'-{sort_by}'  # If 'desc', sort in descending order

        # Apply sorting by 'id', 'dob', or 'name_th'
        if sort_by == 'id':
            drivers = drivers.order_by(sort_by)  # Sort by 'id'
        elif sort_by == 'dob':
            drivers = drivers.order_by(sort_by)  # Sort by 'dob' (date of birth)
        elif sort_by == 'name_th':
            drivers = drivers.order_by(sort_by)  # Sort by 'name_th' (Thai name)
        else:
            drivers = drivers.order_by(sort_by)  # Default sorting by other fields (name, nickname, etc.)

        # Serialize the data and return in JSON format
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DriverCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Driver created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
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

user = User.objects.get(username="newuser365")

# Check if entered password matches the hashed password
if user.check_password('password135'):
    print("Password is correct")
else:
    print("Password is incorrect")
