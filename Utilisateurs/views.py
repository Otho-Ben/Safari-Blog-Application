# Views est la logique du projet !
from .forms import InscriptionForm, UtilisateurUpdate, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # par défaut django nous donne la possibilité de créer
                                                       # des utilisateurs à travers des forums !
from django.contrib.auth import logout
# Create your views here.
def inscription(request):
    
    if request.method == 'POST':
        form=InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('utilisateur-connexion') # Redirection vers page d'acceuil aprés inscription valide !
    else:
        form=InscriptionForm()
    #form = InscriptionForm() pour le test
    context = {
        'form': form,
    }
    return render(request, 'Utilisateurs/inscription.html',context)


def deconnexion_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('utilisateur-connexion')
    else:
        return redirect('blog-index')
    
def profile(request):
    if request.method == 'POST':
        u_form = UtilisateurUpdate(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save() # Sauvgarder les modifications
            return redirect('utilisateur-profile') # Rédirection vers la page du profile
    else:
        u_form = UserCreationForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'Utilisateurs/profile.html')