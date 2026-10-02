import logging
import os

import psycopg

logger = logging.getLogger(__name__)


def get_connection():

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError("DATABASE_URL não está configurada")

    try:
        connection = psycopg.connect(database_url)
        return connection

    except Exception:
        logger.exception("Falha ao conectar no banco")
        raise
