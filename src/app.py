from flask import Flask, jsonify, request
from backEnd.repository import *

app=Flask(__name__)

@app.route('/')
def dato():
    try:
        datos = obtenerEstados()
        estados=[]
        for dato in datos:
            estado={'id': dato[0], 'descripcion': dato[1]}
            estados.append(estado)
        return jsonify(estados)
    except Exception as ex:
        return jsonify({'mensaje' : 'Error'})

@app.route('/ConsultOneState/<id>', methods=['GET'])
def obtenerUnEstado(id):
    try:
        dato = obtenerUnEstados(id)
        if(dato!=None):
            estado={'id': dato[0], 'descripcion': dato[1]}
            return jsonify(estado)
        else:
            return jsonify({'mensaje': ' estado no existe'})
    except Exception as ex:
        return jsonify({'mensaje' : 'Error'})

@app.route('/ActualizarUsuario', methods=['POST'])
def ActualizarUsuario():
    try:
        mensaje = actualizarUsuarios(request.json)
        return mensaje
    except Exception as ex:
        return jsonify({'mensaje' : 'Error'})

@app.route('/CrearUsuario', methods=['POST'])
def CrearUsuario():
    try:
        mensaje = CrearUsuarios(request.json)
        return mensaje
    except Exception as ex:
        return jsonify({'mensaje' : 'Error'})


if(__name__=='__main__'):
    app.run(debug=True)
