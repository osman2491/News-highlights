from app import app
import urllib.request,json
from .models import Source

Source = source.Source

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']


def get_source()


    get_source_url = base_url.format(api_key)

    with urllib.request.urlopen(get_source_url) as url
        get_source_data = url.read()
        get_movies_response = json.load(get_source_data)

        source_results = None

        if get_movies_response['sources']:

            source_results_list = get_movies_response['sources']
            source_results = process_sources_results(source_results_list)

    return source_results

def process_sources_results(sources_list):
    '''
    Function that processes the source result and transforms a list of objects
    Args:
        source_list: a list of dictionaries that contain source details
    Returns:
        source_results: A list of source objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')
        name = sources_item.get('name')
        description = sources_item.get('description')

        sources_object = Sources(id,url,category,language,country,name,description)

    return sources_results

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