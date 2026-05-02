# World Happiness Dashboard

An interactive multi-page web dashboard that visualises World Happiness Report data from 2015 to 2019.

## Features

- **Overview** — choropleth world map with year slider and top/bottom 10 country rankings
- **Compare** — side-by-side bar chart comparison of two countries across any metric
- **Trends** *(coming soon)*
- **Correlations** *(coming soon)*

## Tech Stack

- Python
- Streamlit
- Plotly
- Pandas

## Installation

1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd happiness-dashboard
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the App

```
streamlit run app.py
```

Then open your browser at `http://localhost:8501`.

## Project Structure

```
happiness-dashboard/
├── data/               # CSV files (2015–2019)
├── src/
│   ├── load_data.py    # Loads and combines CSV files
│   ├── clean_data.py   # Cleans and standardises the data
│   └── analysis.py     # Data filtering and metric calculations
├── pages/
│   ├── overview.py     # World map and rankings
│   ├── compare.py      # Country comparison
│   ├── trends.py
│   └── correlations.py
├── app.py              # Entry point
└── requirements.txt
```

## Data

World Happiness Report data (2015–2019). Metrics include happiness score, GDP per capita, social support, health, freedom, generosity, and corruption perception.
