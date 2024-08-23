from flask import Flask, jsonify, make_response, request
from bd import Climas

app = Flask('clima')

# Visualizar os dados (GET)
@app.route('/clima', methods=['GET'])
def get_clima():
    return Climas


# Visualizar dados por ID (GET/ID)
@app.route('/clima/<int:id>', methods=['GET'])
def get_clima_id(id):
    for clima in Climas:
        if clima.get('id') == id:
            return jsonify(clima)
        

# Criar novos dados (POST)
@app.route('/clima', methods=['POST'])
def criar_clima():
    clima = request.json
    Climas.append(clima)
    return make_response(
        jsonify(mensagem="Clima cadastrado com sucesso!",
                clima=clima
                )

    )


# Editar dados (PUT)
@app.route('/clima/<int:id>', methods=['PUT'])
def editar_clima_id(id):
    clima_alterado = request.get_json()
    for indice, clima in enumerate(Climas):
        if clima.get('id') == id:
            Climas[indice].update(clima_alterado)
            return jsonify(Climas[indice])
        

# Deletar dados (DELETE)
@app.route('/clima/<int:id>', methods=['DELETE'])
def excluir_clima(id):
    for indice, clima in enumerate(Climas):
        if clima.get('id') == id:
            del Climas[indice]
            return jsonify({"Mensagem":"Clima excluído com sucesso!"})


app.run(port=5001, host='localhost')