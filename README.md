# GitHub Trending Dashboard

Dashboard that tracks GitHub Trending repositories using web scraping.

## Preview
<p align="center">
  <img src="[LINK_DIRECTO_A_LA_IMAGEN_1]" width="45%"> &nbsp; <img src="[LINK_DIRECTO_A_LA_IMAGEN_2]" width="45%">
  <br>
  <img src="[LINK_DIRECTO_A_LA_IMAGEN_3]" width="45%"> &nbsp; <img src="[LINK_DIRECTO_A_LA_IMAGEN_4]" width="45%">
  <br>
  <img src="[LINK_DIRECTO_A_LA_IMAGEN_5]" width="91%">
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
