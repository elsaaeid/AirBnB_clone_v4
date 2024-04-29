#!/usr/bin/python3
from flask import Blueprint, jsonify, request
from models import storage, Place, Amenity
from api.v1.views import app_views

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


@app_views.route('/places/<place_id>/amenities', methods=['GET'], strict_slashes=False)
def get_place_amenities(place_id):
    """
    Retrieves the list of all Amenity objects of a Place
    """
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({"error": "Not found"}), 404
    amenities = [amenity.to_dict() for amenity in place.amenities]
    return jsonify(amenities)


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_place_amenity(place_id, amenity_id):
    """
    Deletes an Amenity object from a Place
    """
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({"error": "Not found"}), 404
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        return jsonify({"error": "Not found"}), 404
    if amenity not in place.amenities:
        return jsonify({"error": "Not linked to the Place"}), 404
    place.amenities.remove(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'], strict_slashes=False)
def link_place_amenity(place_id, amenity_id):
    """
    Links an Amenity object to a Place
    """
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({"error": "Not found"}), 404
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        return jsonify({"error": "Not found"}), 404
    if amenity in place.amenities:
        return jsonify(amenity.to_dict()), 200
    place.amenities.append(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201