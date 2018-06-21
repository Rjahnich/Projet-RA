# Projet-RA (Réalité Augmentée)
Mur d'escalade en réalité augmenté
Projet Lpro MECSE Sesam IUT CACHAN 2018
```
Ce projet n'est pas fini, voir la fin de ce README pour voir les étapes maquantes
````
Le but de ce projet est de créer un jeu d'escalade en utilisant une kinect.
Dans ce projet nous allons utiliser Python pour la programmation.
Pour l'interface du jeu, nous allons utiliser la librairie Pygame et pour la gestion de la kinect, la librairie PyKinect2.
## Matériels

* PC Windows 10
* Kinect 2 avec son adaptateur pour windows

## Prérequis

Liste complète des dépendances
* [Python 2.7.x or 3.4 and higher](https://www.python.org/)  
* [NumPy](http://www.numpy.org/) 
* [comtypes](https://github.com/enthought/comtypes/) 
* [Kinect for Windows SDK v2](http://aka.ms/k4wv2sdk) - pilote pour la kinect pro
* [Kinect v2 sensor and adapter](http://aka.ms/k4wv2purchase) Remarque: vous pouvez utiliser un Kinect pour Xbox One tant que vous possédez également l'adaptateur Kinect pour Windows
* [PyGame](http://www.pygame.org)
* [PyKinect2](https://github.com/Kinect/PyKinect2)
* [os](https://docs.python.org/fr/3.5/library/os.html)

## Installation des librairies

Le plus simple pour installer les librairies est d'utiliser pip.
Exemple :
```
pip install pygame
````
(Certaines librairies sont déjà intallés selon la version de Python que vous utilisez)

## Utilisation de l'interface

Pour utiliser l'interface, il faut mettre le programme "interface.py" ainsi que les deux fichier "Images interface" et "Fichier de sauvegarde" dézipper dans un même dossier.
Changer le chemin de dossier dans le programme "interface.py"-ligne 8 avec le vôtre.

## Partie Interface

L'interface comprend 3 écrans :

* Accueil 

Un choix de 4 niveau : facile, moyen, difficile, personnalisé

* Edition 

Encore un choix entre 3 parcours. Les noms des différents parcours sont modifiables (avec le bouton éditer de l'interface) et enregistrés à chaque modification dans un fichier texte.
Après le choix d'un parcours, le programme lit les positions des cibles dans deux fichiers texte (un pour la position X, et l'autre pour la position Y). Un bouton "modification cibles" présent sur l'interface permet de déplacer les cibles et de les re-enregistrer par la suite.

* Jeu

Vision du jeu

## Partie Kinect

Pour la partie Kinect nous sommes partis de l'exemple [PyKinectBodyGame.py](https://github.com/Kinect/PyKinect2/blob/master/examples/PyKinectBodyGame.py) pour avoir la détection du squelette.
Ensuite nous avons supprimé les traits du squelette pour ne garder que la position des mains. Pour finir nous avons affiché un cercle sur chaque main pour avoir un visuel de la détection.

# Reste à faire

* Dans l'écran d'édition : Récupérer une image de la kinect et placer les cibles sur celle-ci. (Pour l'instant les cibles sont placées sur un fond noir)
* Dans l'écran de jeu : Affichage de l'image récupérée par la kinect avec les différentes cibles présentent sur celle-ci. Si le joueur reste avec sa main plus de une seconde dans la cible, la cible change de couleur ou disparait et un système de score s'implémente à chaque cible touché.
