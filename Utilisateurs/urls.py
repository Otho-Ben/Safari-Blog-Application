from django.urls import path
from . import views
from django.contrib.auth import views as auth_view # pour ne pas confondre avec la ligne : 2

urlpatterns =[
    path('inscription/',views.inscription,name='utilisateur-inscription'),
    path('profile/',views.profile,name='utilisateur-profile'),
    path('', auth_view.LoginView.as_view(template_name='Utilisateurs/connexion.html'),
          name='utilisateur-connexion'),
    path('deconnexion/', auth_view.LoginView.as_view(template_name='Utilisateurs/logout.html'),
          name='utilisateur-deconnexion'),
]