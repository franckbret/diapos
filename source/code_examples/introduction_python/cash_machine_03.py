#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time

class Article:
    """
    Represente un article avec :
    - un prix
    - une description
    """

    def __init__(self, nom, prix = 0.0):
        self.nom = nom
        self.prix = prix

class Catalogue:
    """
    Represente une liste de produits à la vente
    """

    def __init__(self, liste = {}):
        self.liste = liste

    def ajouter(self, nom, prix):
        article = {nom: prix}
        self.liste.update(article)

    def enlever(self, nom):
        self.liste.pop(nom, None)

class Panier:
    """
    Represente le panier d'articles
    """

    def __init__(self, panier = {}):
        self.panier = panier

    def ajouter(self, nom, quantite):
        article = {nom: quantite}
        self.panier.update(article)

    def enlever(self, nom):
        self.panier.pop(nom)

class Ticket:
    """
    Gere des tickets de caisse
    """
    def __init__(self, catalogue, panier):
        self.catalogue = catalogue
        self.panier = panier
        self.total = 0.00

    def get_total(self):

        for item in self.panier.panier.items():
            produit, quantite =  item
            prix = self.catalogue.liste[produit]
            self.total += prix * quantite

        return format(self.total, '.2f')

    def imprime(self):
        """
        Imprime un ticket de caisse
        """
        separateur_1 = "-"*32
        separateur_2 = "#"*32
        date = time.strftime("%c")
        liste = []
        total = self.get_total()

        for item in self.panier.panier.items():

            produit, quantite =  item
            prix = self.catalogue.liste[produit]
            sous_total = prix * quantite
            liste.append(
                u"{produit} - {prix} € | {quantite} | {sous_total} €\n".format(**locals())
            )

        message_liste = u"".join(liste)
        print(u"""
{separateur_1}
Cash machines bonjour
{separateur_1}
{date}
{separateur_2}
{message_liste}
{separateur_1}
TOTAL: {total} €
{separateur_1}
Merci de votre visite
{separateur_2}
              """.format(**locals())
             )

if __name__ == '__main__':

    catalogue_dict = {
        "pomme" : 0.95,
        "orange" : 0.80,
        "banane" : 1.20,
        "kiwi" : 1.79,
    }

    # creation de l'objet catalogue
    catalogue = Catalogue(catalogue_dict)

    # mise à jour du catalogue avec un nouveau produit
    catalogue.ajouter("poire", 1.15)

    # on ajoute au catalogue un autre produit par erreur
    catalogue.ajouter("chien", 600)

    # et on le supprime
    catalogue.enlever("chien")

    # creation de l'objet panier
    mon_panier = Panier()
    mon_panier.ajouter("pomme", 3)
    mon_panier.ajouter("poire", 5)
    mon_panier.ajouter("kiwi", 1)

    # création de l'objet ticket
    ticket = Ticket(catalogue, mon_panier)

    # imprime le resultat
    ticket.imprime()

