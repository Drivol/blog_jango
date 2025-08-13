from django.shortcuts import render

def index(request):
    posts = [
        {
            'title': 'Campeonato de Futebol 2025',
            'content': 'O campeonato está chegando com grandes expectativas para os times...',
            'image': 'blog/images/futebol.jpg',
        },
        {
            'title': 'Dicas para melhorar sua corrida',
            'content': 'Melhore sua performance com essas dicas essenciais para corredores.',
            'image': 'blog/images/corrida.jpg',
        },
    ]
    return render(request, 'blog/index.html', {'posts': posts})
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})
