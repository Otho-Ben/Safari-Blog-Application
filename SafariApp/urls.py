
from django.urls import path #../SafariProject/urls.py
from . import views #views.py

# urlpatterns = [                                      # Tester le bon fonctionnement !
#     path('testing/', views.index, name='blog-index'),   # Appelle de la fonction index.
# ]

urlpatterns = [                                      
     path('Menu/', views.index, name='blog-index'),
     path('post_detail/<int:pk>/',views.post_detail, name='blog-post-detail'),
 ]