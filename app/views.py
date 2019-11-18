from flask import render_template
from app import app

# Views
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best  news Website Online'
    return render_template('index.html', title = title)
@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View movie page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)