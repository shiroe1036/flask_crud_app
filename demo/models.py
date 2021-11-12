from index import db 
from sqlalchemy.orm import relationship

class Category(db.Model):
    __tablename__ = 'category'
    
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100))
    
    def __init__(self, category):
        self.category = category
        
    def __repr__(self):
        return '<Category %r>' % self.category

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    coming_out = db.Column(db.Date)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = relationship('Category', back_populates="children")
    
    def __init__(self, name, coming_out, category_id) -> None:
        self.name = name
        self.coming_out = coming_out
        self.category_id = category_id
    
    def __repr__(self):
        return '<Film %r>' % self.name