# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import pyodbc

app = FastAPI()

# Paramètres de connexion à la base de données Azure SQL
server = 'serverbddzz.database.windows.net'
database = 'BddZyad'
username = 'adminuser'
password = 'Azerty@1234'
driver = '{ODBC Driver 17 for SQL Server}'

# Connexion à la base de données Azure SQL
def get_db_connection():
    try:
        conn = pyodbc.connect(
            f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
        )
        return conn
    except Exception as e:
        raise Exception(f"Erreur de connexion à la base de données : {str(e)}")

# Route principale pour afficher les films
@app.get("/", response_class=HTMLResponse)
def read_root():
    try:
        # Connexion à la base de données
        conn = get_db_connection()
        cursor = conn.cursor()

        # Récupération des films
        cursor.execute("SELECT titre, realisateur, genre, date_sortie, duree_min, synopsis, note, image_url FROM Film")
        rows = cursor.fetchall()
        conn.close()

        # Génération du contenu HTML pour les cartes de films
        cards_html = ""
        for row in rows:
            titre, realisateur, genre, date_sortie, duree_min, synopsis, note, image_url = row
            cards_html += f"""
            <div class='card'>
                <img src='{image_url}' alt='Affiche de {titre}' class='card-img'>
                <div class='card-content'>
                    <h2 class='card-title'>{titre}</h2>
                    <p><strong>Réalisateur :</strong> {realisateur}</p>
                    <p><strong>Genre :</strong> {genre}</p>
                    <p><strong>Date de sortie :</strong> {date_sortie}</p>
                    <p><strong>Durée :</strong> {duree_min} min</p>
                    <p><strong>Synopsis :</strong> {synopsis}</p>
                    <p><strong>Note :</strong> {note}/10</p>
                </div>
            </div>
            """

        # Lecture du fichier HTML
        with open("index.html", "r", encoding="utf-8") as html_file:
            html_template = html_file.read()

        # Injection des cartes dans le template HTML
        html_content = html_template.replace("{cards_html}", cards_html)

        return HTMLResponse(content=html_content)

    except Exception as e:
        return HTMLResponse(content=f"<h1>Erreur interne</h1><p>{str(e)}</p>", status_code=500)

# Route pour le fichier CSS
@app.get("/style.css", response_class=FileResponse)
def get_styles():
    return FileResponse("style.css")