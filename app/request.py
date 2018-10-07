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
