import urllib.request,json
from .models import Sources,News,Headlines,Category

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


def get_business():
    '''
    function that gets the response to the business json
    '''
    get_business_url = 'https://newsapi.org/v2/everything?q=business&apiKey={}'.format(api_key)
    print(get_business_url)
    with urllib.request.urlopen(get_business_url) as url:
        get_business_data = url.read()
        get_business_response = json.loads(get_business_data)

        get_business_results = None

        if get_business_response['articles']:
            get_business_list = get_business_response['articles']
            get_business_results = process_articles(get_business_list)

    return get_business_results


def get_technology():
    '''
    function that gets the response to the technology json
    '''
    get_technology_url = 'https://newsapi.org/v2/everything?q=technology&apiKey={}'.format(api_key)
    print(get_technology_url)
    with urllib.request.urlopen(get_technology_url) as url:
        get_technology_data = url.read()
        get_technology_response = json.loads(get_technology_data)

        get_technology_results = None

        if get_technology_response['articles']:
            get_technology_list = get_technology_response['articles']
            get_technology_results = process_articles(get_technology_list)

    return get_technology_results


def get_science():
    '''
    function that gets the response to the science json
    '''
    get_science_url = 'https://newsapi.org/v2/everything?q=science&apiKey={}'.format(api_key)
    print(get_science_url)
    with urllib.request.urlopen(get_science_url) as url:
        get_science_data = url.read()
        get_science_response = json.loads(get_science_data)

        get_science_results = None

        if get_science_response['articles']:
            get_science_list = get_science_response['articles']
            get_science_results = process_articles(get_science_list)

    return get_science_results


def get_sports():
    '''
    function that gets the response to the sports json
    '''
    get_sports_url = 'https://newsapi.org/v2/everything?q=sports&apiKey={}'.format(api_key)
    print(get_sports_url)
    with urllib.request.urlopen(get_sports_url) as url:
        get_sports_data = url.read()
        get_sports_response = json.loads(get_sports_data)

        get_sports_results = None

        if get_sports_response['articles']:
            get_sports_list = get_sports_response['articles']
            get_sports_results = process_articles(get_sports_list)

    return get_sports_results

def get_entertainment():
    '''
    function that gets the response to the entertainment json
    '''
    get_entertainment_url = 'https://newsapi.org/v2/everything?q=entertainment&apiKey={}'.format(api_key)
    print(get_entertainment_url)
    with urllib.request.urlopen(get_entertainment_url) as url:
        get_entertainment_data = url.read()
        get_entertainment_response = json.loads(get_entertainment_data)

        get_entertainment_results = None

        if get_entertainment_response['articles']:
            get_entertainment_list = get_entertainment_response['articles']
            get_entertainment_results = process_articles(get_entertainment_list)

    return get_entertainment_results