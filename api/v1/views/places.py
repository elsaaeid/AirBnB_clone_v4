#!/usr/bin/python3
from flask import Blueprint, jsonify, request
from models import storage, Place, State, City, Amenity, User
from api.v1.views import app_views


app_views = Blueprint('app_views', __name__,
                      url_prefix='/api/v1')


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def get_places_by_city(city_id):
    """
    Retrieves the list of all Place objects of a City
    """
    city = storage.get(City, city_id)
    if not city:
        return jsonify({"error": "Not found"}), 404
    places = [place.to_dict() for place in city.places]
    return jsonify(places)


@app_views.route('/places/<place_id>',
                 methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """
    Retrieves a Place object
    """
    place = storage.get(Place, place_id)
    if place:
        return jsonify(place.to_dict())
    else:
        return jsonify({"error": "Not found"}), 404


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """
    Deletes a Place object
    """
    place = storage.get(Place, place_id)
    if place:
        storage.delete(place)
        storage.save()
        return jsonify({})
    else:
        return jsonify({"error": "Not found"}), 404


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """
    Creates a Place object
    """
    city = storage.get(City, city_id)
    if not city:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'user_id' not in data:
        return jsonify({"error": "Missing user_id"}), 400
    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    user = storage.get(User, data['user_id'])
    if not user:
        return jsonify({"error": "User not found"}), 404
    new_place = Place(**data)
    new_place.city_id = city_id
    new_place.save()
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>',
                 methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """
    Updates a Place object
    """
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict()), 200


@app_views.route('/places_search',
                 methods=['POST'], strict_slashes=False)
def places_search():
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400

    data = request.get_json()
    states = data.get('states', [])
    cities = data.get('cities', [])
    amenities = data.get('amenities', [])

    if not any([states, cities, amenities]):
        places = storage.all(Place).values()
        return jsonify([place.to_dict() for place in places])

    place_ids = set()
    if states:
        for state_id in states:
            state = storage.get(State, state_id)
            if state:
                for city in state.cities:
                    place_ids.update({place.id
                                      for place in city.places})

    if cities:
        for city_id in cities:
            city = storage.get(City, city_id)
            if city:
                place_ids.update({place.id
                                  for place in city.places})

    if amenities:
        places = storage.all(Place).values()
        for amenity_id in amenities:
            amenity = storage.get(Amenity, amenity_id)
            if amenity:
                places = [place for place in places
                          if amenity in place.amenities]

    places = [storage.get(Place, place_id) for place_id in place_ids]
    return jsonify([place.to_dict() for place in places])
