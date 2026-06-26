# GitHub Trending Dashboard

Dashboard that tracks GitHub Trending repositories using web scraping.

## Preview
<p align="center">
  <img src="https://i.imgur.com/gjg5teJ.png" width="45%"> &nbsp; <img src="https://i.imgur.com/W6cHHBQ.png" width="45%">
  <br>
  <img src="https://i.imgur.com/cyF7M7W.png" width="45%"> &nbsp; <img src="https://i.imgur.com/ZAt8Thw.png" width="45%">
  <br>
  <img src="https://i.imgur.com/VgrmM7a.png" width="91%">
</p>

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
