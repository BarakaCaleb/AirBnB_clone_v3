#!/usr/bin/env python3
"""This shows all the route status of the AirBnB API"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status")
def status():
    """Returns JSON object with the current server status."""
    return jsonify({"status": "OK"})
