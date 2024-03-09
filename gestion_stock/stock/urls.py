from django.urls import path
from . import views

urlpatterns= [
    path('index/', views.index, name='index' ),
    path('add_categorie/',views.add_categorie, name='add_categorie'),
    path('add_categorie_data/',views.add_categorie_data,name="add_categorie_data"),
    path('categorie/<int:id>/', views.categories,name='categorie'),
    path('modification_categorie/<int:id>/', views.modification_categorie, name='modification_categorie'),
    path('modification_categorie_data/<int:id>/',views.modification_categorie_data, name="modification_categorie_data"),
    path('supression_categorie/<int:id>/' ,views.supression_categorie,name='supression_categorie'),
    path('archive/', views.archive,name="archive"),
    path('delete_categorie_confirm/<int:id>/', views.delete_categorie_confirm, name='delete_categorie_confirm'),
    path('restore_categorie/<int:id>/', views.restore_categorie, name='restore_categorie'),



    path('liste_article/', views.liste_articles, name="liste_article"),
    path('add_article/',views.add_article, name='add_article'),
    path('add_article_data/', views.add_article_data, name="add_article_data"),
    path('detail_articles/<int:id>/', views.detail_articles, name='detail_articles'),
    path('modification_article/<int:id>/', views.modification_article, name='modification_article'),
    path('supression_article/<int:id>/' ,views.supression_article,name='supression_article'),


    path('liste_stock/', views.liste_stock, name="liste_stock"),
    path('add_stock/', views.add_stock,name="add_stock"),
    path('add_stock_data/',views.add_stock_data, name="add_stock_data"),
    path('historique/', views.historique, name="historique")

]