import pandas as pd

def clean(df: pd.DataFrame) -> pd.DataFrame:
    df["year"] = df["year"].astype(int)
    df["country"] = df["country"].str.strip()

    # Drop rows missing the key score
    df = df.dropna(subset=["country", "life_ladder"])

    # Round numeric columns
    numeric_cols = ["life_ladder", "gdp_per_capita", "social_support",
                    "health", "freedom", "generosity", "corruption"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").round(3)

    return df