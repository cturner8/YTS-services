import json
from datetime import datetime
from os import path


def load_data():
    data = []

    if path.exists("env.json"):
        with open("env.json", encoding="utf8") as json_file:
            data = json.load(json_file)

    return data


def save_data(data):
    with open("out.json", "w") as outfile:
        json.dump(data, outfile, indent=4)


def capture_filters():
    filter = {}
    filter["title"] = input(
        "What search filter would you like to add? ").lower()
    filter["dateFrom"] = input(
        "When would you like to start the search from? ")
    filter["dateTo"] = input("When would you like to end the search? ")

    return filter


def filter_by_title(row, filter):
    result = True

    if filter["title"] is not None:
        result = filter["title"] in row["title"].lower()

    return result


def filter_by_date(row, filter):
    result = True

    dateFrom = datetime.now()
    dateTo = datetime.now()

    if filter["dateFrom"] == "" and filter["dateTo"] == "":
        return result

    if filter["dateFrom"] != "":
        dateFrom = datetime.fromisoformat(filter["dateFrom"])
    if filter["dateTo"] != "":
        dateTo = datetime.fromisoformat(filter["dateTo"])

    time = datetime.fromisoformat(row["time"].replace("Z", ""))

    if dateFrom <= dateTo:
        result = dateFrom <= time <= dateTo
    else:
        result = dateFrom <= time or time <= dateTo

    return result


def filter_data(row, filter):
    result = False

    dateResult = filter_by_date(row, filter)
    titleResult = filter_by_title(row, filter)

    result = dateResult and titleResult

    return result


def generate_report(data, filter):
    report = {}
    report["youtube_count"] = 0
    report["youtube_music_count"] = 0
    report["channels"] = {}
    report["raw_data"] = []

    for row in data:
        if filter_data(row, filter) == True:
            if (row["header"] == "YouTube"):
                report = process_video(row, report)
            elif (row["header"] == "YouTube Music"):
                report = process_music(row, report)
            row["title"] = row["title"].replace("Watched", "")

            report["raw_data"].append(row)

    return report


def sort_report(report):
    report["channels"] = {k: v for k, v in sorted(
        report["channels"].items(), key=lambda item: item[1], reverse=True)}

    return report


def process_video(row, report):
    report["youtube_count"] += 1

    if "subtitles" in row:
        channel = row["subtitles"][0]["name"]

        if (channel in report["channels"]):
            report["channels"][channel] += 1
        else:
            report["channels"][channel] = 1

    return report


def process_music(row, report):
    report["youtube_music_count"] += 1

    return report


def get_data(filter, file_data):
    data = {}

    if len(file_data) > 0:
        data = generate_report(file_data, filter)
    else:
        data = generate_report(load_data(), filter)

    data = sort_report(data)

    return data


def has_filters(filter):
    return filter["title"] != "" or filter["dateFrom"] != "" or filter["dateTo"] != ""


def search_data(request):
    filter = {
        "title": "",
        "dateTo": "",
        "dateFrom": ""
    }
    file_data = []

    if request.method == "POST":
        body = request.get_json()

        filter["title"] = body.get("title", "")
        filter["dateTo"] = body.get("dateTo", "")
        filter["dateFrom"] = body.get("dateFrom", "")
        file_data = body.get("fileData", [])

    response_body = {
        "filter": filter,
        "items": get_data(filter, file_data)
    }

    return response_body


def main():
    filter = capture_filters()
    data = get_data(filter, [])
    save_data(data)


if __name__ == "__main__":
    main()
