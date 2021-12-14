# Import flask modules
from flask import jsonify, request

# Import application requirements
from app import app

from controller import Controller

controller = Controller()


# Routes
@app.route('/api/rows', methods=['POST'])
def index_handler():
    response = {'status': 'success'}  # Response dict
    if request.method == 'POST':  # Check on POST Request
        response.update(controller.get_data(payload=request.get_json()))
    return jsonify(response)  # Return response on front-end
