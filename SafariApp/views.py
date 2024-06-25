#
from django.shortcuts import render, redirect
from django.http import HttpResponse # Réponse http pour tester
from .models import Safari_Post
from .forms import PosteModelForm

# Create your views here.

# def index(request):                      # Premier test !
#     return HttpResponse('<h1 style="color:blue">Index Page</h1>')

# def about(request):                      # Deuxième test !
#     return HttpResponse('<h1 style="color:green">About page</h1>')



def index(request):
    poste = Safari_Post.objects.all() # Tout les postes
    if request.method == 'POST':
        form = PosteModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PosteModelForm()
    #form = PosteModelForm() # Accés aux différents formes
    return render(request,'SafariApp/index.html', {'poste': poste, 'form':form})

def post_detail(request, pk):
    post = Safari_Post.objects.get(id=pk)
    context={
        'post': post,
    }
    return render(request, 'SafariApp/post_detail.html', context)