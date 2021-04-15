class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,articles,source,author,title,description,url,urlToImage,publishedAt,content):
        self.articles =articles
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content