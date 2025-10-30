# Weather Data Warehouse Maghreb  
Projet de création d’un entrepôt de données météorologiques pour l’Algérie, la Tunisie et le Maroc

## 🧭 Description  
Ce projet vise à construire un **data warehouse** (schéma en étoile) pour stocker et analyser les données météo historiques couvrant l’Algérie, la Tunisie et le Maroc.  
Le pipeline ETL inclut l’extraction depuis des fichiers CSV, le nettoyage, la transformation, puis le chargement dans une base MySQL (`weathers_datawarehouse`).  
Une application Dash permet la visualisation par pays (températures moyennes, maximales, etc.).  
Un calcul d’entropie est réalisé sur les conditions météorologiques afin d’analyser la variabilité des climats dans chaque pays.

## 📦 Contenu du dépôt  
- `etl/` — Scripts Python pour extraction, nettoyage, transformation et chargement (ETL).  
- `data/` — Dossiers par pays : `Algeria/`, `Tunisia/`, `Morocco/` contenant les fichiers CSV sources.  
- `db/` — Scripts SQL : création de la base, tables, index.  
- `visualisation/` — Application Dash + notebooks pour visualisation et calculs d’entropie.  
- `README.md` — Ce fichier.

## 🔧 Prérequis  
- Python 3.12 ou équivalent  
- Bibliothèques : `numpy`, `pandas`, `pymysql`, `plotly`, `dash`  
- Serveur MySQL ou MariaDB local  
- Fichiers CSV dans `data/` (à placer manuellement ou télécharger)

## 🚀 Installation & exécution  
1. Cloner ce dépôt :  
   ```bash
   git clone https://github.com/<votre-nom-utilisateur>/weather-data-warehouse-maghreb.git
   cd weather-data-warehouse-maghreb
