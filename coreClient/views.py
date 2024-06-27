from django.shortcuts import render, redirect, get_object_or_404
from datetime import timedelta, datetime
from .forms import ClientForm
from .models import Client
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


class RemoveClient(DeleteView):
  model = Client
  template_name = 'user/delete_client.html'
  success_url = reverse_lazy('index')

def index(request):
  clients = Client.objects.all()
  context = {'clients': clients}
  return render(request, 'index.html', context)

def new_client(request):
  if request.method != 'POST':
    form = ClientForm()
  else:
    form = ClientForm(data=request.POST)
    if form.is_valid():
      new_client = form.save(commit=False)
      data_servico = request.POST['data_servico'].split('-')
      data_servico = datetime(int(data_servico[0]), int(data_servico[1]), int(data_servico[-1]))
      data_servico_futuro = data_servico + timedelta(days=180)
      new_client.data_servico_futuro = data_servico_futuro.date()
      new_client.save()
      return redirect('index')
    
  context = {'form': form}

  return render(request, 'user/new_client.html', context)

def edit_client(request, client_id):
  client = get_object_or_404(Client, id=client_id)

  if request.method != 'POST':
    form = ClientForm(instance=client)
  else:
    form = ClientForm(instance=client, data=request.POST)
    if form.is_valid():
      new_user = form.save(commit=False)
      data_servico = request.POST['data_servico'].split('-')
      data_servico = datetime(int(data_servico[0]), int(data_servico[1]), int(data_servico[-1]))
      data_servico_futuro = data_servico + timedelta(days=180)
      new_user.data_servico_futuro = data_servico_futuro.date()
      new_user.save()
      return redirect('index')
    
  context = {'form': form, 'client': client}

  return render(request, 'user/edit_client.html', context)

def send_email(request, client_id):
  client = get_object_or_404(Client, id=client_id)
  context = {'nome': client.nome, 'email': client.email,
             'servico': client.servico, 'data_servico': client.data_servico,
             'data_servico_futuro': client.data_servico_futuro}
  html_context = render_to_string('mail/relatorio.html', context)
  text_context = render_to_string('mail/relatorio.txt', context)

  send_mail(
    subject="Email de teste",
    message=text_context,
    from_email='no-reply@treinaweb.com.br',
    recipient_list=[client.email],
    html_message=html_context,
  )

  return HttpResponseRedirect(reverse('index'))
