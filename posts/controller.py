"""
A posts rest api module for ../app (Twitter)

@author: Rakesh Chowdhury (github/CypherpunkSamurai)
"""
# model
from posts.models import Post, add_post, find_posts
from typing import Tuple, List

# nearby in km
RADIUS: int = 5


def new_post_controller(content, location: Tuple[float, float]) -> Post:
    """
    Create a new post object

    :param content:
    :param location:
    :return:
    """

    # create new post
    return add_post(content, location).tojson()


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

    # returns the results
    posts = find_posts(location, radius_km, page, per_page)
    return [post.tojson() for post in posts]
