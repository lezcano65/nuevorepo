import pymysql
host_name='localhost'
user_name='root'
password_name='lezcano65'
db_name='prestamosdb'

def create_tablas():
    #crear base de datos
    conexion = pymysql.connect(host=host_name, 
                                user=user_name,      
                                password=password_name)
    consulta = conexion.cursor()
    try:
        with conexion.cursor() as cursor:
            instruccion_crear_database = 'CREATE DATABASE IF NOT EXISTS '+db_name
            cursor.execute(instruccion_crear_database)
            print('la base de datos ',db_name,'se encuentra disponible')
    finally:
        conexion.close()
    conexion = pymysql.connect(host=host_name, 
                                user=user_name,      
                                password=password_name,
                                db=db_name)
    consulta = conexion.cursor()
    #crear tabla clientes
    sql = 'CREATE TABLE IF NOT EXISTS clientes(dni INTEGER PRIMARY KEY NOT NULL, nombres VARCHAR(30) NOT NULL, apellidos VARCHAR(30) NOT NULL, telefono VARCHAR(14) NOT NULL, celular VARCHAR(14) NOT NULL)'
    try:
        consulta.execute(sql)
        print('La tabla clientes se encuentra disponible')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla clientes: ", e)
    #crear tabla prestamos
    sql = 'CREATE TABLE IF NOT EXISTS prestamos(numero_prestamo INTEGER PRIMARY KEY NOT NULL, dni_cliente INTEGER NOT NULL, fecha_autorizacion DATETIME NOT NULL, fecha_tentativa DATETIME NOT NULL, cantidad_de_cuotas INTEGER NOT NULL, monto_prestamo INTEGER NOT NULL, precio_cuota INTEGER NOT NULL, fecha_entrega DATETIME NOT NULL, KEY dnisolicitante_dni_clientes_00_idx (dni_cliente), CONSTRAINT dnisolicitante_dni_clientes_00 FOREIGN KEY (dni_cliente) REFERENCES clientes (dni))'
    try:
        consulta.execute(sql)
        print('La tabla prestamos se encuentra disponible')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla prestamos: ", e)
    #crear tabla empleados
    sql = 'CREATE TABLE IF NOT EXISTS empleados(numero_prestamo INTEGER PRIMARY KEY NOT NULL, nombre VARCHAR(30) NOT NULL, cuil integer NOT NULL,KEY numero_prestamo_empleados_nro_prestamo_prestamos_01_idx (numero_prestamo), CONSTRAINT numero_prestamo_empleados_nro_prestamo_prestamos_01 FOREIGN KEY (numero_prestamo) REFERENCES prestamos (numero_prestamo))'
    try:
        consulta.execute(sql)
        print('La tabla empleados se encuentra disponible')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla empleados: ", e)
    #crear tabla cuotas_prestamos 
    sql = 'CREATE TABLE IF NOT EXISTS cuotas_prestamos(numero_prestamo INTEGER NOT NULL, numero_cuota INTEGER NOT NULL, fecha DATETIME NOT NULL, precio_pagado INTEGER NOT NULL, PRIMARY KEY (numero_prestamo, numero_cuota),KEY numerp_prestamo_couta_prestamo_numero_prestamo_prestamo_02_idx (numero_prestamo), CONSTRAINT numerp_prestamo_couta_prestamo_numero_prestamo_prestamo_02 FOREIGN KEY (numero_prestamo) REFERENCES prestamos (numero_prestamo))'
    try:
        consulta.execute(sql)
        print('La tabla cuotas_prestamos se encuentra disponible')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla cuotas_prestamos: ", e)
    conexion.close()

def agregar_cliente(dni, nombres, apellidos, telefono, celular):
    conexion = pymysql.connect(host=host_name, 
                                user=user_name,      
                                password=password_name,
                                db=db_name)
    consulta = conexion.cursor()
    datos = (dni, nombres, apellidos, telefono, celular)
    sql_select_Query = 'INSERT INTO clientes(dni, nombres, apellidos, telefono, celular) VALUES (%s,%s,%s,%s,%s)'
    try:
        consulta.execute(sql_select_Query, datos)
        print("Datos guardados con exito")
    except:
        print("Ocurrió un error al intentar guardar los datos")
    conexion.commit()
    conexion.close()

def eliminar_cliente(dni):
    try:
        conexion = pymysql.connect(host=host_name, 
                                    user=user_name,      
                                    password=password_name,
                                    db=db_name)
        try:
            with conexion.cursor() as cursor:
                sql_select_Query = 'DELETE FROM clientes WHERE dni= %s'
                cursor.execute(sql_select_Query, dni)
                print('cliente eliminado')
        finally:
            conexion.commit()
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error consultando la tabla:", e)

def buscar_cliente_nombres(dni):
    try:
        conexion = pymysql.connect(host=host_name, 
                                    user=user_name,      
                                    password=password_name,
                                    db=db_name)
        try:
            with conexion.cursor() as cursor:
                consulta = 'SELECT * FROM clientes WHERE dni = %s'
                cursor.execute(consulta, dni)
                lista_contactos = cursor.fetchall()
                if lista_contactos == ():
                    print('cliente no encontrado')
                for lista in lista_contactos:
                    print(lista)
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error consultando la tabla:", e)

def update_data_cliente(dni, nombres, apellidos, telefono, celular, buscar):
    conexion = pymysql.connect(host=host_name,
                                user=user_name,
                                password=password_name,
                                db=db_name)
    consulta = conexion.cursor()
    sql_select_Query = 'UPDATE clientes SET dni = %s,nombres = %s,apellidos = %s,telefono = %s,celular = %s WHERE dni = %s'
    datos = (dni,nombres,apellidos,telefono,celular,buscar)
    try:
        consulta.execute(sql_select_Query, datos)
        print("Datos modificados con exito")
    except:
        print("Ocurrió un error al intentar guardar los datos")
    conexion.commit()
    conexion.close()
    consulta.close()

def get_all_data_clientes():
    try:
        connection = pymysql.connect(host=host_name,
                                    user=user_name,
                                    password=password_name,
                                    db=db_name)
        sql_select_Query = "select * from clientes Order By dni"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        lista_resultado = cursor.fetchall()
        if lista_resultado == ():
            print("No hay clientes...")
        for row in lista_resultado:
            print('[+]dni:',row[0],'\n[+]nombres:',row[1],'\n[+]apellidos:',row[2],'\n[+]telefono:',row[3],'\n[+]celular:',row[4],"\n----------") 
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error reading data from MySQL table", e)
    finally:
        connection.close()
        cursor.close()

