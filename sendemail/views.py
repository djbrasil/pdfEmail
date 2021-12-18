from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.base import TemplateView 
from sendemail.forms import SendEmailForm
from sendemail.models import Sendemail 
 
class IndexView(TemplateView):
    template_name = 'send_email/index.html' 

class NewView(CreateView):
	template_name = 'send_email/form.html'
	form_class = SendEmailForm
	success_url = reverse_lazy('table')
	success_message = 'Email Cadastrado com sucesso'

class DeleteView(DeleteView):
	model = Sendemail
	template_name = 'send_email/delete.html'
	success_url = reverse_lazy('table')
	success_message = 'O equipamento foi deletado com sucesso'

class UpdateView(UpdateView):
	model = Sendemail 
	form_class = SendEmailForm
	template_name = 'send_email/alterar.html'
	success_url = reverse_lazy('table')
	success_message = 'As alterações foram efectuadas com sucesso'

class ListView(ListView):
	model = Sendemail
	template_name = 'send_email/table.html' 
 