from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import logging

# Create Flask app
app = Flask(__name__)

# Set up Prometheus metrics endpoint (/metrics)
metrics = PrometheusMetrics(app)

# logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def hello():
    logger.info("Home route accessed")
    return "Hello from Flask!"

@app.route('/health')
def health():
    logger.info("Health check route accessed")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
