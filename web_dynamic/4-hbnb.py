#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
import uuid


app = Flask(__name__)
port = 5000
host = '0.0.0.0'


@app.teardown_appcontext
def tear_down(self):
    """tear down app context"""
    storage.close()


@app.route('/4-hbnb/', strict_slashes=False)
def show_page():
    """displays webpage
    Returns:
        HTML Page
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('4-hbnb.html',
                           cache_id=uuid.uuid4(),
                           states=states,
                           amenities=amenities,
                           places=places,
                           users=users)

if __name__ == "__main__":
    app.run(host=host, port=port)
