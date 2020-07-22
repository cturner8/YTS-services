import json


def load_data():
    with open("env.json", encoding="utf8") as json_file:
        data = json.load(json_file)

    return data


def save_data(data):
    with open("out.json", "w") as outfile:
        json.dump(data, outfile, indent=4)


def generate_report(data):
    report = {}
    report["youtube_count"] = 0
    report["youtube_music_count"] = 0
    report["channels"] = {}

    for row in data:
        if (row["header"] == "YouTube"):
            report = process_video(row, report)
        elif (row["header"] == "YouTube Music"):
            report = process_music(row, report)

    return report


def sort_report(report):
    report["channels"] = {k: v for k, v in sorted(report["channels"].items(), key=lambda item: item[1], reverse=True)}

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


def main():
    data = generate_report(load_data())
    data = sort_report(data)
    save_data(data)


if __name__ == "__main__":
    main()
