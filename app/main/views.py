from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quotes

@main.route('/')
def index():
    title='E-Blogs'
    random_quotes=get_quotes()


    return render_template('index.html', title=title, quotes=random_quotes)