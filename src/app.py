from flask import Flask, jsonify, request
import json
from backEnd.repository import *
from backEnd.Models import models
from backEnd.tenda.tendaConfig import TendaManager
from backEnd.tenda.ip import obtenerPuertaEnlace
from getmac import *

win_mac = get_mac_address(interface="Ethernet")
won_mac = get_mac_address(interface="Wi-Fi")
print (win_mac)
print(won_mac)

puertaEnlace=obtenerPuertaEnlace()
# manager = TendaManager(puertaEnlace, 'admin')

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

@app.route('/EditRouterInfo', methods=['POST'])
def actualizarContraseñaRouter():
    try:
        datos=request.json
        manager.set_wifi_settings(datos['contrasennaRed'], datos['nombreRed'])
        mensaje = {'mensaje': 'se edito datos router'}
        resp=models.Responses()
        resp.generaRespuestaGenerica(mensaje, False)
        return json.dumps(resp.__dict__)
    except Exception as exc:
        print(exc)

@app.route('/consultarNotifiaciones')
def consultarNotifiaciones():
    try:
        datos = obtenerNotificaciones()
        notificaciones=[]
        for dato in datos:
            notifiacion={'id': dato[0], 'notificacion': dato[1], 'documento':dato[2]}
            notificaciones.append(notifiacion)
        resp=models.Responses()
        resp.generaRespuestaGenerica(notificaciones, False)
        return json.dumps(resp.__dict__)
    except Exception as ex:
        return jsonify({'mensaje' : 'Error'})

@app.route('/EliminarNotificacion/<id>')
def EliminarNotificacion(id):
    try:
        mensaje = EliminarNot(id)
        resp=models.Responses()
        resp.generaRespuestaGenerica(mensaje, False)
        return json.dumps(resp.__dict__)
    except Exception as ex:
        return jsonify({'mensaje' : 'Error'})

@app.route('/ObtenerConectados')
def Conectados():
    try:
        datos = manager.get_online_devices_with_stats()
        dispositivos=[]
        for dato in datos:
            mac =dato['qosListMac']
            if mac != win_mac & mac !=won_mac:
                dispositivo={'mac':mac}
                dispositivos.append(dispositivo)
        resp=models.Responses()
        resp.generaRespuestaGenerica(dispositivos, False)
        return json.dumps(resp.__dict__)
    except Exception as exc:
        print(exc)
if(__name__=='__main__'):
    app.run(debug=True)
