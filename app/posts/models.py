# file ./app/posts/models.py
# sql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, select
from sqlalchemy.types import UserDefinedType
# model
from typing import Tuple
from datetime import datetime

from app.utils import logger

db = SQLAlchemy()


class PointType(UserDefinedType):
    def get_col_spec(self):
        return "POINT"

    def bind_expression(self, bindvalue):
        return func.ST_GeomFromText(bindvalue, type_=self)

    def column_expression(self, col):
        return func.ST_AsText(col, type_=self)


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
    location = db.Column(PointType())

    def __init__(self, post_content: str, location: Tuple[float, float]):
        """
        Create a new post from id and content

        :param post_content: Content of the post
        :param location: Location of the post
        """
        self.content = post_content
        self.location = f"POINT{location}"


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

    results: [Post] = []

    # format to POINT data type
    pin = f"({location[0]} {location[1]})"

    # write query to find posts with geographical distance within the radius
    # with pagination using `per_page` number of rows
    # at `page * per_page` offset
    query = select(Post).where(
        func.ST_DWithin(Post.location, pin, radius_km)
    ).limit(per_page).offset(page * per_page)

    # run query
    try:
        query_results = db.session.execute(query)
        for row in query_results:
            results.append(row)
    except Exception as e:
        logger.exception(e)

    return results
