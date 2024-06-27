from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('new_client/', views.new_client, name='new_client'),
  path('edit_client/<client_id>/', views.edit_client, name='edit_client'),
  path('remove_client/<int:pk>/', views.RemoveClient.as_view(), name='remove_client'),
  path('email/<client_id>/', views.send_email, name='send_email'),
]