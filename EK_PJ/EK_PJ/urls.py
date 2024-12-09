from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from EK_APP import views  # Keep only this import

urlpatterns = [
    path('admin/', admin.site.urls),

    # Registration
    path('api/register/get/', views.RegisterGetView.as_view(), name='register-get'),
    path('api/register/post/', views.RegisterPostView.as_view(), name='register-post'),

    # Login
    path('api/login/', views.LoginView.as_view(), name='login'),

    # Driver Endpoints
    path('api/drivers/list/', views.DriverListView.as_view(), name='driver-list'),
    path('api/drivers/create/', views.DriverCreateView.as_view(), name='driver-create'),
    path('api/drivers/edit/?key=value/', views.edit_driver, name='edit-driver'),
    path('api/drivers/delete/?key=value>/', views.delete_driver, name='delete-driver'),
    path('api/drivers/list/?sort_by=name_en&order=asc', views.DriverListView.as_view(), name ='filter_by_name_en'),
    path('api/drivers/list/?sort_by=name_th&order=asc', views.DriverListView.as_view(),name ='filter_by_name_th'),
    path('api/drivers/list/?sort_by=dob&order=asc', views.DriverListView.as_view(),name ='filter_by_bod'),
    path('api/drivers/list/?sort_by=id&order=asc', views.DriverListView.as_view(),name ='filter_by_id'),
    path('api/drivers/list/?sort_by=age&order=desc', views.DriverListView.as_view(),name ='filter_by_age'),
    path('api/drivers/list/?sort_by=name_th&order=asc', views.DriverListView.as_view(),name ='filter_by_qr_code'),
    path('api/drivers/list/?sort_by=nickname&order=asc', views.DriverListView.as_view(),name ='filter_by_qr_code'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
