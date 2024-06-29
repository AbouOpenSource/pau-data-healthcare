import time

from flask import Flask

LIMIT_LEFT = 27
LIMIT_RIGHT = 42


def get_data_from_topic():
    """
    Recuperer les donnees depuis MQTT, Kafka
    """
    temp = time.time() % LIMIT_RIGHT
    return {"temperature": temp, "tension_art": temp + 60}


app = Flask(__name__)


@app.route("/")
def hello_world():
    return (f"<p>Temperature est : {get_data_from_topic()['temperature']}</p><br>"
            f"<p>Tension est : {get_data_from_topic()['tension_art']}</p>")


# Gerer de tel sort qu'on n'a pas besoin de faire un refresh

# ajouter bootstrap avec chart affichant la donnee