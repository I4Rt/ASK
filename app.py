from config import *
from model.post import *
from model.image import *
from model.author import *
from controllers.page import *
from controllers.forms import *
from controllers.rest import *


if __name__ == "__main__":
    print('App is running')
    with app.app_context():
        # cors.init_app(app)
        db.create_all()
        # post1 = Post('test1', 'testing the post sys')
        # image = Image(data='hexhex2', post=post1)
        
        # # post1.save()
        # # image.save()
        
        # print(Image.getAll()[1].post_id)
        app.run(host='0.0.0.0', port=3030, debug=True)