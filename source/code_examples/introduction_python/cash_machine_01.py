utilisateur = "Franck"

catalogue = {
    "pomme" : 0.95,
    "orange" : 0.80,
    "banane" : 1.20,
}

panier = {
    "pomme": 3,
    "banane":5,
}

sous_total = 0

for item in panier.items():
    produit, quantite =  item
    prix = catalogue[produit]
    sous_total += prix * quantite

total = sous_total

print(total)
