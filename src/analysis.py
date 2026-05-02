#  # Stats & computed metrics



def get_country_data(country1,country2,year,df):
    """
    Compares different metrics (GDP, Freedom, life expectency etc ) 
    between two selected country in a certain year
    
    Args: 
        country1 & country2 : countries to compare
        year: selected year
        df:  a pandas DataFrame containing the cleaned happiness data
    
    return: the filtered dataframe based on selected year and selected countries
    """
    filtered_result = df[(df["year"] == year) & (df["country"].isin([country1,country2]))]
    
    return filtered_result