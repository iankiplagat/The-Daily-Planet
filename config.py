import os

class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey={}'
    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?sources=bbc-news,al-jazeera-english,cnn,independent,google-news,the-telegraph,the-lad-bible,bloomberg,engadget,espn,fortune&language=en&sortBy=publishedAt&pageSize={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
    


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}    