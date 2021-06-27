from flask import request
from app import app
from app.controllers.health_indicator import HealthIndicator

@app.route('/api')
def helloapi():
    return "Hello World!"

## Health Check ##
@app.route('/health')
def health_indicator():
    return HealthIndicator().run()
##################
