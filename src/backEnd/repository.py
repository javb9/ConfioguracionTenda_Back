
from flask import Flask, jsonify, request
import pyodbc

conexion = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=JAVB2807;DATABASE=TG_DB;UID=sa;PWD=123')


def obtenerEstados():
    try:
        cursor = conexion.cursor()
        cursor.execute("select * from T03_STATES")
        row = cursor.fetchall()
        return row
    except Exception as exc:
        print(exc)


def obtenerUnEstados(id):
    try:
        cursor = conexion.cursor()
        cursor.execute("select * from T03_STATES where AT03ID =" + id)
        row = cursor.fetchone()
        return row
    except Exception as exc:
        print(exc)


def actualizarUsuarios(usuario):
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE T01_USERS SET AT01PRIMER_NOMBRE =" + usuario['primerNombre'] + ",AT01SEGUNDO_NOMBRE = "+ usuario['segundoNombre'] + ",AT01PRIMER_APELLIDO = " + usuario['primerApellido'] + ",AT01SEGUNDO_APELLIDO = " + usuario['segundoApellido'] + ",AT01USUARIO = " + usuario['login'] + ",AT01CONTRASENA = " + usuario['contraseña'] + ",AT01CORREO = " + usuario['correo'] + ",AT01TELEFONO = " + usuario['telefono'] + " WHERE AT01ID= " + usuario['id'])
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
        return jsonify({'mensaje': 'se creo usuario'})
    except Exception as exc:
        print(exc)
