from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting all news
    everything_news = get_news('everything')
    title = 'Home - The Daily Planet '
    return render_template('index.html', title=title, everything = everything_news)