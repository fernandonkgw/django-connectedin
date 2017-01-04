# -*- coding: UTF-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from perfis.models import Perfil
from perfis.models import Convite

#@login_required
#@require_http_methods(['GET'])
def index(request):
	print request.user.username
	print request.user.email
	print request.user.has_perm('perfis.add_convite')
	return render(request, 'index.html', {'perfis':Perfil.objects.all(), 'perfil_logado':get_usuario_logado(request) } )

@login_required
def exibir(request, perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_usuario_logado(request)
	ja_eh_contato = perfil in perfil_logado.contatos.all()
	return render(request, 'perfil.html', {'perfil':perfil, 'ja_eh_contato':ja_eh_contato})

@permission_required('perfis.add_convite', raise_exception=False)
@login_required
def convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_usuario_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	# realizando redirecionamento
	return redirect('index')

@login_required
def get_usuario_logado(request):
	perfil_logado = request.user.perfil
	print perfil_logado.id
	for contato in perfil_logado.contatos.all:
		
	return perfil_logado

@login_required
def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')
    