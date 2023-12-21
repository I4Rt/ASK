from model.BaseData import *

class Author(db.Model, BaseData):
    name = db.Column(db.Text, unique=False)
    info = db.Column(db.Text, unique=False)
    
    def __init__(self, name:str, info:str):
        self.name = name
        self.info = info
        db.Model.__init__(self)
        BaseData.__init__(self, self.id)