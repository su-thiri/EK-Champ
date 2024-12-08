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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from EK_APP.views import DriverViewSet

router = DefaultRouter()
router.register(r'drivers', DriverViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/get/', views.EK_Champ_GetView.as_view(), name='drivers-get'),
    path('api/register/post/', views.EK_Champ_PostView.as_view(), name='drivers-post'),
    path('EK_Champ_Login/', views.EK_Champ_LoginView.as_view()),

    path('api/drivers/list/', views.DriverListView.as_view(), name='driver-list'),  # URL for GET (list drivers)
    path('api/drivers/create/', views.DriverCreateView.as_view(), name='driver-create'),  # URL for POST (create driver)
    # For editing a driver
    path('api/drivers/edit/<int:driver_id>/', views.edit_driver, name='edit_driver'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)