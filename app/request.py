from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_API_BASE_URL"]


def get_top_headlines(sources) :
    get_top_headlines_url = headlines_url.format(sources, api_key)

    with urllib.request.urlopen(get_top_headlines_url) as url :
        top_headlines_data = url.read()
        top_headlines_response = json.loads(top_headlines_data)

        top_headlines_results = None 

        if top_headlines_response['top_headlines'] :
            top_headlines_results_list = top_headlines_response['top_headlines']
            top_headlines_results = process_top_headlines_results(top_headlines_results_list)

    return(top_headlines_results)

def process_top_headlines_results(top_headlines_results_list) :
    '''
    process Top_headlines results and transforms a list of objects
    '''
    top_headlines_results = []
    for top_headlines_item in top_headlines_results_list:

        author = top_headlines_item.get('author')
        title = top_headlines_item.get('title')
        description = top_headlines_item.get('description')
        url = top_headlines_item.get('url')
        urlToImage = top_headlines_item.get('urlToImage')
        publishedAt = top_headlines_item.get('publishedAt')
        content = top_headlines_item.get('content')

        top_headlines_object = Top_Headlines(author, title, description, url, urlToImage, publishedAt, content)
        top_headlines_results.append(top_headlines_object)

    return top_headlines_results