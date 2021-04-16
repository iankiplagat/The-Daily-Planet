from flask import render_template
from app import app
from .request import get_news,get_articles

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

@app.route('/articles/<title>')
def articles(title):

    '''
    View articles page function that returns the articles details page and its data
    '''
    articles = get_articles(title)
    title = f'{articles.title}'

    return render_template('articles.html',title = title,articles = articles)