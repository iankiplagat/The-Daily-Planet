from flask import render_template
from . import main
from ..requests import get_news,get_headlines,get_business,get_technology,get_science,get_sports,get_entertainment
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

@main.route('/business')
def business():

    '''
    
    '''
    business = get_business()
    title = 'Business News'

    return render_template('business.html', title = title, business = business)

@main.route('/technology')
def technology():

    '''
    
    '''
    technology = get_technology()
    title = 'Technology News'

    return render_template('technology.html', title = title, technology = technology)

@main.route('/science')
def science():

    '''
    
    '''
    science = get_science()
    title = 'Science News'

    return render_template('science.html', title = title, science = science)

@main.route('/sports')
def sports():

    '''
    
    '''
    sports = get_sports()
    title = 'Sports News'

    return render_template('sports.html', title = title, sports = sports)

@main.route('/entertainment')
def entertainment():

    '''
    
    '''
    entertainment = get_entertainment()
    title = 'Entertainment News'

    return render_template('entertainment.html', title = title, entertainment = entertainment)