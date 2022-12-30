from flask import Flask, jsonify, request
import json
from backEnd.repository import *
from backEnd.Models import models
from backEnd.tenda.tendaConfig import TendaManager

app=Flask(__name__)

@app.route('/consultarRoles')
def consultarRoles():
    try:
        datos = obtenerRoles()
        estados=[]
        for dato in datos:
            estado={'id': dato[0], 'descripcion': dato[1]}
            estados.append(estado)
        resp=models.Responses()
        resp.generaRespuestaGenerica(estados, False)
        return json.dumps(resp.__dict__)
    except Exception as ex:
        return jsonify({'mensaje' : 'Error'})

@app.route('/Autenticacion', methods=['POST'])
def autenticacion():
    try:
        print(request.json)
        dato = Autenticacion(request.json)
        mensaje=''
        if(dato!=None):
            mensaje = {'mensaje': 'Ingreso exitoso', 'login':True, 'idUsuario': dato[0]}
        else:
            mensaje={'mensaje': 'usuario y/o contraseña incorrecta', 'login':False}

        resp=models.Responses()
        resp.generaRespuestaGenerica(mensaje, False)
        return json.dumps(resp.__dict__)
    except Exception as ex:
        mensaje={'mensaje' : 'Error'}
        resp=models.Responses()
        resp.generaRespuestaGenerica(mensaje, True)
        return json.dumps(resp.__dict__)

@app.route('/EditarUsuario', methods=['POST'])
def EditarUsuario():
    try:
        mensaje = actualizarUsuarios(request.json)
        resp=models.Responses()
        resp.generaRespuestaGenerica(mensaje, False)
        return json.dumps(resp.__dict__)
    except Exception as ex:
        return jsonify({'mensaje' : 'Error'})

@app.route('/RegistrarUsuario', methods=['POST'])
def RegistrarUsuario():
    try:
        mensaje = CrearUsuarios(request.json)
        resp=models.Responses()
        resp.generaRespuestaGenerica(mensaje, False)
        return json.dumps(resp.__dict__)
    except Exception as ex:
        return jsonify({'mensaje' : 'Error'})

@app.route('/CambiarContrasennaRouter', methods=['POST'])
def CambiarContrasennaRouter():
    try:
        resp=models.Responses()
        resp.generaRespuestaGenerica({'mensaje':'se cambio de forma correcta'}, False)
        return json.dumps(resp.__dict__)
    except Exception as ex:
        return jsonify({'mensaje' : 'Error'})

@app.route('/consultarTiposDoc')
def consultarTiposDoc():
    try:
        datos = obtenerTiposDoc()
        estados=[]
        for dato in datos:
            estado={'id': dato[0], 'descripcion': dato[1]}
            estados.append(estado)
        resp=models.Responses()
        resp.generaRespuestaGenerica(estados, False)
        return json.dumps(resp.__dict__)
    except Exception as ex:
        return jsonify({'mensaje' : 'Error'})

@app.route('/consultarUsuario/<id>')
def consultarUsuario(id):
    try:
        datos = obtenerUsuario(id)
        usuario = {"nombre": datos[1], "tipoDocumento": datos[2], "numeroDocumento": datos[3], "login": datos[4], "contraseña":datos[5], "correo":datos[6], "telefono":datos[7], "idRol": datos[8] }
        resp=models.Responses()
        resp.generaRespuestaGenerica(usuario, False)
        return json.dumps(resp.__dict__)
    except Exception as ex:
        return jsonify({'mensaje' : 'Error'})

if(__name__=='__main__'):
    app.run(debug=True)
