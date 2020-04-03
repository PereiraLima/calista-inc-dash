import pandas as pd
import plotly.graph_objs as go
from .getdata import cleandata

# TODO: Scroll down to line 157 and set up a fifth visualization for the data dashboard



def get_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies
    # as a line chart

    graph_one = []
    df = cleandata('data/data1.csv')
    df.columns = ['country', 'year', 'hectaresarablelandperperson']
    df.sort_values('hectaresarablelandperperson', ascending=False, inplace=True)
    countrylist = df.country.unique().tolist()

    for country in countrylist:
        x_val = df[df['country'] == country].year.tolist()
        y_val = df[df['country'] == country].hectaresarablelandperperson.tolist()
        graph_one.append(
            go.Scatter(
                x=x_val,
                y=y_val,
                mode='lines',
                name=country
            )
        )

    layout_one = dict(title='Change in Hectares Arable Land <br> per Person 1990 to 2015',
                      xaxis=dict(title='Year',
                                 autotick=False, tick0=1990, dtick=25),
                      yaxis=dict(title='Hectares'),
                      )

    # second chart plots ararble land for 2015 as a bar chart
    graph_two = []
    df = cleandata('data/data2.csv')
    df.columns = ['country', 'year', 'hectaresarablelandperperson']
    df.sort_values('hectaresarablelandperperson', ascending=False, inplace=True)
    df = df[df['year'] == 2015]

    graph_two.append(
        go.Bar(
            x=df.country.tolist(),
            y=df.hectaresarablelandperperson.tolist(),
        )
    )

    layout_two = dict(title='Hectares Arable Land per Person in 2015',
                      xaxis=dict(title='Country', ),
                      yaxis=dict(title='Hectares per person'),
                      )

    # third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    df = cleandata('data/data2.csv')
    df.columns = ['country', 'year', 'percentrural']
    df.sort_values('percentrural', ascending=False, inplace=True)
    for country in countrylist:
        x_val = df[df['country'] == country].year.tolist()
        y_val = df[df['country'] == country].percentrural.tolist()
        graph_three.append(
            go.Scatter(
                x=x_val,
                y=y_val,
                mode='lines',
                name=country
            )
        )

    layout_three = dict(title='Change in Rural Population <br> (Percent of Total Population)',
                        xaxis=dict(title='Year',
                                   autotick=False, tick0=1990, dtick=25),
                        yaxis=dict(title='Percent'),
                        )

    # fourth chart shows rural population vs arable land
    graph_four = []

    valuevariables = [str(x) for x in range(1995, 2016)]
    keepcolumns = [str(x) for x in range(1995, 2016)]
    keepcolumns.insert(0, 'Country Name')

    df_one = cleandata('data/data2.csv', keepcolumns, valuevariables)
    df_two = cleandata('data/data3.csv', keepcolumns, valuevariables)

    df_one.columns = ['country', 'year', 'variable']
    df_two.columns = ['country', 'year', 'variable']

    df = df_one.merge(df_two, on=['country', 'year'])

    for country in countrylist:
        x_val = df[df['country'] == country].variable_x.tolist()
        y_val = df[df['country'] == country].variable_y.tolist()
        year = df[df['country'] == country].year.tolist()
        country_label = df[df['country'] == country].country.tolist()

        text = []
        for country, year in zip(country_label, year):
            text.append(str(country) + ' ' + str(year))

        graph_four.append(
            go.Scatter(
                x=x_val,
                y=y_val,
                mode='markers',
                text=text,
                name=country,
                textposition='top center'
            )
        )

    layout_four = dict(title='Rural Population versus <br> Forested Area (Square Km) 1990-2015',
                       xaxis=dict(title='Rural Population'),
                       yaxis=dict(title='Forest Area (square km)'),
                       )

    # TODO: Make a fifth chart from the data in API_SP.RUR.TOTL_DS2_en_csv_v2_9914824.csv
    # This csv file contains data about the total rural population for various countries over many years
    # Make a bar chart showing the rural population of these countries ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Brazil', 'Italy', 'Canada'] in the year 2015.
    graph_five = []
    df_five = cleandata('data/data3.csv')
    country = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Brazil', 'Italy', 'Canada']
    df_five = df_five[df_five.country.isin(country)]
    df_five = df_five[df_five.year == 2015]

    graph_five.append(go.Bar(
        x = df_five.country,
        y = df_five.variable,
    ))

    layout_five = dict(title='Rural Population in 2015',
                       xaxis=dict(title='Country'),
                       yaxis=dict(title='Population'),
                       )






    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    figures.append(dict(data=graph_five, layout=layout_five))


    return figures