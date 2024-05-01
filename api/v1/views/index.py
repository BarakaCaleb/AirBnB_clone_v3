#!/usr/bin/env python3
"""This shows all the route status of the AirBnB API"""
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from api.v1.views import app_views


@app_views.route("/status", methods=['GET'])
def status():
    """Returns JSON object with the current server status."""
    return jsonify({"status": "OK"})



@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """Gets the count of each object type.
    
    Returns:
        A JSON Object with the number of objects by type."""
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    
        })
