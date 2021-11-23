from flask import Flask, jsonify, request, Response, render_template
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__, template_folder='templates')
app.config['MONGO_URI'] = 'mongodb://localhost/cripto'

mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if username and email and password:
            hash = generate_password_hash(password)
            id = mongo.db.users.insert(
                {'username': username, 'password': hash, 'email': email}
            )
            response = {
                'id': str(id),
                'username': username,
                'password': hash,
                'email': email
            }
            return response
        else:
            return not_found()

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({'_id':ObjectId(id)})
    response = json_util.dumps(user)
    return Response(response, mimetype='application/json')



@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response

@app.route('/users/<_id>', methods=['PUT'])
def update_user(_id):
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    if username and email and password and _id:
        hash = generate_password_hash(password)
        mongo.db.users.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'username': username, 'email': email, 'password': hash}})
        response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
      return not_found()



@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True)