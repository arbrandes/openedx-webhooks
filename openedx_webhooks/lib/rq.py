"""
RQ tools.
"""

import os

import redis
from rq import Queue

_redis_url = os.environ.get('REDIS_TLS_URL', os.environ.get('REDIS_URL', 'redis://'))

redis_tls_options = "?ssl_cert_reqs=none"
if _redis_url.startswith("rediss"):
    _redis_url += redis_tls_options

# redis.Redis: Instance of a connected Redis store
store = redis.from_url(_redis_url)

# rq.Queue: Instance of RQ queue
q = Queue(connection=store)
