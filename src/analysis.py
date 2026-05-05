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

def get_country_trends(country,df):
    """
    compares a metric from the selected country across years 2015-2019

    Args:
        country : selected country
        df : panda dataframe of all metrics of selected country 
    returns : filtered country with all metrics 
    """
    
    
    filtered_result = df[df["country"] == country]
    return filtered_result
    