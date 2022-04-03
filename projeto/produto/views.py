from django.shortcuts import render
from .models import Produto

def produto_list(request):
    template_list = 'produto_list.html'
    objects = Produto.objects.all()
    context = {'object_list': objects}
    return render(request, template_list, context)
