from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . import models
from django.db.models import Sum

# Create your views here.
def index(request):
    categories = models.categorie.objects.filter(isarchived="False").order_by('designation')
    return render(request, 'stock/categorie/index.html', {"categorie":categories})

def add_categorie(request):
    categories = models.categorie.objects.all().order_by('designation')[:4]
    return render(request, 'stock/categorie/add_categorie.html',{"categorie":categories})

def add_categorie_data(request):
    if request.method == "POST":
        design=request.POST['designation']
        desc= request.POST['description']
        categorie = models.categorie(
            designation =design,
            description = desc
        )
        categorie.save()

        return  redirect("index")

def categories(request , id):
    Categories = get_object_or_404(models.categorie, id=id)
    articles = models.article.objects.filter(categorie=id).order_by('designation')[:6]
    context ={
        "categorie":Categories,
        "article":articles
    }
    return render(request, 'stock/categorie/categorie.html', context)

def modification_categorie(request, id):
    categories = get_object_or_404(models.categorie, id=id)
    return render(request, 'stock/categorie/modification_categorie.html', {"categorie":categories})

def modification_categorie_data(request, id):
    if request.method == "POST":
        design=request.POST['designation']
        desc= request.POST['description']
        cat=models.categorie.objects.get(id=id)
        cat.designation=design
        cat.description=desc
        cat.save()
        return  redirect("index")


def supression_categorie(request, id):
        categorie = models.categorie.objects.get(id=id)
        liste_article = categorie.articles.all()
        if liste_article:
            categorie.isarchived=True
            categorie.save()
        else:
            categorie.delete()

        return redirect("index")

def archive(request):
    categories = models.categorie.objects.filter(isarchived="True").order_by('designation')
    return render(request, 'stock/categorie/archive.html', {"categorie": categories})

def delete_categorie_confirm(request, id):
    categorie = models.categorie.objects.get(id=id)
    context= {
        "categorie":categorie
    }
    return render(request, 'stock/categorie/delete_confirm.html', context)


def restore_categorie(request, id):
        categorie = models.categorie.objects.get(id=id)
        liste_article = categorie.articles.all()
        if liste_article:
            categorie.isarchived = False
            categorie.save()
        else:
            categorie.delete()

        return redirect("index")


#-----------------------------------------------------------------------------
#   LES CODES POUR LES ARTRICLES
#------------------------------------------------------------------------------

def liste_articles(request):
    articles = models.article.objects.all().order_by('categorie')
    return render(request, 'stock/article/liste_article.html',{"article":articles})

def add_article(request):
    categories = models.categorie.objects.all()
    context ={"categorie":categories}
    return render(request, 'stock/article/add_article.html',context)

def add_article_data(request):
    if request.method == "POST":
        ref=request.POST['reference']
        design= request.POST['designation']
        desc = request.POST['description']
        prixAchat= request.POST['prixAchat']
        prixVente= request.POST['prixVente']
        stockmin= request.POST['stockmin']
        stockmax= request.POST['stockmax']
        categorie= request.POST['categorie']
        print(request.POST)

        Article = models.article(
            reference=ref,
            designation=design,
            description=desc,
            prixVente=prixVente,
            prixAchat=prixAchat,
            stockmin=stockmin,
            stockmax=stockmax,
            categorie=models.categorie.objects.get(pk=categorie)
        )

        Article.save()

        return  redirect("liste_article")

def detail_articles(request , id):
    article = get_object_or_404(models.article, id=id)
    articles = models.article.objects.all()[:6]
    context ={
        "articles":articles,
        "article":article
    }
    return render(request, 'stock/article/detail_article.html', context)

def modification_article(request, id):
    articles = get_object_or_404(models.article, id=id)
    return render(request, 'stock/article/modification_article.html', {"article":articles})

def supression_article(request, id):
    article = models.article.objects.get(id=id)
    article.delete()

    return redirect("liste_article")


#------------------------------------------------------------------------------

def liste_stock(request):
    stock = models.stock.objects.values('article__designation').annotate(quantite=Sum('quantite'))
    context={
        "stock":stock
    }
    return  render(request,'stock/stock/liste_stock.html', context)

def add_stock(request):
    articles = models.article.objects.all()
    return render(request, 'stock/stock/add_stock.html', {"article":articles})

def add_stock_data(request):
    if request.method == 'POST':
        art = request.POST['article']
        mouve = request.POST['mouvement']
        quant = request.POST['quantite']
        stock = models.stock(
            article = models.article.objects.get(pk=art),
            mouvement = mouve,
            quantite= quant
        ).save()

    return  redirect('liste_stock')

def historique(request):
    stocks = models.stock.objects.all()
    context = {"stock": stocks}
    return render(request, 'stock/stock/historique.html', context)