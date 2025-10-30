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


### Connexion à la base de données
conn = pymysql.connect(host = 'localhost',
                            user = 'root',
                            password='',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
cur.execute("DROP DATABASE IF EXISTS weathers_datawarehouse")
# Créer la base de données
cur.execute("CREATE DATABASE weathers_datawarehouse")
print("La base de données 'weathers_datawarehouse' a été créée.")
# Utiliser la base de données weathers_datawarehouse
cur.execute("USE weathers_datawarehouse")
### La creation des tables 
# Suppression des tables existantes
cur.execute("DROP TABLE IF EXISTS Fact_Weather")
cur.execute("DROP TABLE IF EXISTS Dim_Date")
cur.execute("DROP TABLE IF EXISTS Station_Dim")

# Création de la table Dimension Date
cur.execute('''CREATE TABLE Dim_Date (
                Date_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                Date TEXT
                )''')

# Création de la table Dimension Location
cur.execute('''CREATE TABLE Station_Dim (
                Station_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                Station_Name TEXT,
                Station_Code TEXT,
                Evaluation REAL,
                Latitude REAL,
                Longitude REAL,
                Country_Name TEXT
                )''')

# Création de la table Fact_Weather
cur.execute('''CREATE TABLE Fact_Weather (
                Weather_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                Date_ID INTEGER,
                Station_ID INTEGER,
                PRCP REAL,
                SNWD REAL,
                SNOW REAL,
                TAVG REAL,
                TMAX REAL,
                TMIN REAL,
                WDFG REAL,
                PGTM INTEGER,
                WSFG REAL,
                FOREIGN KEY(Date_ID) REFERENCES Dim_Date(Date_ID),
                FOREIGN KEY(Station_ID) REFERENCES Station_Dim(Station_ID)
                )''')

print("la table Fact_Weather created")
print("la table Date_Dim created")
print("la table Station_Dim created")


## le processus ETL
### Extraction et Transformation des fichiers Algeria
# Chemin vers le dossier contenant les données
chemin_dossier = "./Weather Data/Algeria"

# Liste des noms de fichiers CSV
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
    "Weather_2020-2022_ALGERIA.csv"
]

# Fonction pour nettoyer un fichier de données
def nettoyer_fichier(chemin_fichier):
    # Charger le fichier CSV en un DataFrame pandas
    df = pd.read_csv(chemin_fichier)
    
    # Supprimer les lignes avec des valeurs manquantes dans les colonnes pertinentes
    colonnes_climatiques = ["PRCP", "TAVG", "TMAX", "TMIN"]
    df = df.dropna(subset=colonnes_climatiques)
    
    # Afficher le nombre de valeurs manquantes pour chaque colonne après le nettoyage
    print(f"Nombre de valeurs manquantes pour chaque colonne après le nettoyage du fichier {chemin_fichier}:")
    print(df.isnull().sum())
    
    # Sauvegarder le DataFrame nettoyé dans le fichier d'origine
    df.to_csv(chemin_fichier, index=False)
    
    print(f"Données nettoyées sauvegardées dans {chemin_fichier}")

# Nettoyer tous les fichiers
for fichier in fichiers:
    print(f"Nettoyage du fichier {fichier}:")
    chemin_complet = os.path.join(chemin_dossier, fichier)
    nettoyer_fichier(chemin_complet)

print("Nettoyage terminé!")



### Extraction et Transformation des fichiers Tunisia
# Chemin vers le dossier contenant les données
chemin_dossier = "./Weather Data/Tunisia"

# Liste des noms de fichiers CSV
fichiers = [
    "Weather_1920-1959_TUNISIA.csv",
    "Weather_1960-1989_TUNISIA.csv",
    "Weather_1990-2019_TUNISIA.csv",
    "Weather_2020-2022_TUNISIA.csv"
]

