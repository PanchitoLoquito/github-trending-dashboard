import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
from datetime import datetime

URL = "https://github.com/trending"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/122.0 Safari/537.36"
    )
}

DATA_FOLDER = Path("data")
DATA_FOLDER.mkdir(exist_ok=True)

CSV_FILE = DATA_FOLDER / "trending.csv"


def clean_number(value):
    if not value:
        return 0

    value = value.strip().replace(",", "")

    try:
        return int(value)
    except ValueError:
        return 0


def get_trending_repositories():
    response = requests.get(
        URL,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    repositories = []

    repos = soup.find_all(
        "article",
        class_="Box-row"
    )

    for repo in repos:

        name = (
            repo.h2.text
            .strip()
            .replace("\n", "")
            .replace(" ", "")
        )

        description_tag = repo.find("p")

        description = (
            description_tag.text.strip()
            if description_tag
            else ""
        )

        language_tag = repo.find(
            "span",
            itemprop="programmingLanguage"
        )

        language = (
            language_tag.text.strip()
            if language_tag
            else "Unknown"
        )

        stars_tag = repo.find(
            "a",
            href=lambda x: x and x.endswith(
                "/stargazers"
            )
        )

        forks_tag = repo.find(
            "a",
            href=lambda x: x and x.endswith(
                "/forks"
            )
        )

        stars = clean_number(
            stars_tag.text if stars_tag else "0"
        )

        forks = clean_number(
            forks_tag.text if forks_tag else "0"
        )

        repositories.append(
            {
                "date": datetime.now().date(),
                "repository": name,
                "description": description,
                "language": language,
                "stars": stars,
                "forks": forks,
            }
        )

    return pd.DataFrame(repositories)


def save_data(df):
    if CSV_FILE.exists():

        old_df = pd.read_csv(CSV_FILE)

        df = pd.concat(
            [old_df, df],
            ignore_index=True
        )

        df = df.drop_duplicates(
            subset=["date", "repository"]
        )

    df.to_csv(
        CSV_FILE,
        index=False
    )

    print(
        f"Saved {len(df)} records "
        f"to {CSV_FILE}"
    )


if __name__ == "__main__":
    data = get_trending_repositories()
    save_data(data)