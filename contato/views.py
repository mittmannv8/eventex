from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext


from models import Contato
from forms import ContatoForm

def add_contato(request):
    form = ContatoForm()
    context = RequestContext(request,{'form':form})
    return render_to_response('contato/add.html', context)


def save_contato(request):
    form = ContatoForm(request.POST)

    if not form.is_valid:
        context = RequestContext(request,{'form':form})
        return render_to_response('contato/add.html', context)
    
    contato = form.save()

    return HttpResponseRedirect(
        reverse('contato:sucesso', args=[contato.pk])
    )

def sucesso(request,pk):
    contato = get_object_or_404(Contato,pk=pk)
    context = RequestContext(request,{'contato':contato})
    return render_to_response('contato/sucesso.html',context)