# Fonction pour nettoyer un fichier de données
def nettoyer_fichier(chemin_fichier):
    # Charger le fichier CSV en un DataFrame pandas
    df = pd.read_csv(chemin_fichier)
    
    # Supprimer les lignes avec des valeurs manquantes dans les colonnes pertinentes
    colonnes_climatiques = ["PRCP", "TAVG", "TMAX", "TMIN"]
    df = df.dropna(subset=colonnes_climatiques)
    
    # Afficher le nombre de valeurs manquantes pour chaque colonne après le nettoyage
    print(f"Nombre de valeurs manquantes pour chaque colonne après le nettoyage du fichier {chemin_fichier}:")
    print(df.isnull().sum())
    
    # Sauvegarder le DataFrame nettoyé dans le fichier d'origine
    df.to_csv(chemin_fichier, index=False)
    
    print(f"Données nettoyées sauvegardées dans {chemin_fichier}")

# Nettoyer tous les fichiers
for fichier in fichiers:
    print(f"Nettoyage du fichier {fichier}:")
    chemin_complet = os.path.join(chemin_dossier, fichier)
    nettoyer_fichier(chemin_complet)

print("Nettoyage terminé!")


### Extraction et Transformation des fichiers Morocco
# Chemin vers le dossier contenant les données
chemin_dossier = "./Weather Data/Morocco"

# Liste des noms de fichiers CSV
fichiers = [
    "Weather_1920-1959_MOROCCO.csv",
    "Weather_1960-1989_MOROCCO.csv",
    "Weather_1990-2019_MOROCCO.csv",
    "Weather_2020-2022_MOROCCO.csv"
]

# Fonction pour nettoyer un fichier de données
def nettoyer_fichier(chemin_fichier):
    # Charger le fichier CSV en un DataFrame pandas
    df = pd.read_csv(chemin_fichier, low_memory=False)
    
    # Supprimer les lignes avec des valeurs manquantes dans les colonnes pertinentes
    colonnes_climatiques = ["PRCP", "TAVG", "TMAX", "TMIN"]
    df = df.dropna(subset=colonnes_climatiques)
    
    # Afficher le nombre de valeurs manquantes pour chaque colonne après le nettoyage
    print(f"Nombre de valeurs manquantes pour chaque colonne après le nettoyage du fichier {chemin_fichier}:")
    print(df.isnull().sum())
    
    # Sauvegarder le DataFrame nettoyé dans le fichier d'origine
    df.to_csv(chemin_fichier, index=False)
    
    print(f"Données nettoyées sauvegardées dans {chemin_fichier}")

# Nettoyer tous les fichiers
for fichier in fichiers:
    print(f"Nettoyage du fichier {fichier}:")
    chemin_complet = os.path.join(chemin_dossier, fichier)
    nettoyer_fichier(chemin_complet)

print("Nettoyage terminé!")



### Charger les fichiers de Algeria 
# Liste des fichiers CSV à insérer
fichiers = [
               "Weather_1920-1929_ALGERIA.csv",
               "Weather_1930-1939_ALGERIA.csv",
               "Weather_1940-1949_ALGERIA.csv",
               "Weather_1950-1959_ALGERIA.csv",
               "Weather_1960-1969_ALGERIA.csv",
               "Weather_1970-1979_ALGERIA.csv",
               "Weather_1980-1989_ALGERIA.csv",
               "Weather_1990-1999_ALGERIA.csv",
               "Weather_2000-2009_ALGERIA.csv",
               "Weather_2010-2019_ALGERIA.csv",
               "Weather_2020-2022_ALGERIA.csv"
]

