# GitHub Trending Dashboard

Dashboard that tracks GitHub Trending repositories using web scraping.

## Features

- Scrape GitHub Trending
- Store historical data
- Analyze repository trends
- Interactive Streamlit dashboard
- Language rankings
- Daily evolution charts

## Installation

```bash
git clone https://github.com/your-user/github-trending-dashboard.git

cd github-trending-dashboard

pip install -r requirements.txt
```

## Run scraper

```bash
python scraper/scrape_trending.py
```

## Run dashboard

```bash
streamlit run dashboard/app.py
```

## Technologies

- Requests
- BeautifulSoup
- Pandas
- Streamlit
- Plotly
