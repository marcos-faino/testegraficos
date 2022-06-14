import base64
from io import BytesIO

from django.views.generic import ListView
from .models import *
from matplotlib import pyplot as plt


class LivrosView(ListView):
    template_name = 'listlivros.html'
    model = Livro

    def _criar_grafico(self):
        generos = Genero.objects.all()
        gnlabels = []
        gnquant = []
        for g in generos:
            if (Livro.objects.filter(idgenero=g.idgenero)).count() > 0:
                gnlabels.append(g.descricao)
                gnquant.append((Livro.objects.filter(idgenero=g.idgenero)).count())
        plt.pie(gnquant, labels=gnlabels)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()
        return graph

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        generos = Genero.objects.order_by('descricao').all()
        tabela = []
        for g in generos:
            tabela.append({'desc':g.descricao,
                           'quant':(Livro.objects.filter(idgenero=g.idgenero)).count()
                           })
        contexto['tabela'] = tabela
        grafico = self._criar_grafico()
        contexto['grafico'] = grafico
        return contexto