for fichier in fichiers:
    # Chemin d'accès au fichier CSV
    csv_file = os.path.join("Weather Data", "Algeria", fichier)

    # Ouverture du fichier CSV
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Insérer des données dans la table Station_Dim en ignorant les duplicatas
            cur.execute("INSERT IGNORE INTO Station_Dim (Station_Code, Station_Name, Latitude, Longitude, Evaluation, Country_Name) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (row['STATION'], row['NAME'], row['LATITUDE'], row['LONGITUDE'], row['ELEVATION'], 'Algeria'))

            # Récupérer l'ID de la station insérée
            cur.execute("SELECT LAST_INSERT_ID() AS Station_ID")
            station_id = cur.fetchone()['Station_ID']

            # Insérer des données dans la table Dim_Date en ignorant les duplicatas
            cur.execute("INSERT IGNORE INTO Dim_Date (Date) VALUES (%s)", (row['DATE'],))
            cur.execute("SELECT LAST_INSERT_ID() AS Date_ID")
            date_id = cur.fetchone()['Date_ID']
            
            # Insérer des données dans la table Fact_Weather en utilisant les identifiants de station et de date correspondants
            cur.execute("INSERT INTO Fact_Weather (Date_ID, Station_ID, PRCP, TAVG, TMAX, TMIN) VALUES (%s, %s, %s, %s, %s, %s)", 
                          (date_id, station_id, row['PRCP'], row['TAVG'], row['TMAX'], row['TMIN']))


 ### Charger les fichiers de Tunisia
 # Liste des fichiers CSV à insérer pour la Tunisie
fichiers_tunisie = [
    "Weather_1920-1959_TUNISIA.csv",
    "Weather_1960-1989_TUNISIA.csv",
    "Weather_1990-2019_TUNISIA.csv",
    "Weather_2020-2022_TUNISIA.csv"
]

for fichier in fichiers_tunisie:
    # Chemin d'accès au fichier CSV
    csv_file = os.path.join("Weather Data", "Tunisia", fichier)

    # Ouverture du fichier CSV
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Insérer des données dans la table Station_Dim en ignorant les duplicatas
            cur.execute("INSERT IGNORE INTO Station_Dim (Station_Code, Station_Name, Latitude, Longitude, Evaluation, Country_Name) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (row['STATION'], row['NAME'], row['LATITUDE'], row['LONGITUDE'], row['ELEVATION'], 'Tunisia'))

            # Récupérer l'ID de la station insérée
            cur.execute("SELECT LAST_INSERT_ID() AS Station_ID")
            station_id = cur.fetchone()['Station_ID']

             # Insérer des données dans la table Dim_Date en ignorant les duplicatas
            cur.execute("INSERT IGNORE INTO Dim_Date (Date) VALUES (%s)", (row['DATE'],))
            cur.execute("SELECT LAST_INSERT_ID() AS Date_ID")
            date_id = cur.fetchone()['Date_ID']
            
            # Insérer des données dans la table Fact_Weather en utilisant les identifiants de station et de date correspondants
            cur.execute("INSERT INTO Fact_Weather (Date_ID, Station_ID, PRCP, TAVG, TMAX, TMIN) VALUES (%s, %s, %s, %s, %s, %s)", 
                          (date_id, station_id, row['PRCP'], row['TAVG'], row['TMAX'], row['TMIN']))

###  Charger les fichiers de Morocco
# Liste des fichiers CSV à insérer pour le Maroc
fichiers_maroc = [
    "Weather_1920-1959_MOROCCO.csv",
    "Weather_1960-1989_MOROCCO.csv",
    "Weather_1990-2019_MOROCCO.csv",
    "Weather_2020-2022_MOROCCO.csv"
]

for fichier in fichiers_maroc:
    # Chemin d'accès au fichier CSV
    csv_file = os.path.join("Weather Data", "Morocco", fichier)

    # Ouverture du fichier CSV
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Insérer des données dans la table Station_Dim en ignorant les duplicatas
            cur.execute("INSERT IGNORE INTO Station_Dim (Station_Code, Station_Name, Latitude, Longitude, Evaluation, Country_Name) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (row['STATION'], row['NAME'], row['LATITUDE'], row['LONGITUDE'], row['ELEVATION'], 'Morocco'))

            # Récupérer l'ID de la station insérée
            cur.execute("SELECT LAST_INSERT_ID() AS Station_ID")
            station_id = cur.fetchone()['Station_ID']

             # Insérer des données dans la table Dim_Date en ignorant les duplicatas
            cur.execute("INSERT IGNORE INTO Dim_Date (Date) VALUES (%s)", (row['DATE'],))
            cur.execute("SELECT LAST_INSERT_ID() AS Date_ID")
            date_id = cur.fetchone()['Date_ID']
            
            # Insérer des données dans la table Fact_Weather en utilisant les identifiants de station et de date correspondants
            cur.execute("INSERT INTO Fact_Weather (Date_ID, Station_ID, PRCP, TAVG, TMAX, TMIN) VALUES (%s, %s, %s, %s, %s, %s)", 
                          (date_id, station_id, row['PRCP'], row['TAVG'], row['TMAX'], row['TMIN']))

print("chargement terminee")