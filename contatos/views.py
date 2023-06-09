from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat

# Create your views here.

def index(request):
    contatos = Contato.objects.order_by('-id').filter( #filtra só os que estão com o mostrar true
        mostrar=True
    )
    paginator = Paginator(contatos, 3)
    
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos':contatos
    })

def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id) #get_objetct previne q mostre o erro caso o id não exista

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato':contato
    })
   
def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        raise Http404()
    
    campos = Concat('name', Value(' '), 'last_name')

    contatos = Contato.objects.annotate(
        nome_completo = campos

    ).filter(
        Q(nome_completo__icontains = termo) | Q(phone__icontains=termo)
    )
    # order_by('-id').filter( #filtra só os que estão com o mostrar true
    #     Q(name__icontains = termo) | Q(last_name__icontains = termo),
    #     mostrar=True
    # )

    paginator = Paginator(contatos, 3)
    
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos':contatos
    })

