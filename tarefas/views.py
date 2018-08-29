from django.shortcuts import render
from django.http import HttpResponse

from .forms import CategoriaForm, TarefaForm

# Create your views here.

def nova_categoria(request):
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Categoria adicionada ~.^')
		else:
			print(form.erros)
	else:
		form = CategoriaForm()
	return render(request, 'tarefas/nova_categoria.html', {'form': form})

def nova_tarefa(request):
	if request.method == 'POST':
		form = TarefaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Tarefa Adicionada')
		else:
			print(form.erros)
	else:
		form = TarefaForm()
	return render(request, 'tarefas/nova_tarefa.html', {'form': form})




