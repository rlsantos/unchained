from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['ricardo.santos@vacaria.ifrs.edu.br']
            if cc_myself:
                recipients.append(sender)

            #TODO: Configurar no arquivo settings.py as credenciais parar envio de e-mails
            #send_mail(subject, message, sender, recipients)
            context = {
                'form': form,
            }
            return render(request, 'unchained/thanks.html', context)

    else:
        form = ContactForm()
        context = {
            'form': form,
        }

    return render(request, 'unchained/contact.html', {'form': form})


def index(request):
    context = {"user": "Aluno"}
    return render(request, 'base.html', context)
