#!/usr/bin/python3
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
import os
from flask_cors import CORS


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
# Create a CORS instance allowing /* for 0.0.0.0
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Calls storage.close() at the end of the request
    """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """
    Returns a JSON-formatted 404 status code response
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
