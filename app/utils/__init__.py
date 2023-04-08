import os
import logging

# app config
IS_DEBUG = os.getenv("DEBUG", 0)
POSTGRESQL_URI = os.getenv("POSTGRES_URL", None)

# logging config
logging.basicConfig(
    level=logging.DEBUG if IS_DEBUG else logging.INFO
)
# logger
logger = logging.Logger("app")
