from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
def mainpage(request): 
    return render(request, 'mainpage.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def driver(request):
    return render(request, 'driveritem.html')

def welcome(request):
    return render(request, 'welcome.html')



class EK_Champ_RegisterationView(APIView):
    serializer_project= EKPJSerializer
    def get(self,request):
        info  = EKPJ.objects.all().values()
        return Response({"Your Account Info": info})

    def post(self,request):
        serializer_post_project=EKPJSerializer(data=request.data)
        if(serializer_post_project.is_valid()):
            EKPJ.objects.create(
                            username=serializer_post_project.data.get("username"),
                            password=serializer_post_project.data.get("password"),
                            )

        project = EKPJ.objects.all().filter(username=request.data["username"]).values()
        return Response({"Notification": "Your information is Added!", "Project": project})

class EK_Champ_LoginView(APIView):
    serializer_project= EKPJSerializerLogin
    def get(self,request):
        info  = EKPJLogin.objects.all().values()
        return Response({"Your Account Info": info})

    def post(self,request):
        serializer_post_project=EKPJSerializerLogin(data=request.data)
        if(serializer_post_project.is_valid()):
            EKPJ.objects.create(
                            username=serializer_post_project.data.get("username"),
                            password=serializer_post_project.data.get("password"),
                            )

        project = EKPJ.objects.all().filter(username=request.data["username"]).values()
        return Response({"Notification": "Your Login is Successful!", "Project": project})