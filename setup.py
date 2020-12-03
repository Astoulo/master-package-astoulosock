#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
# notez qu'on import la lib

import master_package_astousock

# Ceci n'est qu'un appel de fonction. Mais il est trèèèèèèèèèèès long
# et il comporte beaucoup de paramètres
setup(
 
    # le nom de votre bibliothèque, tel qu'il apparaitre sur pypi
    name='master_package_astousock',
 
    # la version du code
    version=master_package_astousock.__version__,
 
    # Liste les packages à insérer dans la distribution
    # plutôt que de le faire à la main, on utilise la foncton
    # find_packages() de setuptools qui va cherche tous les packages
    # python recursivement dans le dossier courant.
    # C'est pour cette raison que l'on a tout mis dans un seul dossier:
    # on peut ainsi utiliser cette fonction facilement
    packages=find_packages(),
 
    # votre pti nom 
    author="Astou Lo Sock",
 
    # Votre email, sachant qu'il sera publique visible, avec tous les risques
    # que ça implique.
    author_email="astoulosock25@gmail.com",
 
    # Une description courte
    description="""Il existe 2 modules dans ce package:
                annee_bissextile() pour vérifier si la valeur saisie est bissextile ou pas 
                multiplication() pour retourner la table de multiplication de la valeur saisie""",
 
    # Une description longue, sera affichée pour présenter la lib
    # Généralement on dump le README ici
    long_description=open('README.md').read(),
 
    # Vous pouvez rajouter une liste de dépendances pour votre lib
    # et même préciser une version. A l'installation, Python essayera de
    # les télécharger et les installer.
    #
    # Ex: ["gunicorn", "docutils >= 0.3", "lxml==0.5a7"]
    #
    # Dans notre cas on en a pas besoin, donc je le commente, mais je le
    # laisse pour que vous sachiez que ça existe car c'est très utile.
    # install_requires= ,
 
    # Active la prise en compte du fichier MANIFEST.in
    include_package_data=True,
 
    # Une url qui pointe vers la page officielle de votre lib
    url='https://github.com/Astoulo/master-package-astoulosock',
 
    # Il est d'usage de mettre quelques metadata à propos de sa lib
    # Pour que les robots puissent facilement la classer.
    # La liste des marqueurs autorisées est longue:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    #
    # Il n'y a pas vraiment de règle pour le contenu. Chacun fait un peu
    # comme il le sent. Il y en a qui ne mettent rien.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Communications",
    ],
 
 
    # C'est un système de plugin, mais on s'en sert presque exclusivement
    # Pour créer des commandes, comme "django-admin".
    # Par exemple, si on veut créer la fabuleuse commande "annee_bissextile-sm", on
    # va faire pointer ce nom vers la fonction annee_bissextiler(). La commande sera
    # créé automatiquement. 
    # La syntaxe est "nom-de-commande-a-creer = package.module:fonction".
    entry_points = {
        'console_scripts': [
            'annee_bissextile-sm = master_package_astousock.annee_bissextile:annee_bissextile',
            'multiplication-sm = master_package_astousock.table_multiplication:multiplication',

        ],
    },
 
    # A fournir uniquement si votre licence n'est pas listée dans "classifiers"
    # ce qui est notre cas
    license="WTFPL",
 
    # Il y a encore une chiée de paramètres possibles, mais avec ça vous
    # couvrez 90% des besoins
 
)


# running install
# running bdist_egg
# running egg_info
# creating master_package.egg-info
# writing master_package.egg-info\PKG-INFO
# writing dependency_links to master_package.egg-info\dependency_links.txt
# writing entry points to master_package.egg-info\entry_points.txt
# writing top-level names to master_package.egg-info\top_level.txt
# writing manifest file 'master_package.egg-info\SOURCES.txt'
# reading manifest file 'master_package.egg-info\SOURCES.txt'
# reading manifest template 'MANIFEST.in'
# writing manifest file 'master_package.egg-info\SOURCES.txt'
# installing library code to build\bdist.win-amd64\egg
# running install_lib
# running build_py
# creating build
# creating build\lib
# creating build\lib\master_package
# copying master_package\annee_bissextile.py -> build\lib\master_package
# copying master_package\table_multiplication.py -> build\lib\master_package
# copying master_package\__init__.py -> build\lib\master_package
# creating build\bdist.win-amd64
# creating build\bdist.win-amd64\egg
# creating build\bdist.win-amd64\egg\master_package
# copying build\lib\master_package\annee_bissextile.py -> build\bdist.win-amd64\egg\master_package
# copying build\lib\master_package\table_multiplication.py -> build\bdist.win-amd64\egg\master_package
# copying build\lib\master_package\__init__.py -> build\bdist.win-amd64\egg\master_package
# byte-compiling build\bdist.win-amd64\egg\master_package\annee_bissextile.py to annee_bissextile.cpython-37.pyc
# byte-compiling build\bdist.win-amd64\egg\master_package\table_multiplication.py to table_multiplication.cpython-37.pyc
# byte-compiling build\bdist.win-amd64\egg\master_package\__init__.py to __init__.cpython-37.pyc
# creating build\bdist.win-amd64\egg\EGG-INFO
# copying master_package.egg-info\PKG-INFO -> build\bdist.win-amd64\egg\EGG-INFO
# copying master_package.egg-info\SOURCES.txt -> build\bdist.win-amd64\egg\EGG-INFO
# copying master_package.egg-info\dependency_links.txt -> build\bdist.win-amd64\egg\EGG-INFO
# copying master_package.egg-info\entry_points.txt -> build\bdist.win-amd64\egg\EGG-INFO
# copying master_package.egg-info\top_level.txt -> build\bdist.win-amd64\egg\EGG-INFO
# zip_safe flag not set; analyzing archive contents...
# creating dist
# creating 'dist\master_package-0.0.1-py3.7.egg' and adding 'build\bdist.win-amd64\egg' to it
# removing 'build\bdist.win-amd64\egg' (and everything under it)
# Processing master_package-0.0.1-py3.7.egg
# Copying master_package-0.0.1-py3.7.egg to c:\users\tmp_sarr51958.orange-sonatel\anaconda3\lib\site-packages
# Adding master-package 0.0.1 to easy-install.pth file
# Installing annee_bissextile-sm-script.py script to C:\Users\tmp_sarr51958.ORANGE-SONATEL\Anaconda3\Scripts
# Installing annee_bissextile-sm.exe script to C:\Users\tmp_sarr51958.ORANGE-SONATEL\Anaconda3\Scripts
# Installing multiplication-sm-script.py script to C:\Users\tmp_sarr51958.ORANGE-SONATEL\Anaconda3\Scripts
# Installing multiplication-sm.exe script to C:\Users\tmp_sarr51958.ORANGE-SONATEL\Anaconda3\Scripts

# Installed c:\users\tmp_sarr51958.orange-sonatel\anaconda3\lib\site-packages\master_package-0.0.1-py3.7.egg
# Processing dependencies for master-package==0.0.1
# Finished processing dependencies for master-package==0.0.1
