from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_contacts, name='contacts'),
    path('add/', views.add_contacts, name='add-contact'),
    path('edit/<int:people_id>/', views.edit_contacts, name='edit-contact'),
    path('delete/<int:people_id>/', views.delete_contacts, name='delete-contact'),
]
