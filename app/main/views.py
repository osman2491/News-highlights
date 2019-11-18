from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_everything,get_top_headlines
from ..models import 

@main.route('/')
def index():
    '''
    view root page that returns the index and it's data
    '''
    sources = get_sources()
    Everything = get_everything()
    print(Everything)
    print(sources)
    title = 'News articles'

    return render_template('index.html',title=title, sources = sources,Everything = Everything)

