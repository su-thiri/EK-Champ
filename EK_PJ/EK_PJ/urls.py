"""
URL configuration for EK_PJ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from EK_APP import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('EK_Champ_Register/', views.EK_Champ_RegisterationView.as_view()),
    path('EK_Champ_Login/', views.EK_Champ_LoginView.as_view()),
    path('drivers/overview/', views.Driver_Overview.as_view()),
    path('drivers/create/', views.Driver_Create.as_view()),
    path('drivers/edit/<int:pk>/', views.Driver_Edit.as_view()),
    path('drivers/overview/?search=name_of_driver', views.Driver_Edit.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)