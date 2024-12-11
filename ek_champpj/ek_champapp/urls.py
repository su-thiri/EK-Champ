from django.urls import path
from ek_champapp import views

urlpatterns = [
    path('base_round/', views.base_round, name='base_round'),
    path('createround/', views.create_round, name='create_round'),
    path('store_round/', views.store_round, name='createdata_round'),
    path('edit_round/<int:pk>/', views.edit_round, name='edit_round'),
    path('editdata_round/<int:pk>/', views.editdata_round, name='editdata_round'),
    
    path('base_teamno/', views.base_teamno, name='base_teamnumber'),
    path('create_teamno/', views.create_teamno, name='create_teamnumber'),
    path('store_teamno/', views.store_teamno, name='createdata_teamnumber'),
    path('edit_teamno/<int:pk>/', views.edit_teamno, name='edit_teamnumber'),
    path('editdata_teamno/<int:pk>/', views.editdata_teamno, name='editdata_teamnumber'),
    
    path('base_tinround/', views.base_tinround, name='base_team_in_round'),
    path('create_tinround/', views.create_tinround, name='create_team_in_round'),
    path('store_tinround/', views.store_tinround, name='createdata_team_in_round'),
    path('edit_tinround/<int:pk>/', views.edit_tinround, name='edit_team_in_round'),
    path('editdata_tinround/<int:pk>/', views.editdata_tinround, name='editdata_team_in_round'),
]
