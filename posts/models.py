# file ./app/posts/models.py
# sql
from abc import ABC

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, select, String
from sqlalchemy.types import UserDefinedType
# model
from typing import Tuple
from datetime import datetime
# utils
from utils import logger
from ast import literal_eval as make_tuple

db = SQLAlchemy()


class PointType(UserDefinedType, ABC):
    """
    Postgre POINT type
    """
    cache_ok = True

    x: float
    y: float

    def __init__(self, x: float = 0, y: float = 0):
        self.precision = 32
        self.x = x
        self.y = y

    def get_col_spec(self, **kw):
        return "POINT"


class Post(db.Model):
    """
    A Post Object Model
    """

    __tablename__ = 'posts'
    serialize_only = ('id', 'timestamp', 'content', 'location')

    # columns
    id: int = db.Column(db.Integer, primary_key=True)
    timestamp: int = db.Column(db.DateTime, default=datetime.utcnow())
    content: str = db.Column(db.String(280))

    # use point type for location (lat, lon)
    location = db.Column(PointType())

    def __init__(self, post_content: str, location: Tuple[float, float]):
        """
        Create a new post from id and content

        :param post_content: Content of the post
        :param location: Location of the post
        """
        self.content = post_content
        # i have not used point type here as im unaware how to adapt it to the query
        self.location = f"{location}"

    def __repr__(self):
        return f"<User {self.id}>"

    def tojson(self):
        """
        Serialize the Post

        :return:
        """
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "content": self.content,
            "location": {
                # convert the tuple in string format to a python tuple
                "lat": make_tuple(self.location)[0],
                "lon": make_tuple(self.location)[1]
            }
        }


def add_post(content: str, location: Tuple[float, float]) -> Post:
    """
    Add a post to table

    :param content:
    :param location:
    :return:
    """
    post = Post(content, location)
    db.session.add(post)
    db.session.commit()
    return post


def find_posts(
        location: Tuple[float, float],
        radius_km: int,
        page: int,
        per_page: int
) -> [Post]:
    """
    Nearby posts

    :param location:
    :param radius_km:
    :param page:
    :param per_page:
    :return:
    """

    page -= 1
    results: [Post] = []

    # format to POINT data type
    pin = f"{location}"

    # we use our custom defined "WithinRadius" function here
    # sqlalchemy creates the sql query for the function automatically writtem func.(name)
    # with pagination using `per_page` number of rows
    # at `page * per_page` offset
    query = select(Post).where(
        func.WithinRadius(Post.location, pin, radius_km)
    ).limit(per_page).offset(page * per_page)

    # run query
    try:
        query_results = db.session.execute(query)
        for row, in query_results:
            results.append(row)
    except Exception as e:
        logger.exception(e)

    return results
