from flask import Flask, request, jsonify, make_response
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def index():
    return make_response(jsonify({"Mensaje": "Servidor en linea"}), 200)

@app.route('/Insert', methods=['POST'])
def Insert():

    if request.method == 'POST':

        try:
            MONGO_URI = 'mongodb://localhost'
            client = MongoClient(MONGO_URI)
            db = client['ArquitecturaDelCompu']
            collection = db['Lab5']

            obj = request.json['object_to_insert']
            collection.insert_one(obj)

            resp = make_response(jsonify({"Mensaje": "Objeto Insertado correctamente"}), 200)
            return resp

        except:
            return make_response(jsonify({"Mensaje" : "Ha ocurrido un error al insertar el objeto"}), 400)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)