import urllib.request,json
from .models import Sources,News,Headlines

# Getting api key
api_key = None
# Getting the news base url
base_url = None
# Getting the news source url
source_url= None

def configure_request(app):
    global api_key,base_url,source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    source_url= app.config['SOURCE_API_BASE_URL']


def get_news(articles):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(articles,api_key)

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


def get_news_sources(id):
    
    '''
    Function that gets the json response to our url request
    '''
    get_news_sources_url = source_url.format(id,api_key)
    
    with urllib.request.urlopen(get_news_sources_url) as url:
        get_news_sources_data = url.read()
        get_news_sources_response = json.loads(get_news_sources_data)
        
        news_sources_results = None
        
        if get_news_sources_response['id']:
            news_sources_results_list = get_news_sources_response['id']
            news_sources_results = process_results(news_sources_results_list)
 
    return news_sources_results


def process_results(news_sources_list):
    '''
    Function that processes the json results
    '''
    news_sources_results = []
    for source in news_sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        country = source.get('country')
        if url:
            news_source_object = Sources(id,name,description,url,category,country)
            news_sources_results.append(news_source_object)
    
    return news_sources_results


def get_headlines():
    '''
    function that gets the response to the category json
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news,al-jazeera-english,cnn,independent,google-news,the-telegraph,mashable,the-lad-bible,bloomberg,engadget,espn,fortune&sortBy=publishedAt&apiKey={}'.format(api_key)
    print(get_headlines_url)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        get_headlines_results = None

        if get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            get_headlines_results = process_articles(get_headlines_list)

    return get_headlines_results