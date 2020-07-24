from flask import Flask, render_template
import functions

app = Flask(__name__)

filter = {}
filter["title"] = ""
filter["dateTo"] = ""
filter["dateFrom"] = ""

data = functions.get_data(filter)


@app.route('/')
def home():
    print(data["youtube_count"])

    return render_template("home.html", data=data)
