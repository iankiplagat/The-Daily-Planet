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
    articles_news = get_news('articles')
    print(articles_news)
    title = 'Home - The Daily Planet '
    return render_template('index.html', title=title, articles = articles_news)