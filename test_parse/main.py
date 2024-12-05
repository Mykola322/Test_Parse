from flask import Flask, render_template

from data.weather import get_weather
from data.base import create_db
from data.models import Pizza, Ingredient


app = Flask(__name__)


@app.get("/")
def index():
    weather = get_weather("Lviv")

    pizza_recom = ""
    if weather.get("temp") < 0:
        pizza_recom = "Неаполітано"
    elif weather.get("temp") > 40:
        pizza_recom = "Холодна пиця"
    elif 0 <= weather.get("temp") < 20:
        pizza_recom = "Класична пиця"
    else:
        pizza_recom = "Грибна пиця"

    return render_template("index.html", weather=weather, pizza_recom=pizza_recom)



if __name__ == "__main__":
    create_db()
    app.run(debug=True)
