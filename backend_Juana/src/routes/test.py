from flask import Blueprint, jsonify, request
from flask_cors import CORS

test_blueprint = Blueprint("test", __name__)
CORS(test_blueprint)

@test_blueprint.route('/one', methods=['GET'])
def test_one():
    return jsonify({'ok': True, 'data': 'test-one'})

@test_blueprint.route('/two', methods=['GET'])
def test_two():
    return jsonify({'ok': True, 'data': 'test-two'})
