# file ./app/posts/models.py
# sql
from flask_sqlalchemy import SQLAlchemy
# model
from typing import Tuple
from geoalchemy2 import Geography
from datetime import datetime

db = SQLAlchemy()


class Post(db.Model):
    """
    A Post Object Model
    """

    __tablename__ = 'posts'

    # columns
    id: int = db.Column(db.Integer, primary_key=True)
    timestamp: int = db.Column(db.DateTime, default=datetime.utcnow())
    content: str = db.Column(db.String(280))

    # use point type for location (lat, lon)
    # 4326 tells the geoalchemy2 module we want spacial geographic points on earth
    # postgis reference: http://postgis.net/workshops/postgis-intro/geography.html
    location = db.Column(Geography(geometry_type='POINT', srid=4326))

    def __init__(self, post_content: str, location: Tuple[float, float]):
        """
        Create a new post from id and content

        :param post_content: Content of the post
        :param location: Location of the post
        """
        self.content = post_content
        self.location = f"POINT{location}"
