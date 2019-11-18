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