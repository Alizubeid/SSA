from redis import Redis, exceptions
from dotenv import load_dotenv
from os import getenv

load_dotenv()

class RedisManager:
    def __init__(self, host="redis", port=6379, password=None):
        self.host = host
        self.port = port
        self.password = password

    def __enter__(self):
        try:
            self.connection = Redis(
                host=self.host,
                port=self.port,
                password=self.password,
            )
            Redis()
            return self
        except exceptions.AuthenticationError:
            self.connection.close()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()


CACHE_OBJECT = RedisManager(password=getenv("REDIS_PASSWORD"))

