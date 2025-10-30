### Les bibliothéques necessaires
import numpy as np 
import pandas as pd 
import sys
import os
sys.path.append(r'c:\users\dell\appdata\roaming\python\python312\site-packages')
import pymysql 
import csv
import plotly.express as px
import plotly.graph_objects as go

### Comparison des attributs communs et différents, avec comptage des attributs partagés et uniques pour les fichiers CSV de l'Algérie. 
def extraire_en_tetes(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        return next(csv.reader(f))

def compter_attributs(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        return len(next(csv.reader(f), []))

chemin_dossier = './Weather Data/Algeria'

fichiers = [
    "Weather_1930-1939_ALGERIA.csv",
    "Weather_1940-1949_ALGERIA.csv",
    "Weather_1950-1959_ALGERIA.csv",
    "Weather_1960-1969_ALGERIA.csv",
    "Weather_1970-1979_ALGERIA.csv",
    "Weather_1980-1989_ALGERIA.csv",
    "Weather_1990-1999_ALGERIA.csv",
    "Weather_2000-2009_ALGERIA.csv",
    "Weather_2010-2019_ALGERIA.csv",
    "Weather_2020-2022_ALGERIA.csv",
    "Weather_1920-1929_ALGERIA.csv"
]

en_tetes_fichiers = {fichier: extraire_en_tetes(os.path.join(chemin_dossier, fichier)) for fichier in fichiers}

colonnes_communes = set(en_tetes_fichiers[fichiers[0]])
colonnes_differentes = {fichier: set(en_tetes_fichiers[fichier]) - colonnes_communes for fichier in en_tetes_fichiers}

print("Colonnes communes à tous les fichiers :", colonnes_communes)
print("\nColonnes différentes pour chaque fichier :")
for fichier, colonnes in colonnes_differentes.items():
    print(f"{fichier} : {colonnes}")

print("\nNombre d'attributs dans chaque fichier :")
for fichier in fichiers:
    print(f"Nombre d'attributs dans {fichier}: {compter_attributs(os.path.join(chemin_dossier, fichier))}")

### Comparison des attributs communs et différents, avec comptage des attributs partagés et uniques pour les fichiers CSV de Morocco.
def extraire_en_tetes(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        return next(csv.reader(f))

def compter_attributs(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        return len(next(csv.reader(f), []))

chemin_dossier = './Weather Data/Morocco'

fichiers = [
    "Weather_1920-1959_MOROCCO.csv",
    "Weather_1960-1989_MOROCCO.csv",
    "Weather_1990-2019_MOROCCO.csv",
    "Weather_2020-2022_MOROCCO.csv"
]

en_tetes_fichiers = {fichier: extraire_en_tetes(os.path.join(chemin_dossier, fichier)) for fichier in fichiers}

colonnes_communes = set(en_tetes_fichiers[fichiers[0]])
colonnes_differentes = {fichier: set(en_tetes_fichiers[fichier]) - colonnes_communes for fichier in en_tetes_fichiers}

print("Colonnes communes à tous les fichiers :", colonnes_communes)
print("\nColonnes différentes pour chaque fichier :")
for fichier, colonnes in colonnes_differentes.items():
    print(f"{fichier} : {colonnes}")

print("\nNombre d'attributs dans chaque fichier :")
for fichier in fichiers:
    print(f"Nombre d'attributs dans {fichier}: {compter_attributs(os.path.join(chemin_dossier, fichier))}")

### Comparison des attributs communs et différents, avec comptage des attributs partagés et uniques pour les fichiers CSV de Tunisia.
def extraire_en_tetes(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        return next(csv.reader(f))

def compter_attributs(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        return len(next(csv.reader(f), []))

chemin_dossier = './Weather Data/Tunisia'

fichiers = [
    "Weather_1920-1959_TUNISIA.csv",
    "Weather_1960-1989_TUNISIA.csv",
    "Weather_1990-2019_TUNISIA.csv",
    "Weather_2020-2022_TUNISIA.csv"
]

en_tetes_fichiers = {fichier: extraire_en_tetes(os.path.join(chemin_dossier, fichier)) for fichier in fichiers}

colonnes_communes = set(en_tetes_fichiers[fichiers[0]])
colonnes_differentes = {fichier: set(en_tetes_fichiers[fichier]) - colonnes_communes for fichier in en_tetes_fichiers}

print("Colonnes communes à tous les fichiers :", colonnes_communes)
print("\nColonnes différentes pour chaque fichier :")
for fichier, colonnes in colonnes_differentes.items():
    print(f"{fichier} : {colonnes}")

print("\nNombre d'attributs dans chaque fichier :")
for fichier in fichiers:
    print(f"Nombre d'attributs dans {fichier}: {compter_attributs(os.path.join(chemin_dossier, fichier))}")

