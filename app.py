######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *


####### Set up your app #####
app = dash.Dash(__name__)
server = app.server
app.title='Cereal!'
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

###### Import a dataframe #######
df = pd.read_csv("https://raw.githubusercontent.com/MelK44/basic-dash-pandas/master/all_cereals.csv")

colors_list=[['Apple Jacks',
  'Cinnamon Toast Crunch',
  'Froot Loops',
  'Frosted Flakes',
  'Lucky Charms',
  'Quaker Oat Squares',
  'Special K',
  '100% Bran',
  '100% Natural Bran',
  'All-Bran',
  'All-Bran with Extra Fiber',
  'Almond Delight',
  'Apple Cinnamon Cheerios',
  'Basic 4',
  'Bran Chex',
  'Bran Flakes',
  "Cap'n'Crunch",
  'Cheerios',
  'Clusters',
  'Cocoa Puffs',
  'Corn Chex',
  'Corn Flakes',
  'Corn Pops',
  'Count Chocula',
  "Cracklin' Oat Bran",
  'Cream of Wheat (Quick)',
  'Crispix',
  'Crispy Wheat & Raisins',
  'Double Chex',
  'Frosted Mini-Wheats',
  'Fruit & Fibre Dates; Walnuts; and Oats',
  'Fruitful Bran',
  'Fruity Pebbles',
  'Golden Crisp',
  'Golden Grahams',
  'Grape Nuts Flakes',
  'Grape-Nuts',
  'Great Grains Pecan',
  'Honey Graham Ohs',
  'Honey Nut Cheerios',
  'Honey-comb',
  'Just Right Crunchy  Nuggets',
  'Just Right Fruit & Nut',
  'Kix',
  'Life',
  'Maypo',
  'Muesli Raisins; Dates; & Almonds',
  'Muesli Raisins; Peaches; & Pecans',
  'Mueslix Crispy Blend',
  'Multi-Grain Cheerios',
  'Nut&Honey Crunch',
  'Nutri-Grain Almond-Raisin',
  'Nutri-grain Wheat',
  'Oatmeal Raisin Crisp',
  'Post Nat. Raisin Bran',
  'Product 19',
  'Puffed Rice',
  'Puffed Wheat',
  'Quaker Oatmeal',
  'Raisin Bran',
  'Raisin Nut Bran',
  'Raisin Squares',
  'Rice Chex',
  'Rice Krispies',
  'Shredded Wheat',
  "Shredded Wheat 'n'Bran",
  'Shredded Wheat spoon size',
  'Smacks',
  'Strawberry Fruit Wheats',
  'Total Corn Flakes',
  'Total Raisin Bran',
  'Total Whole Grain',
  'Triples',
  'Trix',
  'Wheat Chex',
  'Wheaties',
  'Wheaties Honey Gold']]




####### Layout of the app ########
app.layout = html.Div([
    html.H3('Choose a Cereal:'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in colors_list],
        value=colors_list[0]
    ),
    html.Br(),
    dcc.Graph(id='display-value')
])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('display-value', 'figure'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(user_input):
    results = df.groupby(user_input)[['calories','fiber','fat','sugars','vitamins','cups']].mean()
    mydata = [go.Bar(x = results.index,
                     y = results.values,
                     marker = dict(color='purple'))]
    mylayout = go.Layout(title = 'How does your cereal stack up?',
                         xaxis = dict(title='this is my x-axis'),
                         yaxis = dict(title='this is my y-axis'))
    myfig = go.Figure(data=mydata, layout=mylayout)
    return myfig


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
