from flask import render_template
from . import main
from ..requests import get_news,get_headlines
# ,get_news_sources

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    # Getting all news and sources
    
    # sources = get_news_sources('id')
    articles_news = get_news('articles')
   
    title = 'The Daily Planet'
    
    return render_template('index.html', title=title, articles = articles_news)

@main.route('/headlines')
def headlines():

    '''
    
    '''
    headlines = get_headlines()
    title = 'Top News'

    return render_template('headlines.html', title = title, headlines = headlines)