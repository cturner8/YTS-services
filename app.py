from flask import Flask
import functions

app = Flask(__name__)


@app.route('/')
def render():
    filter = {}
    filter["title"] = ""
    filter["dateTo"] = ""
    filter["dateFrom"] = ""

    data = functions.get_data(filter)
    print(data["youtube_count"])
    
    return "Result " + str(data["youtube_count"])