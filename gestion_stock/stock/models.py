from django.db import models

# Create your models here.

class categorie(models.Model):
    designation = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    isarchived = models.BooleanField(default="False")

    def __str__(self):
        return f"{self.designation} {self.description}"

class article(models.Model):
    reference = models.CharField(max_length=100)
    designation =models.CharField(max_length=100)
    description =models.TextField(max_length=300)
    prixAchat = models.FloatField(default=0.0)
    prixVente = models.FloatField(default=0.0)
    stockmin = models.IntegerField(default=0)
    stockmax = models.IntegerField(default=0)
    categorie = models.ForeignKey(categorie,on_delete=models.PROTECT, related_name="articles")

    def __str__(self):
        return f"{self.designation}"

class stock(models.Model):
    quantite =models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    mouvement = models.CharField(max_length=100)
    article = models.ForeignKey(article, on_delete=models.CASCADE)

