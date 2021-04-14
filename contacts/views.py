from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from contacts.models import *
from django.views.generic import UpdateView, CreateView, ListView
from accounts.models import Account

# Create your views here.


def homeView(request):
    return render(request, 'contacts/home.html')

def listContactsView(request):
    details = Contact.objects.all()
    return render(request, 'contacts/list_contacts.html', {'details': details})

class ContactsAddView(LoginRequiredMixin, CreateView):
	model = Contact
	template_name='contacts/add_contacts.html'
	fields = [ 'name', 'contact_number','description']
	success_url=''

	def form_valid(self, form):
		form.instance.user_name = self.request.user
		return super().form_valid(form)
