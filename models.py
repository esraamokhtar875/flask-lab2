from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description= db.Column(db.String(300))
    image = db.Column(db.String(200))



    # def __str__ (self):
    #     return f"{self.name}"
    #
    # @property
    # def image_url(self):
    #     return url_for('static', filename=f"posts/images/{self.image}")





