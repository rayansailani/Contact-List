from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="homepage"),
    path('list/',views.listContactsView, name='listContacts'),
    path('add_contacts/', views.ContactsAddView.as_view(), name='add'),
    path('delete_contacts/<str:pk>/', views.delete_contacts, name='delete_contact'),
    path('update_contacts/<str:pk>/', views.update_contacts, name="update_contacts"),

]
