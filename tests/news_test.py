import unittest
from app.models import News,Sources,Headlines,Category

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.source_sources = Sources(0,'Dartmouth College','Helen Sharpe','Dartmouth Honor Class','Kiplagat','','')

    def test_instance(self):
        self.assertTrue(isinstance(self.source_source,Sources))

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('Ian joins The Dartmouth honor class','Dartmouth College','Helen Sharpe','Dartmouth Honor Class','Kiplagat','','https://image.newsapi.org/v2/everything',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
        
        
class HeadlinesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Headlines class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.headline_headlines = Headlines('Ian joins The Dartmouth honor class','Dartmouth College','Helen Sharpe','Dartmouth Honor Class','Kiplagat','')

    def test_instance(self):
        self.assertTrue(isinstance(self.headline_headlines,Headlines))        
    
    
class CategoryTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Category class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.category_category = Category('Ian joins The Dartmouth honor class','Dartmouth College','Helen Sharpe','Dartmouth Honor Class','Kiplagat','')

    def test_instance(self):
        self.assertTrue(isinstance(self.category_category,Category))            
        
        
