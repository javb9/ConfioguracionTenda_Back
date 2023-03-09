
from flask import Flask, jsonify, request
import pyodbc

conexion = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=JAVB2807;DATABASE=TG_DB;UID=sa;PWD=123')


def Autenticacion(loginRequest):
    try:
        cursor = conexion.cursor()
        cursor.execute("""select * from T01_USERS 
                    WHERE AT01USUARIO = '{0}' 
                    AND AT01CONTRASENA='{1}'""".format(loginRequest['usuario'], loginRequest['contrasena']))
        row = cursor.fetchone()
        return row
    except Exception as exc:
        print(exc)

def obtenerRoles():
    try:
        cursor = conexion.cursor()
        cursor.execute("select AT02ID, AT02DESCRIPCION from T02_ROLES")
        row = cursor.fetchall()
        return row
    except Exception as exc:
        print(exc)

def obtenerTiposDoc():
    try:
        cursor = conexion.cursor()
        cursor.execute("select AT04ID, AT04DESRIPCION from T04_DOCUMENTS_TYPES")
        row = cursor.fetchall()
        return row
    except Exception as exc:
        print(exc)

def actualizarUsuarios(usuario):
    try:
        cursor = conexion.cursor()
        cursor.execute("""UPDATE T01_USERS SET AT01NOMBRE ='{0}',
                AT01TIPO_DOCUMENTO = '{1}',
                AT01NUMERO_DOCUMENTO = '{2}',
                AT01CORREO = '{3}',
                AT01TELEFONO = '{4}'
                WHERE AT01ID= {5}""".format(usuario['nombre'], usuario['tipoDocumento'], usuario['numeroDocumento'], usuario['correo'], usuario['telefono'], usuario['id']))
        conexion.commit()
        crearNotificacion(usuario['numeroDocumento'], 'ACTUALIZAR')
        return {'mensaje': 'se edito usuario'}
    except Exception as exc:
        print(exc)

def crearNotificacion(usuario, validacion):
    try:
        tipoNotificacion=''
        if(validacion=='ACTUALIZAR'):
            tipoNotificacion='cambio de datos de usuario'
        else:
            tipoNotificacion='se creo nuevo usuario'
        cursor = conexion.cursor()
        cursor.execute("""INSERT INTO T05_NOTIFICACIONES (AT05NOTIFICACION,AT05DOCUMENTO_USUARIO) VALUES('{0}', '{1}')""".format(tipoNotificacion, usuario))
        conexion.commit()
    except Exception as exc:
        print(exc)

def CrearUsuarios(usuario):
    try:
        cursor = conexion.cursor()
        sql = """INSERT INTO T01_USERS (AT01NOMBRE,AT01TIPO_DOCUMENTO,AT01NUMERO_DOCUMENTO,AT01USUARIO,AT01CONTRASENA,AT01CORREO,AT01TELEFONO,AT01ID_ROL,AT01ESTADO_REGISTRO) 
            VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')""".format(usuario['nombre'], usuario['tipoDocumento'], usuario['numeroDocumento'],  usuario['login'], usuario['contraseña'], usuario['correo'], usuario['telefono'], usuario['idRol'], 1)
        cursor.execute(sql)
        conexion.commit()
        crearNotificacion(usuario['numeroDocumento'], 'CREAR')
        return {'mensaje': 'se creo usuario'}
    except Exception as exc:
        print(exc)

def obtenerUsuario(id):
    try:
        cursor = conexion.cursor()
        cursor.execute("""SELECT 
                AT01ID,
                AT01NOMBRE,
                AT01TIPO_DOCUMENTO,
                AT01NUMERO_DOCUMENTO,
                AT01USUARIO,
                AT01CONTRASENA,
                AT01CORREO,
                AT01TELEFONO, 
                AT01ID_ROL
                FROM T01_USERS
                WHERE AT01ID= {0}""".format(id))
        row = cursor.fetchone()
        return row
    except Exception as exc:
        print(exc)


def obtenerNotificaciones():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT AT05ID, AT05NOTIFICACION, AT05DOCUMENTO_USUARIO FROM T05_NOTIFICACIONES ORDER BY AT05ID DESC")
        row = cursor.fetchall()
        return row
    except Exception as exc:
        print(exc)


def EliminarNot(id):
    try:
        cursor = conexion.cursor()
        cursor.execute("""DELETE T05_NOTIFICACIONES WHERE AT05ID={0}""".format(id))
        conexion.commit()
        return {'mensaje':'se elminio con exito la notificacion'}
    except Exception as exc:
        print(exc)

