from worldbankapp import app

from flask import render_template
from wrangling_space.getfigures import get_figures
from worldbankapp import app
import json, plotly

figures = get_figures()

# plot ids for the html id tag
ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

# Convert plotly figures to JSON for javascript in html template
figuresJSON = json.dumps(figures, cls = plotly.utils.PlotlyJSONEncoder)

@app.route('/')
@app.route('/index')
def index():
    # return render_template('index.html', data_set = data) -> to send data
    return render_template('index.html', ids = ids, figuresJSON = figuresJSON) # Send figures to HTML template

