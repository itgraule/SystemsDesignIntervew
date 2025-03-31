from xml.dom import ValidationErr
from flask import Flask, jsonify
import re
from datetime import datetime
from typing import Optional, List
from uuid import UUID
from datetime import datetime
from models import get_trip, get_city, get_info


# Main
# TODO: Move to factory
app = Flask(__name__)


# Routes
# TODO: Move to routes.py
# Home Route
@app.route("/")
def home():
    data = get_info()
    return jsonify(data), 200 


# Analytics City Route
@app.route("/api/v1/analytics/city/<city_id>")
def analytics_city(city_id):

    #TODO: Add authentication

    #TODO: Add Imput Validation Logic

    #TODO: Add filtering and sorting logic based on get parameters

    # Fetch raw data (usually a dict or ORM object)
    city_data = get_city(city_id)
    if city_data is None:
        return jsonify({"error": "City Not found: " + city_id}), 404

    try:
        # Return data matching the structure needed
        return jsonify(city_data), 200
    
    except ValidationErr as e:
        # This indicates an issue mapping DB data to the response model
        app.logger.error(f"Error creating response model for trip {city_id}: {e.errors()}")
        return jsonify({"error": "Internal server error creating response"}), 500
    except Exception as e:
        app.logger.error(f"Error fetching trip {city_id}: {e}")
        return jsonify({"error": "Internal server error"}), 500


# Analytics Trip Route
@app.route("/api/v1/analytics/trip/<trip_id>")
def analytics_trip(trip_id):
    #TODO: Add authentication

    #TODO: Add Imput Validation Logic

    #TODO: Add filtering and sorting logic based on get parameters

    # Fetch raw data (usually a dict or ORM object)
    trip_data = get_trip(trip_id)
    if trip_data is None:
        return jsonify({"error": "Trip Not found: " + trip_id}), 404

    try:
        # Return data matching the structure needed 
        return jsonify(trip_data), 200
    
    except ValidationErr as e:
        # This indicates an issue mapping DB data to the response model
        app.logger.error(f"Error creating response model for trip {trip_id}: {e.errors()}")
        return jsonify({"error": "Internal server error creating response"}), 500
    except Exception as e:
        app.logger.error(f"Error fetching trip {trip_id}: {e}")
        return jsonify({"error": "Internal server error"}), 500



