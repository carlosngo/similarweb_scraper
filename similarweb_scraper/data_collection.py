import re
import json
import pandas as pd
from pathlib import Path
from data_cleaning import clean_data


def collect_data():
    scraped_html_file_names = [
        "similarweb-byte-trading-com.html",
        "similarweb-crunchbase-com.html",
        "similarweb-google-com.html",
        "similarweb-pitchbook-com.html",
        "similarweb-stripe-com.html",
    ]

    data = []

    for file_name in scraped_html_file_names:
        file_path = Path("similarweb-scrapes") / file_name
        with file_path.open("r", encoding="utf-8") as html_file:
            row = extract_data(html_file.read())
            row = clean_data(row)
            data.append(row)

    return pd.DataFrame(data)


def extract_data(html_string):
    matches = re.search("__APP_DATA__ = ({.*})", html_string)
    app_data_json_string = matches.group(1)
    return json.loads(app_data_json_string)["layout"]["data"]
