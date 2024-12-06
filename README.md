# Projet Azure: Application Web de Liste de Films

## Description
Ce projet déploie une application web qui affiche une liste de films à partir d'une base de données SQL hébergée sur Azure. Il utilise plusieurs services Azure pour la gestion des données, le stockage d'images, et le déploiement de l'application via des conteneurs Docker.

## Prérequis
- **Compte Azure** : Créer un compte sur [Azure](https://azure.microsoft.com/fr-fr/free/).
- **Outils nécessaires** :
  - [Visual Studio Code](https://code.visualstudio.com/)
  - [Azure CLI](https://learn.microsoft.com/fr-fr/cli/azure/)
  - [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Services utilisés
1. **Azure SQL Database** : Pour stocker les métadonnées des films.
2. **Azure Container Registry (ACR)** : Pour héberger l'image Docker.
3. **Azure Storage** : Pour stocker les images des films.
4. **Azure App Service** : Pour héberger l'application web.

## Étapes du projet
1. **Création des ressources Azure** :
   - Créer un groupe de ressources.
   - Configurer la base de données SQL pour stocker les films.
   - Créer une compte de stockage pour stocker des images de film.
   - Créer un registre de conteneurs pour héberger l'image Docker de l'application.
   - Déployer l'application web via Azure App Service.

2. **Configuration de l'image Docker** :
   - Créer un dossier avec les fichiers nécessaires (`Dockerfile`, `index.html`, `main.py`, etc.).
   - Construire l'image Docker et la pousser sur ACR.

3. **Code de l'application** :
   - Utiliser **FastAPI** pour créer l'API web qui récupère et affiche les films à partir de la base de données.
   - Le front-end est basé sur du HTML et CSS pour afficher les films sous forme de cartes avec les informations et images correspondantes.

## Structure du projet
- **Dockerfile** : Fichier de configuration pour créer l'image Docker.
- **index.html** : Template HTML pour afficher la liste des films.
- **main.py** : Code Python avec FastAPI pour gérer les requêtes et interagir avec la base de données.
- **style.css** : Fichier CSS pour le style de l'interface web.

## Lancer l'application
1. **Construire l'image Docker** :
   ```bash
   docker build -t app-cc .
   docker run -d -p 8080:8080 app-cc
