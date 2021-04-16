from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
apikey = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_news(articles):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(articles,apikey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_articles = None

        if get_news_response['articles']:
           news_articles_list = get_news_response['articles']
           news_articles = process_articles(news_articles_list)


    return news_articles
  
def process_articles(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_articles: A list of news objects
    '''
    news_articles = []
    for news_item in news_list:
        source = news_item.get('source.name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if urlToImage:
            news_object = News(source,author,title,description,url,urlToImage,publishedAt,content)
            news_articles.append(news_object)

    return news_articles

def get_articles(title):
    get_articles_details_url = base_url.format(title,apikey)

    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_object = None
        if articles_details_response:
            source = articles_details_response.get('source')
            author = articles_details_response.get('author')
            title = articles_details_response.get('title')
            description = articles_details_response.get('description')
            url = articles_details_response.get('url')
            urlToImage = articles_details_response.get('urlToImage')
            publishedAt = articles_details_response.get('publishedAt')
            content = articles_details_response.get('content')

            articles_object = News(source,author,title,description,url,urlToImage,publishedAt,content)

    return articles_object

def articles_source(title):
    articles_source_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(title,api_key)
    print(articles_source_url)
    with urllib.request.urlopen(articles_source_url) as url:
        articles_source_data = url.read()
        articles_source_response = json.loads(articles_source_data)

        articles_source_results = None

        if articles_source_response['articles']:
            articles_source_list = articles_source_response['articles']
            articles_source_results = process_articless_results(articles_source_list)


    return articles_source_results

def process_articles_results(news):
    '''
    function that processes the json files of articless from the api key
    '''
    articles_source_results = []
    for articles in news:
        author = articles.get('author')
        description = articles.get('description')
        time = articles.get('publishedAt')
        url = articles.get('urlToImage')
        image = articles.get('url')
        title = articles.get ('title')

        if url:
            articles_objects = News(author,description,time,image,url,title)
            articles_source_results.append(articles_objects)

    return articles_source_results
