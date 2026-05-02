import pandas as pd
import os
import streamlit as st

# Map each year's messy column names → standard names
COLUMN_MAP = {
    # 2015 / 2016 style
    "country":                        "country",
    "happiness score":                "life_ladder",
    "happiness.score":                "life_ladder",
    "economy (gdp per capita)":       "gdp_per_capita",
    "economy..gdp.per.capita.":       "gdp_per_capita",
    "health (life expectancy)":       "health",
    "health..life.expectancy.":       "health",
    "freedom":                        "freedom",
    "trust (government corruption)":  "corruption",
    "trust..government.corruption.":  "corruption",
    "generosity":                     "generosity",
    "family":                         "social_support",

    # 2017 style
    "happiness.score":                "life_ladder",
    "economy..gdp.per.capita.":       "gdp_per_capita",
    "health..life.expectancy.":       "health",
    "freedom.to.make.life.choices":   "freedom",
    "trust..government.corruption.":  "corruption",

    # 2018 / 2019 style
    "country or region":              "country",
    "score":                          "life_ladder",
    "gdp per capita":                 "gdp_per_capita",
    "social support":                 "social_support",
    "healthy life expectancy":        "health",
    "freedom to make life choices":   "freedom",
    "perceptions of corruption":      "corruption",
    
    
    "lower confidence interval" : "lower_ci",
    "upper confidence interval" : "upper_ci",
}

KEEP_COLS = ["country", "year", "life_ladder", "gdp_per_capita",
             "social_support", "health", "freedom", "generosity", "corruption","lower_ci","upper_ci"]

@st.cache_data
def load_data():
    frames = []
    data_dir = "data"

    for year in range(2015, 2020):
        path = os.path.join(data_dir, f"{year}.csv")
        if not os.path.exists(path):
            continue

        df = pd.read_csv(path)

        # Normalize column names for mapping
        df.columns = df.columns.str.strip().str.lower()
        df = df.rename(columns=COLUMN_MAP)

        df["year"] = year

        # Keep only the columns we care about (ignore missing ones)
        cols = [c for c in KEEP_COLS if c in df.columns]
        df = df[cols]

        frames.append(df)

    combined = pd.concat(frames, ignore_index=True)
    return combined