from django.contrib import admin
from .models import Safari_Post

# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_display = ('titre','date')
admin.site.register(Safari_Post, AdminPost) # L'historique des postes
