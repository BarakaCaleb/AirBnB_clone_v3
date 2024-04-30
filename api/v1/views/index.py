#!/usr/bin/env python3
"""This shows all the route status of the AirBnB API"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status")
def status():
    """Returns JSON object with the current server status."""
    return jsonify({"status": "OK"})



@app_views.route("/stats")
def stats():
    """Gets the count of each object type.
    
    Returns:
        A JSON Object with the number of objects by type."""
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        places
        reviews
        states
        users
    })
