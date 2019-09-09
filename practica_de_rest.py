from flask import Flask, request
from flask import jsonify

app = Flask(__name__, static_url_path='')


@app.route('/')
def send_js():
    return app.send_static_file('mandar_a_rest.html')

@app.route('/ejemplo')
def ejemplo2():
    return jsonify(Hola = 'Mundo!', mensaje = "Prueba el siguiente /ejemplo3 para usar los datos en json con el resto de metodos")

@app.route('/ejemplo2', methods=['GET'])
def ejemplo3():
    return jsonify(Hola = 'Mundo2!')

@app.route('/ejemplo3', methods=['GET', 'POST', 'DELETE', 'PUT'])
def ejemplo5():
    if request.method == 'POST':
            content = request.get_json(force=True)
            print(content)
            if 'nombre' in content.keys():
                nombre =content['nombre']
            else:
                return jsonify(error='json no es correcto')
            if 'apellido' in content.keys():
                apellido =content['apellido']
            else:
                return jsonify(error='json no es correcto')            
            return jsonify('Quien eres? Soy ' + nombre +" "+ apellido)
    elif request.method == 'GET':
        content = request.get_json()
        return jsonify('soy un get')
    elif request.method == 'DELETE':
        return jsonify('soy un DELETE que mando '+str(content['nombre']+" "+content['apellido']))
    elif request.method == 'PUT':
        content = request.get_json(force=True)
        return jsonify('soy un PUT que mando '+str(content['nombre']+" "+content['apellido']))

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=8080)