#!usr/bin/env python3
"""The entry point for the AirBnB APIs"""
from flask import flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)














if __name__ == '__main__':
    app.run(
            host=getenv("HBNB_API_HOST", default="0.0.0.0"),
            port=getenv("HBNB_API_PORT", default="5000"),
            threaded=True
            )
