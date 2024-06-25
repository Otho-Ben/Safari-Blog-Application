from django.db import models
from django.contrib.auth.models import User # Pour les utilisateurs
# Create your models here.
class Safari_Post(models.Model):    #py manage.py makemigrations, django s'occupe de tout, même la création de l'id implicitement
    titre = models.CharField(max_length=50)
    main = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Relation avec l'utilisateur d'où l'appelle de ForeignKey
    date= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',) # Le poste le plus récent devient le premier dans la liste des postes

    def __str__(self):
        return self.titre