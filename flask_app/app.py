from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))

redis_client = redis.Redis(
    host=redis_host,
    port=redis_port,
    decode_responses=True
)

@app.route('/ping')
def ping():
    return jsonify({"status": "ok"})

@app.route('/count')
def count():
    try:
        visits = redis_client.incr('visits')
        return jsonify({
            "visit_count": visits,
            "redis_status": "connected"
        })
    except redis.ConnectionError:
        return jsonify({
            "error": "Redis connection failed",
            "redis_status": "disconnected"
        }), 500
