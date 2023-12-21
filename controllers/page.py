from config import *

from flask import request, url_for, redirect, render_template
from os import path
from model.post import *

@app.route('/saveFile', methods=['GET'])
def getMainTest():
    
    return render_template('fileSave.html', img='files/img.jpg', )

@app.route('/newPost', methods=['GET'])
def getNewPost():
    return render_template('newPost.html')

@app.route('/main', methods=['GET'])
def getMain():
    posts = Post.getAll()
    posts.reverse()
    return render_template('main.html', posts=posts)

@app.route('/news', methods=['GET'])
def getNews():
    posts = Post.getAll()
    posts.reverse()
    return render_template('news.html', title='Новости', posts=posts)


@app.route('/contacts', methods=['GET'])
def getContacts():
    return render_template('contacts.html')