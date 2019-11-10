# ProjetUdes_imgMedicale2

Le projet suivant est un exercice proposé par le cours IMN503 "Reconstruction d'imagerie médicale". L'objectif est de se familiariser avec plusieurs notions importantes du traitement d'images médicales telles que le calcul de similarité, les transformations (rigides, similitudes, affines...) et le recalage.

# Installation

Requis: Python 3.5+ | Linux, Mac OS X, Windows

```sh
pip install pipenv
```
Puis dans le dossier du projet:  

```sh
pipenv install --python 3.5
```
Le pipfile permettra l'installation de toutes les dépendances nécessaires à l'utilisation du projet. 
Puis pour exécuter des commandes dans cet environnement virtuel: 

```sh
pipenv shell
```

# Préparez-vous :

Le script principal de ce projet se nomme tp2.py, il permet d'afficher la réponse à toutes les questions du sujet. Le premier argument à passer est le numéro de la question. Pour exemple, on peut lancer la commande suivante proposant une aide pour les différents arguments à passer pour chaque question:
```sh
python tp2.py 1
```

# Exemple : 

Exemple d'utilisation:

La question 1 est de générer les histogrammes conjoints de plusieurs couples d'images: 
```sh
pipenv run python tp2.py 1
```
![alt text](https://github.com/EmmaJouffroy/projetUdes_imgMedicale2/blob/master/Resultats/Histogramme/histogrammes.png)

La question 2 s'intéresse à différents moyens de transformer des volumes (ici c'est une transformation similitude):
```sh
pipenv run python tp2.py 3 similitude 1.5 90 0 0 5 5 5
```
<p align="center">
<img src="https://github.com/EmmaJouffroy/projetUdes_imgMedicale2/blob/master/Resultats/Transformation/transfo.png" alt="drawing" width="500"/>
</div>

# Auteurs

* **Emma Jouffroy** - [PurpleBooth](https://github.com/EmmaJouffroy)
* **Maxime Adolphe** - [PurpleBooth](https://github.com/madolphe)

