from config import *

from flask import request, url_for, redirect, render_template
from os import path

from model.post import *


@app.route('/saveImage', methods=['GET', 'POST'])
def saveImageFoo():
    file = request.files.get('file')
    try:
        file.save(path.join(app.static_folder, 'files', 'img.jpg'))
    except:
        pass
    return redirect(url_for('getMainTest'))

@cross_origin
@app.route('/search', methods=['GET', 'POST', 'OPTIONS'])
def search():
    rawTargets = request.form.get('targets')
    targets = rawTargets.split(' ')
    result = []
    posts = Post.getAll()
    for post in posts:
        if min(list(map(lambda x: x in post.info or x in post.title, targets))):
            result.append(post)
    print('search finished')
    return render_template('news.html',  title=f'Результаты по запросу "{rawTargets}"', posts=result)
            
    
    