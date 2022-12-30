
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
        return {'mensaje': 'se edito usuario'}
    except Exception as exc:
        print(exc)

def CrearUsuarios(usuario):
    try:
        cursor = conexion.cursor()
        sql = """INSERT INTO T01_USERS (AT01NOMBRE,AT01TIPO_DOCUMENTO,AT01NUMERO_DOCUMENTO,AT01USUARIO,AT01CONTRASENA,AT01CORREO,AT01TELEFONO,AT01ID_ROL,AT01ESTADO_REGISTRO) 
            VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')""".format(usuario['nombre'], usuario['tipoDocumento'], usuario['numeroDocumento'],  usuario['login'], usuario['contraseña'], usuario['correo'], usuario['telefono'], usuario['idRol'], 1)
        cursor.execute(sql)
        conexion.commit()
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