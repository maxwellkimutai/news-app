import urllib.request,json
from .models import Source,Article
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

Source = Source

Article = Article

api_key = None

news_sources_url = None

articles_url = None

def configure_request(app):
    global api_key,news_sources_url,articles_url
    #Getting api key
    api_key = app.config['NEWS_API_KEY']

    news_sources_url = app.config["NEWS_SOURCES_API_BASE_URL"]

    articles_url = app.config["SPECIFIC_SOURCE_API_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = news_sources_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_source_results(source_results_list)

    return source_results

def process_source_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')
        language = source_item.get('language')

        source_object = Source(id,name,description,category,language)
        source_results.append(source_object)

    return source_results

def get_articles(source_id):
    '''
    Function that gets the json response to our url request for a specific source
    '''
    get_articles_url = articles_url.format(source_id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_list)

    return articles_results
