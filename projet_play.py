import random
import mysql.connector
from datetime import datetime

# Fonction pour générer une phrase aléatoire
def generate_sentence():
    subjects = ["A cat", "The dog", "A bird", "The mouse"]
    actions = ["eating", "playing with", "chasing", "sleeping near"]
    objects = ["a piece of cheese", "a ball", "a toy", "a mouse"]

    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)

    sentence = f"{subject} {action} {obj}"
    return sentence

# Fonction pour insérer une phrase dans la base de données
def insert_sentence(sentence):
    try:
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="playground"
        )
        cursor = conn.cursor()
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO collecte (date, sentences) VALUES (%s, %s)", (current_datetime, sentence))
        conn.commit()
    except (Exception, mysql.Error) as error:
        print("Erreur lors de l'insertion dans la base de données :", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Générer une phrase et l'insérer dans la base de données
sentence = generate_sentence()
print("Phrase générée :", sentence)
insert_sentence(sentence)
print("Phrase insérée dans la base de données.")
