from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="homepage"),
    path('list/',views.listContactsView, name='listContacts'),
    path('add_contacts/', views.ContactsAddView.as_view(), name='add'),
]
