from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from django.core.mail import send_mail
from django.template.loader import render_to_string   
from django.conf import settings 
# #####
from django.core.mail import EmailMultiAlternatives 
from django.core.mail import send_mail    
from django.template.loader import render_to_string
from django.http import HttpResponse 
from weasyprint import HTML     
import weasyprint

# Create your models here
CHOICES_SEXO=[('1','Feminino'),('2','Masculino')]

class Sendemail(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=100) 
    sexo = models.CharField('sexo', max_length=1, choices=CHOICES_SEXO)

   
@receiver(post_save, sender=Sendemail)
def post_save_handler(sender, **kwargs):
    sendemail = kwargs.get('instance', None)
    created = kwargs.get('created', False)
    raw = kwargs.get('raw', False)
 
    # Configuração do body do email
    email_template = """
    Usuario: {nome} Email: {email}
    Geramos um pdf.
    """ 
    
    # converter html para pdf
    html_string = render_to_string('send_email/html_template_email.html',{'user': email_context})
    html_template = html_string.replace('{', '{{').replace('}', '}}').replace('{{$', '{').replace('$}}', '}')
    
    email_context = {'nome': sendemail.nome, 
                    'email': sendemail.email, 
                    'sexo': sendemail.sexo}

    response = HttpResponse(content_type='application/pdf')
    pdf = html_template.format(**email_context)
    
    # html para pdf
    response['Content-Disposition'] = 'filename=certificate_{}'.format(email_context['nome']) + '.pdf'
    pdf = weasyprint.HTML(string=pdf, base_url='http://127.0.0.1:8000/media').write_pdf(stylesheets=[weasyprint.CSS(string='body { font-family: serif}')]) 
 
    template_body = email_template.format(**email_context) 

    to_emails = [str(email_context['email'])]
    subject = "test pdf"

    email = EmailMultiAlternatives(subject, body=template_body, from_email=settings.EMAIL_HOST_USER, to=to_emails )
    email.attach("emailpdf_{}".format(email_context['nome']) + '.pdf', pdf, "application/pdf")
    email.content_subtype = "pdf"  
    email.decode = 'us-ascii' 
    email.send()  