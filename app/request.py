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
