from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from contacts.models import *
from django.views.generic import UpdateView, CreateView, ListView
from accounts.models import Account
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from contacts.forms import ContactUpdateForm
import csv

@csrf_exempt
def homeView(request):
	if request.method == 'POST':
		user = request.POST.get('user')
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="Contact.csv"'
		writer = csv.writer(response)
		writer.writerow(['Name', 'Phone Number', 'Description'])
		instance = Contact.objects.all()
		for contact in instance:
			if str(contact.user_name) == str(user):
				writer.writerow([contact.name, contact.contact_number, contact.description])
		return response
	return render(request, 'contacts/home.html')

@login_required
def delete_contacts(request, pk):
		queryset = Contact.objects.filter(id = pk)
		if request.method == 'POST':
			queryset.delete()
			return redirect('listContacts')
		return render(request, 'contacts/delete.html')


@login_required
def listContactsView(request):
    details = Contact.objects.all()
    return render(request, 'contacts/list_contacts.html', {'details': details})
	
@login_required
def update_contacts(request, pk):
	queryset = Contact.objects.get(id=pk)
	form = ContactUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = ContactUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('listContacts')

	context = {
		'form':form
	}
	return render(request, 'contacts/add_contacts.html', context)

class ContactsAddView(LoginRequiredMixin, CreateView):
	model = Contact
	template_name='contacts/add_contacts.html'
	fields = [ 'name', 'contact_number','description']
	success_url='listContacts'

	def form_valid(self, form):
		form.instance.user_name = self.request.user
		return super().form_valid(form)
