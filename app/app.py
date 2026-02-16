from flask import Flask, jsonify, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

REQ_COUNT = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint"])
REQ_LATENCY = Histogram("http_request_duration_seconds", "HTTP request latency", ["endpoint"])

@app.before_request
def before():
    # You can keep it simple; endpoint will be set in routes.
    pass

@app.get("/")
def home():
    start = time.time()
    REQ_COUNT.labels("GET", "/").inc()
    time.sleep(0.02)  # small delay to make latency visible in graphs
    REQ_LATENCY.labels("/").observe(time.time() - start)
    return jsonify(message="DevOps Project Running ", service="sample-flask", version="1.0")

@app.get("/health")
def health():
    REQ_COUNT.labels("GET", "/health").inc()
    return jsonify(status="ok")

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
