# file: ./app/posts/route.py
from utils import logger
from flask import Blueprint, request

from posts.controller import get_post_nearby, new_post_controller

# namespace
ROUTE_NAMESPACE = 'posts'
# Blueprints for /posts
b_get_post = Blueprint('get_post', ROUTE_NAMESPACE)
b_new_post = Blueprint('new_post', ROUTE_NAMESPACE)


@b_get_post.route('/posts/get', methods=['GET'])
def get_post():
    """
    Get a post by post_id

    :return:
    """

    # read params
    args = request.args

    # required params
    lat = args.get("lat", type=float, default=None)
    lon = args.get("lon", type=float, default=None)
    distance = args.get("distance", type=int, default=5)
    if lat is None or lon is None:
        return {"error": "query parameters lat and lon are required to fetch posts"}

    # optional params
    per_page = args.get('per_page', default=10, type=int)
    page = args.get('page', default=1, type=int)

    # get posts
    try:
        logger.info(f"get_post_nearby ->")
        posts = get_post_nearby(
            (lat, lon),
            page,
            per_page,
            distance
        )
    except Exception as e:
        logger.exception(e)
        return {"result": "error", "message": f"there was a error querying posts. {e}"}

    return {"result": "success", "posts": posts}


@b_new_post.route('/posts/new', methods=['POST'])
def new_post():
    """
    Create a new post from current user

    :return: New Post ID
    """
    try:
        # read json
        data = request.get_json()

        # check missing json keys
        if not any(key in data for key in ["content", "lat", "lon"]):
            return {"result": "error", "message": "content, lat, and lon are required to create new post"}

        content = data["content"]
        lat = data["lat"]
        lon = data["lon"]

        post = new_post_controller(
            content,
            (lat, lon)
        )
        return {"result": "success", "message": "post created", "posts": [post]}
    except Exception as e:
        logger.exception(e)
        return {"result": "error", "message": f"error creating post. {e}"}
