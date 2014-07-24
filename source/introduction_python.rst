:title: Introduction Python
:author: Franck Bret
:description: A la découverte du langage de programmation Python
:keywords: introduction, python 
:css: css/introduction_python.css

----

Introduction à Python
=====================

.. code:: python 

  print("Hello Python!")

.. _Manuel: https://pypi.python.org/pypi/manuel
.. image:: images/python-logo-master-v3-TM.png

*Franck Bret - @franckbret - 2014*

----

C'est quoi ?
============

Python est un langage de programmation : 

* **objet**, 
* **multi-paradigme** 
* **multi-plateformes** 

C'est un langage interprété.

.. image:: images/python-logo-master-v3-TM.png

.. note:: Il est doté d'un typage dynamique fort, d'une gestion automatique de la mémoire par ramasse-miettes et d'un système de gestion d'exceptions.
  L'interpréteur standard, CPython, compile en bytecode le code Python.

----

Un langage attirant ?
=====================

- Lisible et simple à prendre en main
- Interactif (Terminal)
- Documenti(é/able) 
- Standardisé par des recommandations (PEP8)
- Communauté investie à l'image du BDFL

Un eco-système complet et de qualité
-------------------------------------

.. note:: Homogène dans le sens ou les recommandations / guidelines, influencent la qualité des programmes.

----

Pour quels usages ?
===================

Aujourd'hui on retrouve Python un peu partout : 

* Gestion de données
* Interface utilisateur, Jeux
* Simulation, calcul et recherche scientifique
* Applications, sites web, Api
* Logiciels server & desktop
* Réseau et maintenance
* Embarqué

.. note:: Python est par défaut dans tous les GNU/linux, Mac et certains Windows.

----

Qui s'en sert ?
===============

Quelques noms connus:

* Eve On Line, Battlefield, Civilization
* Google, Youtube, Mozilla, Yahoo
* Intel, Cisco, Hewlett-Packard, Seagate, Qualcomm, IBM
* Nasa, Nsa, National Geographic
* Rackspace, Dropbox, BitTorrent
* Instagram, Disqus, Reddit, Eventbrite, Lanyrd, Pinterest, Path, Slideshare  
* Autolib, Libération, 20 Minutes, Century21
* ...

.. note:: Voir les python success story sur le web

----

Un peu de code ?
================

----

Console python 
===============

Dans un terminal on tape python et c'est parti !

** franck  ** python

.. code:: python

  Python 3.3.2+ (default, Feb 28 2014, 00:52:16) 
  [GCC 4.8.1] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>> print("Hello World!")
  Hello World!

Pas de terminal sous la main ? https://www.pythonanywhere.com/try-ipython/


.. _Manuel: https://pypi.python.org/pypi/manuel
.. note:: la console python est interactive 

----

Jouons avec du texte
====================


.. code:: python

  >>> utilisateur = "Franck"
  >>> phrase = "Bonjour à tous !"
  >>> print(utilisateur + " dit : " + phrase)
  Franck dit : Bonjour à tous !

.. _Manuel: https://pypi.python.org/pypi/manuel

----

Jouons avec des nombres
=======================

.. code:: python

  >>> prix_unitaire = 15.95
  >>> quantite = 10
  >>> ristourne_pourcent = 10
  >>> sous_total = prix_unitaire * quantite
  >>> print(sous_total)
  159.5
  >>> total = sous_total - (sous_total * ristourne_pourcent / 100)
  >>> print(total)
  143.55

.. _Manuel: https://pypi.python.org/pypi/manuel

----

Avec les deux
=============

.. code:: python

  >>> separateur = "#" * 80 
  >>> print(separateur)
  ################################################################################
  >>> print(utilisateur + " dit : " + "Cela fera un total de " + str(total) + u" €")
  Franck dit : Cela fera un total de 143.55 €
  >>> print(separateur)
  ################################################################################
  >>> print(u"%s dit : Cela fera un total de %s €" % (utilisateur, total))
  Franck dit : Cela fera un total de 143.55 €
  >>> print(separateur)
  ################################################################################
  >>> print("{} dit : Cela fera un total de {} €".format(utilisateur, total))
  Franck dit : Cela fera un total de 143.55 €

.. _Manuel: https://pypi.python.org/pypi/manuel

----

Quand ça fonctionne pas ça le dit
=================================

.. code:: python
  
  >>> print(utilisateur + total)
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: cannot concatenate 'str' and 'float' objects
  >>> print(utilisateur + str(total))
  Franck143.55

.. _Manuel: https://pypi.python.org/pypi/manuel

----

Les objets ont un type
======================

