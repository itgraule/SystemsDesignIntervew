from models import get_trip, get_city

def test_get_city():
    city_id = "es-mad"
    city_data = get_city("city_id")
    assert city_data is not None

def test_invalid_get_city():
    city_id = "es-bcn"
    city_data = get_city("city_id")
    assert city_data is None


def test_get_trip():
    trip_id = "a1b2c3d4-e5f6-7890-1234-567890abcdef"
    trip_data = get_trip("trip_id")
    assert trip_data is not None

def test_get_invalid_trip():
    trip_id = "some-uiid-121212-oasj12-123123"
    trip_data = get_trip("trip_id")
    assert trip_data is None

