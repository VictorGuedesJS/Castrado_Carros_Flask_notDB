from flask import Flask, make_response, jsonify, request, abort
from db import carros

app = Flask(__name__)


@app.route('/carros', methods = ['GET'])
def getCarros():
    return make_response(
        jsonify(carros)
    )
@app.route('/carros/<int:item_id>', methods = ['GET'])
def getCarrosById(item_id):
    item = next((item for item in carros if item['id'] == item_id), None)
    if item is None:
        abort(404)  # Return a 404 Not Found error if item not found
    return jsonify(item)

@app.route('/carros/<int:carro_id>', methods = ['PUT'])
def updateCarro(carro_id):
    carro = next((carro for carro in carros if carro['id'] == carro_id), None)
    
    if carro is None:
        abort(404)  

    data = request.get_json()
    
    campos_necessarios = ['modelo', 'marca', 'ano']
    for campo in campos_necessarios:
        if campo not in data:
            return  abort(400, description="Invalid input")

    
    carro['modelo'] = data['modelo']
    carro['marca'] = data['marca']
    carro['ano'] = data['ano']

    
    return jsonify(carro)



@app.route('/carros', methods = ['POST'])
def postCarros():
    carro = request.json
    carros.append(carro)
    print(carro)
    return "\n Sucessful Added"


app.run()