.. code:: python

  >>> type(utilisateur)
  <type 'str'>
  >>> type(total)
  <type 'float'>
  >>> type(str(total))
  <type 'str'>


.. _Manuel: https://pypi.python.org/pypi/manuel

----

Et des attributs / méthodes
===========================

.. code:: python

  >>> utilisateur = "Franck"
  >>> dir(utilisateur)
  ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__',
  '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
  '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', 
  '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__'
  ...
  'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 
  'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 
  'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 
  'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
  'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
  >>> utilisateur.count("f")
  0
  >>> utilisateur.count("z")
  0
  >>> utilisateur.count("F")
  1
  >>> utilisateur.count("r")
  1

.. _Manuel: https://pypi.python.org/pypi/manuel

----

Une console vraiment interactive, Ipython
==========================================

.. code:: python

  IPython 1.2.1 -- An enhanced Interactive Python.
  ?         -> Introduction and overview of IPython's features.
  %quickref -> Quick reference.
  help      -> Python's own help system.
  object?   -> Details about 'object', use 'object??' for extra details.

  In [1]: utilisateur = "Franck"

  In [2]: utilisateur.count?
  Type:       builtin_function_or_method
  String Form:<built-in method count of str object at 0x7f83f1325b10>
  Docstring:
  S.count(sub[, start[, end]]) -> int

  Return the number of non-overlapping occurrences of substring sub in
  string S[start:end].  Optional arguments start and end are interpreted
  as in slice notation.


.. _Manuel: https://pypi.python.org/pypi/manuel

----

Structure de données
====================

.. code:: python

  >>> position = (42.699745, 2.894889)
  >>> type(position)
  <type 'tuple'>
  >>> x, y = position
  >>> x
  42.699745
  >>> fruits = ["pomme", "orange", "banane"]
  >>> type(fruits)
  <type 'list'>
  >>> fruits[0]
  'pomme'
  >>> a, b, c = fruits
  >>> a
  'pomme'
  >>> b
  'orange'
  >>> fruits_par_jour = { "pomme": 2, "orange": 1, "banane": 3}
  >>> type(fruits_par_jour)
  <type 'dict'>
  >>> fruits_par_jour["pomme"]
  2
  >>> fruits_par_jour[b]
  1

.. _Manuel: https://pypi.python.org/pypi/manuel

----

Un programme
============

Stockons ce code python dans un fichier **cash_machine_01.py**

.. code:: python

  catalogue = {
      "pomme" : 0.95,
      "orange" : 0.80,
      "banane" : 1.20,
  }
  panier = {
      "pomme": 3,
      "banane":5,
  }
  total = 0

  for item in panier.iteritems():
      produit, quantite = item
      prix = catalogue[produit]
      total += prix * quantite

  print(total)

*voir source/code_examples/introduction_python/cash_machine_01.py*

.. _Manuel: https://pypi.python.org/pypi/manuel

----

Exécution du programme
======================

Le programme stocké dans le fichier source/code_examples/introduction_python/cash_machine_01.py s'exécute avec la commande:

.. code:: python

  python source/code_examples/introduction_python/cash_machine_01.py
  8.85

8.85 est le résultat retourné à la console via la fonction

  print(total)

.. _Manuel: https://pypi.python.org/pypi/manuel

----

Avec des fonctions
==================

En python le mot clef réservé pour la définition d'une fonction est **def**

.. code:: python

  catalogue = {
      "pomme" : 0.95,
      "orange" : 0.80,
      "banane" : 1.20,
  }
  panier = {
      "pomme": 3,
      "banane":5,
  }

  def total_panier(catalogue = catalogue, panier = panier):
      """
      Renvoie le total d'un panier en fonction du prix de chaque article en
      catalogue
      """
      total = 0
      for item in panier.iteritems():
          produit, quantite =  item
          prix = catalogue[produit]
          total += prix * quantite

      return total

  print(total_panier())


*voir source/code_examples/introduction_python/cash_machine_02.py*

.. _Manuel: https://pypi.python.org/pypi/manuel

----

Les classes
===========

Les classes sont définies avec le mot clef réservé ** class ** 

.. code:: python

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

*voir source/code_examples/introduction_python/cash_machine_03.py*

.. _Manuel: https://pypi.python.org/pypi/manuel

----

Les modules
===========

Python offre en standard de nombreux modules.

.. code:: python

  import time
  time.strftime("%c")
  >>> 'Thu Jul 21 13:01:24 2014'

L'ensemble des modules se trouvent sur le Cheese Shop https://pypi.python.org/

.. _Manuel: https://pypi.python.org/pypi/manuel

----

That's all folks!
=================

Merci
