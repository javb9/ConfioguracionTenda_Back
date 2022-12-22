
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

def actualizarUsuarios(usuario):
    try:
        cursor = conexion.cursor()
        cursor.execute("""UPDATE T01_USERS SET AT01PRIMER_NOMBRE ='{0}',
                AT01SEGUNDO_NOMBRE = '{1}',
                AT01PRIMER_APELLIDO = '{2}',
                AT01SEGUNDO_APELLIDO = '{3}',
                AT01USUARIO = '{4}',
                AT01CONTRASENA = '{5}',
                AT01CORREO = '{6}',
                AT01TELEFONO = '{7}', 
                AT01ID_ROL = {8}
                WHERE AT01ID= {9}""".format(usuario['primerNombre'], usuario['segundoNombre'], usuario['primerApellido'], usuario['segundoApellido'], usuario['usuario'], usuario['contraseña'], usuario['correo'], usuario['telefono'], usuario['idRol'], usuario['id']))
        conexion.commit()
        return jsonify({'mensaje': 'se actualizo usuario'})
    except Exception as exc:
        print(exc)

def CrearUsuarios(usuario):
    try:
        cursor = conexion.cursor()
        sql = """INSERT INTO T01_USERS (AT01PRIMER_NOMBRE,AT01SEGUNDO_NOMBRE,AT01PRIMER_APELLIDO,AT01SEGUNDO_APELLIDO,AT01USUARIO,AT01CONTRASENA,AT01CORREO,AT01TELEFONO,AT01ID_ROL,AT01ESTADO_REGISTRO) 
            VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')""".format(usuario['primerNombre'], usuario['segundoNombre'], usuario['primerApellido'], usuario['segundoApellido'], usuario['login'], usuario['contraseña'], usuario['correo'], usuario['telefono'], usuario['idRol'], 1)
        cursor.execute(sql)
        conexion.commit()
        return {'mensaje': 'se creo usuario'}
    except Exception as exc:
        print(exc)
