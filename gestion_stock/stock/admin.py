from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.article)
admin.site.register(models.stock)
admin.site.register(models.categorie)

