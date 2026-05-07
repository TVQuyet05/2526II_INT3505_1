import time
import logging
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from pythonjsonlogger import jsonlogger

app = Flask(__name__)

# Configure JSON Logging
logger = logging.getLogger("flask_app")
logger.setLevel(logging.INFO)
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s')
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

# Rate Limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

# Prometheus Metrics
REQUEST_COUNT = Counter(
    'http_requests_total', 'Total HTTP Requests',
    ['method', 'endpoint', 'http_status']
)
REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds', 'HTTP Request Latency',
    ['method', 'endpoint']
)

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    request_latency = time.time() - request.start_time
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path,
        http_status=response.status_code
    ).inc()
    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.path
    ).observe(request_latency)
    
    # Audit log
    logger.info("http_request", extra={
        "method": request.method,
        "path": request.path,
        "status": response.status_code,
        "ip": request.remote_addr,
        "latency": request_latency
    })
    return response

@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/health', methods=['GET'])
@limiter.exempt
def health():
    return jsonify({"status": "UP"}), 200

@app.route('/v1/echo', methods=['GET'])
@limiter.limit("10 per minute")
def echo():
    msg = request.args.get('msg', 'hello')
    return jsonify({"msg": msg}), 200

@app.route('/v1/items', methods=['POST'])
@limiter.limit("5 per minute")
def create_item():
    data = request.get_json() or {}
    name = data.get('name', 'unknown')
    return jsonify({"id": 1, "name": name}), 201

if __name__ == '__main__':
    # Chạy trên port 8000 để khớp với cấu hình Prometheus
    app.run(host='0.0.0.0', port=8000)
