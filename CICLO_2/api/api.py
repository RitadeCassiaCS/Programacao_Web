"""
Engenharia de Software - UniEVANGÉLICA
Programação Web
Dev: Rita de Cássia da Costa Silva
06/06/2024
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

cars = [
    {
        'id': 10,
        'modelo': 'GTS',
        'marca': 'McLaren'
    },
    {
        'id': 20,
        'modelo': 'Duster',
        'marca': 'Renault'
    },
    {
        'id': 30,
        'modelo': 'Panamera Turbo',
        'marca': 'Porsche'
    }
    {
        'id': 40,
        'modelo': 'Bronco Raptor',
        'marca': 'Ford'
    }
    {
        'id': 50,
        'modelo': 'AMG GT',
        'marca': 'Mercedes'
    }
]

#GET /api/cars - recuperar a lista de carros

@app.route('/cars', methods=['GET'])
def get_car():
    return jsonify(cars)

#POST /api/cars - criar um novo carro

@app.route('/cars', methods=['POST'])
def post_new_car():
    new_car = request.get_json()
    cars.append(new_car)
    return jsonify(cars)

#GET /api/cars/{car_id} - recuperar informações de um carro específico por ID

@app.route('/cars/<int:id>', methods=['GET'])
def get_car_by_id(id):
    for car in cars:
        if car.get('id') == id:
            return jsonify(car)

#PUT /api/cars/{car_id} - atualizar informações de um carro específico por ID

@app.route('/cars/<int:id>', methods=['PUT'])
def edit_car_by_id(id):
    edited_car = request.get_json()
    for index, car in enumerate(cars):
        if car.get('id') == id:
            cars[index].update(edited_car)
            return jsonify(cars[index])

#DELETE /api/cars/{car_id} - excluir um carro específico por ID

@app.route('/cars/<int:id>', methods=['DELETE'])
def delete_car(id):
    for index, car in enumerate(cars):
        if car.get('id') == id:
            del cars[index]
    
    return jsonify(cars)


app.run(port=5000, host='localhost', debug=True)