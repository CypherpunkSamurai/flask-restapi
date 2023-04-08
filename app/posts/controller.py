"""
A posts rest api module for ../app (Twitter)

@author: Rakesh Chowdhury (github/CypherpunkSamurai)
"""
# sql
from app.utils import logger
from sqlalchemy import select, func
# model
from app.posts.models import Post, db
from typing import Tuple, List

# nearby in km
RADIUS: int = 5


def new_post(content, location: Tuple[float, float]) -> Post:
    """
    Create a new post object

    :param content:
    :param location:
    :return:
    """

    # create new post
    post = Post(content, location)
    db.session.add(post)
    db.session.commit()
    return post


def get_post_nearby(location: Tuple[float, float],
                    page: int = 1,
                    per_page: int = 10,
                    radius_km: int = RADIUS) -> List[Post]:
    """
    Fetch posts near the location at a radius

    :param per_page:
    :param page:
    :param location: Tuple(latitude, longitude)
    :param radius_km: Radius in Km (default = 5)

    :return: List of Posts
    """

    results: List[Post] = []

    # format to POINT data type
    pin = f"POINT({location[0]} {location[1]})"
    radius_m = radius_km * 1000

    # write query to find posts with geographical distance within the radius
    # with pagination using `per_page` number of rows
    # at `page * per_page` offset
    query = select(Post).where(
        func.ST_DWithin(Post.location, pin, radius_m)
    ).limit(per_page).offset(page * per_page)

    # run query
    try:
        query_results = db.session.execute(query)
        for row in query_results:
            results.append(row)
    except Exception as e:
        logger.exception(e)
        return []

    # returns the results
    return results
