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

#

PAGE_DATA = """
 <div class="container">
    <div class="row my-3">
        <div class="col">
            <h4>Bootstrap 5 Chart.js</h4>
        </div>
    </div>
    <div class="row my-2">
        <div class="col-md-6 py-1">
            <div class="card">
                <div class="card-body">
                    <canvas id="chLine"></canvas>
                </div>
            </div>
        </div>
        <div class="col-md-6 py-1">
            <div class="card">
                <div class="card-body">
                    <canvas id="chBar"></canvas>
                </div>
            </div>
        </div>
    </div>
    <div class="row py-2">
        <div class="col-md-4 py-1">
            <div class="card">
                <div class="card-body">
                    <canvas id="chDonut1"></canvas>
                </div>
            </div>
        </div>
        <div class="col-md-4 py-1">
            <div class="card">
                <div class="card-body">
                    <canvas id="chDonut2"></canvas>
                </div>
            </div>
        </div>
        <div class="col-md-4 py-1">
            <div class="card">
                <div class="card-body">
                    <canvas id="chDonut3"></canvas>
                </div>
            </div>
        </div>
    </div>
</div>
 
 """
