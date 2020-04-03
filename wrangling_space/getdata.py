import pandas as pd

def cleandata(filename, keepcolumns=['Country Name', '1990', '2015'], value_variables=['1990', '2015']):
    """Clean world bank data for a visualizaiton dashboard

    Keeps data range of dates in keep_columns variable and data for the top 10 economies
    Reorients the columns into a year, country and value
    Saves the results to a csv file

    Args:
        dataset (str): name of the csv data file

    Returns:
        None

    """
    df = pd.read_csv(filename, skiprows=4)

    # Keep only the columns of interest (years and country name)
    df = df[keepcolumns]

    top10country = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Brazil',
                    'Italy', 'Canada']
    df = df[df['Country Name'].isin(top10country)]

    # melt year columns  and convert year to date time
    df_melt = df.melt(id_vars='Country Name', value_vars=value_variables)
    df_melt.columns = ['country', 'year', 'variable']
    df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year

    # output clean csv file
    return df_melt
