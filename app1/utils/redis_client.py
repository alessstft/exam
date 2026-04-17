import redis

from app1.core.config import REDIS_URL


def get_redis_client():
    try:
        client = redis.Redis.from_url(REDIS_URL, decode_responses=True)
        client.ping()
        return client
    except Exception:
        return None


redis_client = get_redis_client()
