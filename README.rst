=======
Diapos
=======

Un endroit pour stocker mes présentations.

Pour voir les présentations c'est par là http://franckbret.github.io

Ces présentations sont générées avec un outil python qui s'appelle Hovercraft.

Hovercraft permet de transformer des document au format Restructured Text (.rst) en une présentation html basée sur impress.js.

Installation
------------

Pré-requis
~~~~~~~~~~

* Python
* hovercraft

Installation dans un virtualenv (méthode recommandée):

    sudo apt-get install python-virtualenv && sudo apt-get install python-pip 
    virtualenv -p /usr/bin/python3.3 diapos
    cd diapos/
    # pour activer l'environnement virtuel
    source bin/activate

    # pour désactiver l'environnement virtuel
    deactivate 

Usage & Configuration
~~~~~~~~~~~~~~~~~~~~~

Une fois l'environnement virtuel activé, on créé un dossier pour stocker le projet

    mkdir opt

On récupère le projet : 

    cd opt
    git clone https://github.com/franckbret/diapos.git

Et on installe les dépendances : 
    cd diapos
    pip install -r requirements.txt

On vérifie que hovercraft est bien installé.

    hovercraft --help

Devrait donner comme sortie : 

    Usage: hovercraft [-h] [-t TEMPLATE] [-c CSS] [-a] [-s] [-n]
                  <presentation> <targetdir>

    Create impress.js presentations with reStructuredText

    Positional arguments:
      <presentation>        The path to the reStructuredText presentation file.
      <targetdir>           The directory where the presentation is written. Will
                            be created if it does not exist.

    Optional arguments:
      -h, --help            Show this help.
      -t TEMPLATE, --template TEMPLATE
                            Specify a template. Must be a .cfg file, or a
                            directory with a template.cfg file. If not given it
                            will use a default template.
      -c CSS, --css CSS     An additional css file for the presentation to use.
      -a, --auto-console    Pop up the console automatically. This is useful when
                            you are rehearsing and making sure the presenter notes
                            are correct.
      -s, --skip-help       Do not show the initial help popup.
      -n, --skip-notes      Do not include presenter notes in the output.




Pour générer une présentation on utilise la commande `hovercraft $source $ $destination`,
où `$source` correspond au fichier `.rst` que l'on veut convertir et `destination` au répertoire 
dans lequel sera exporté le présentation au format html.

    hovercraft source/introduction_python.rst html/introduction_python


Voir une présentation
~~~~~~~~~~~~~~~~~~~~~

On lance le fichier index.html de la présentation dans un navigateur.

    firefox html/introduction_python/index.html

Plus d'infos
~~~~~~~~~~~~

Restructured Text (.rst)

__ http://fr.wikipedia.org/wiki/ReStructuredText

Hovercraft

__ https://hovercraft.readthedocs.org/en/1.0/

Impress.js

__ https://github.com/bartaz/impress.js/

Ipython

__ http://ipython.org/

Virtualenv

__ http://virtualenv.readthedocs.org/


