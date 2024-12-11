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

<<<<<<< Updated upstream
    path('api/drivers/list/', views.DriverListView.as_view(), name='driver-list'),  # URL for GET (list drivers)
    path('api/drivers/create/', views.DriverCreateView.as_view(), name='driver-create'),  # URL for POST (create driver)
    # For editing a driver
    path('api/drivers/edit/<int:driver_id>/', views.edit_driver, name='edit_driver'),
=======
    # Registration
    path('api/register/get/', views.RegisterGetView.as_view(), name='register-get'),
    path('api/register/post/', views.RegisterPostView.as_view(), name='register-post'),

    # Login
    path('api/login/', views.LoginView.as_view(), name='login'),

    # Driver Endpoints
    path('api/drivers/list/', views.DriverListView.as_view(), name='driver-list'),
    path('api/drivers/create/', views.DriverCreateView.as_view(), name='driver-create'),
    path('api/drivers/edit/?key=value/', views.edit_driver, name='edit-driver'),
    path('api/drivers/delete/?key=value/', views.delete_driver, name='delete-driver'),
    path('api/drivers/list/?sort_by=name_en&order=asc', views.DriverListView.as_view(), name ='filter_by_name_en'),
    path('api/drivers/list/?sort_by=name_th&order=asc', views.DriverListView.as_view(),name ='filter_by_name_th'),
    path('api/drivers/list/?sort_by=dob&order=asc', views.DriverListView.as_view(),name ='filter_by_bod'),
    path('api/drivers/list/?sort_by=id&order=asc', views.DriverListView.as_view(),name ='filter_by_id'),
    path('api/drivers/list/?sort_by=age&order=desc', views.DriverListView.as_view(),name ='filter_by_age'),
    path('api/drivers/list/?sort_by=name_th&order=asc', views.DriverListView.as_view(),name ='filter_by_qr_code'),
    path('api/drivers/list/?sort_by=nickname&order=asc', views.DriverListView.as_view(),name ='filter_by_qr_code'),
    path('api/drivers/list/?search=value', views.DriverListView.as_view(),name ='search'),
    # List and filter rounds
    path('api/rounds/list/', views.RoundListView.as_view(), name='round-list'),
    
    # Create a new round
    path('api/rounds/create/', views.RoundCreateView.as_view(), name='round-create'),
    
    # Edit an existing round by ID
    path('api/rounds/edit/<int:pk>/', views.edit_round, name='edit-round-by-round-id'),
    
    # Delete an existing round by ID
    path('api/rounds/delete/<int:pk>/', views.delete_round, name='delete-round-by-round-id'),
    path('api/rounds/list/?search=value', views.delete_round, name='search-round'),
    path('api/rounds/list/?sort_by=<field>&order=<order>', views.RoundListView.as_view(), name='filter-by-round-column-in-order-asc-or-desc'),
>>>>>>> Stashed changes
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)