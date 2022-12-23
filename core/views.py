from django.shortcuts import get_object_or_404, render

from .models import Cliente, Curso


def index(request):
    cursos = Curso.objects.count
    clientes = Cliente.objects.count

    context = {
        'titulo': 'Home',
        'subtitulo': 'Estimular Digital',
        'cursos': cursos,
        'clientes': clientes,
    }

    return render(request, 'index.html', context)


def contato(request):
    context = {
        'titulo': 'Contato',
        'subtitulo': 'Como podemos ajudar?',
    }

    return render(request, 'contato.html', context)


def curso(request, id):
    curso_detalhe = get_object_or_404(Curso, id=id)
    # curso_detalhe = Curso.objects.get(id=id)
    context = {
        'titulo': 'Curso',
        'subtitulo': 'Descrição',
        'curso': curso_detalhe,
    }

    return render(request, 'curso.html', context)


def cliente(request, id):
    cliente_detalhe = Cliente.objects.get(id=id)
    context = {
        'titulo': 'Cliente',
        'subtitulo': 'Detalhes do cliente',
        'cliente': cliente_detalhe,
    }

    return render(request, 'cliente.html', context)


def cursos(request):
    produtos = Curso.objects.all()
    context = {
        'titulo': 'Cursos',
        'subtitulo': 'Listando os cursos cadastrados',
        'produtos': produtos,
    }

    return render(request, 'cursos.html', context)


def clientes(request):
    clients = Cliente.objects.all()
    context = {
        'titulo': 'Clientes',
        'subtitulo': 'Listando os clientes cadastrados',
        'clientes': clients,
    }

    return render(request, 'clientes.html', context)


def perfil(request):

    context = {
        'titulo': 'Perfil',
        'subtitulo': 'Listando detalhes do usuário',

    }

    return render(request, 'perfil.html', context)


def calendario(request):

    context = {
        'titulo': 'Calendário',
        'subtitulo': 'Eventos do calendário',

    }

    return render(request, 'calendario.html', context)


def error404(request, exception):
    return render(request, 'error404.html')


def error500(request):
    return render(request, 'error500.html')
