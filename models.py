# Assume this function fetches data from your database/service layer
# This is a mock function to simulate a database fetch
# In a real app, this would hit your database (Cloud SQL, etc.)

def get_info():
    data = {
            "messgae": "Demo, APP for Analytics",
            "version": "0.0.1",
            "status": "Development",
            "endpoints": [
                {
                    "route": "/api/v1/analytics/city/<cityId>",
                    "description": "Get analytics data for a city",
                    "demo": "/api/v1/analytics/city/es-mad",
                },
                {
                    "route": "/api/v1/analytics/trip/<tripId>",
                    "description": "Get analytics data for a trip",
                    "demo": "/api/v1/analytics/trip/a1b2c3d4-e5f6-7890-1234-567890abcdef",
                },
            ],
        }
    return data 


def get_city(city_id: str) :
    # --- Database Interaction Logic ---
    # Fetch raw data for the city_id
    # In a real app, this would hit your database (Cloud SQL, etc.)
    if city_id == "es-mad":
        # Return data matching the structure needed by Pydantic models
        # (You might use an ORM that maps directly or construct this json)
        data = {
            "query_details": {
            "city_id": "es-mad", 
            "start_date": "2025-03-29",
            "end_date": "2025-03-29",
            "granularity": "daily",
            "generated_at": "2025-03-30T16:42:55Z" 
            },
            "metrics_summary": { 
            "city_id": "es-mad", 
            "city_name": "Madrid",
            "total_revenue": {
                "amount": 48700.50,
                "currency": "EUR"
            },
            "completed_trips": 2510,
            "average_trip_distance_km": 8.5,
            "total_trip_distance_km": 21335,
            "average_trip_duration_minutes": 22.1,
            "total_trip_duration_hours": 924.8,
            "average_fare_per_trip": {
                "amount": 19.40,
                "currency": "EUR"
            },
            "unique_active_drivers": 650,
            "unique_active_riders": 2250,
            "rider_cancellation_rate_percent": 5.5,
            "driver_cancellation_rate_percent": 2.0
            }
        }
        return data
    else:
        return None

def get_trip(trip_id: str):
    # --- Database Interaction Logic ---
    # Fetch raw data for the trip_id
    # In a real app, this would hit your database (Cloud SQL, etc.)
    if str(trip_id) == "a1b2c3d4-e5f6-7890-1234-567890abcdef":
         # Return data matching the structure needed by Pydantic models
         # (You might use an ORM that maps directly or construct this json)
        data = {
            "trip_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
            "rider": {
            "rider_id": "f0e9d8c7-b6a5-4321-fedc-ba9876543210",
            "first_name": "Elena",
            "last_name": "García"
            },
            "driver": {
            "driver_id": "1a2b3c4d-5e6f-7890-abcd-ef1234567890",
            "first_name": "Javier",
            "last_name": "Martínez",
            "average_rating": 4.85
            },
            "vehicle": {
            "vehicle_id": "fedcba98-7654-3210-1a2b-3c4d5e6f7890",
            "make": "Seat",
            "model": "León",
            "color": "Rojo",
            "license_plate": "1234 ABC",
            "vehicle_type": "standard"
            },
            "trip_status": "completed",
            "request_time": "2025-03-30T15:10:15Z",
            "accept_time": "2025-03-30T15:11:05Z",
            "pickup_time": "2025-03-30T15:15:45Z",
            "dropoff_time": "2025-03-30T15:35:10Z",
            "estimated_pickup_time": "2025-03-30T15:16:00Z",
            "estimated_dropoff_time": "2025-03-30T15:38:00Z",
            "estimated_fare": 18.50,
            "actual_fare": 19.75,
            "fare_currency": "EUR",
            "fare_breakdown": {
            "base_fare": 3.50,
            "distance_charge": 9.80,
            "time_charge": 4.20,
            "surge_multiplier": 1.0,
            "tolls": 0.00,
            "booking_fee": 1.00,
            "tax_vat": 1.25
            },
            "distance_meters": 7850,
            "duration_seconds": 1165,
            "pickup_location": {
            "address": "Calle de Serrano, 45, 28001 Madrid, Spain",
            "latitude": 40.4288,
            "longitude": -3.6885,
            "city": "Madrid"
            },
            "dropoff_location": {
            "address": "Plaza Mayor, 1, 28012 Madrid, Spain",
            "latitude": 40.4154,
            "longitude": -3.7074,
            "city": "Madrid"
            },
            "map_polyline": "encoded_polyline_string_here...", 
            "payment_method_details": 
            { 
                "payment_method_id": "pm_abc123xyz...",
                "card_type": "Visa",
                "last4": "4242"
            },
            "created_at": "2025-03-30T15:10:15Z",
            "updated_at": "2025-03-30T15:35:15Z"
        }
        return data
    
    else:
        return None # Trip not found