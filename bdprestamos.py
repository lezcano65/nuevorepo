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
    sql = 'CREATE TABLE IF NOT EXISTS prestamos(numero_prestamo INTEGER PRIMARY KEY NOT NULL, dni_cliente INTEGER NOT NULL, fecha_autorizacion VARCHAR(14) NOT NULL, fecha_tentativa VARCHAR(14) NOT NULL, cantidad_de_cuotas INTEGER NOT NULL, monto_prestamo INTEGER NOT NULL, precio_cuota INTEGER NOT NULL, fecha_entrega VARCHAR(14) NOT NULL,cuil_empleado INTEGER NOT NULL, KEY dnisolicitante_dni_clientes_00_idx (dni_cliente), CONSTRAINT dnisolicitante_dni_clientes_00 FOREIGN KEY (dni_cliente) REFERENCES clientes (dni), KEY cuil_empleado_cuil_empleados_01_idx (cuil_empleado), CONSTRAINT cuil_empleado_cuil_empleados_01 FOREIGN KEY (cuil_empleado) REFERENCES empleados (cuil))'
    try:
        consulta.execute(sql)
        print('La tabla prestamos se encuentra disponible')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla prestamos: ", e)
    #crear tabla empleados
    sql = 'CREATE TABLE IF NOT EXISTS empleados(cuil INTEGER PRIMARY KEY NOT NULL, nombre VARCHAR(30) NOT NULL)'
    try:
        consulta.execute(sql)
        print('La tabla empleados se encuentra disponible')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla empleados: ", e)
    #crear tabla cuotas_prestamos 
    sql = 'CREATE TABLE IF NOT EXISTS cuotas_prestamos(numero_prestamo INTEGER NOT NULL, numero_cuota INTEGER NOT NULL, fecha VARCHAR(14) NOT NULL, precio_pagado INTEGER NOT NULL, cuil_empleado INTEGER NOT NULL, PRIMARY KEY (numero_prestamo, numero_cuota),KEY numerp_prestamo_couta_prestamo_numero_prestamo_prestamo_02_idx (numero_prestamo), CONSTRAINT numerp_prestamo_couta_prestamo_numero_prestamo_prestamo_02 FOREIGN KEY (numero_prestamo) REFERENCES prestamos (numero_prestamo), KEY cuil_empleado_cuil_empleados_04_idx (cuil_empleado), CONSTRAINT cuil_empleado_cuil_empleados_04 FOREIGN KEY (cuil_empleado) REFERENCES empleados (cuil))'
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

def get_all_data_empleados():
    try:
        connection = pymysql.connect(host=host_name,
                                    user=user_name,
                                    password=password_name,
                                    db=db_name)
        sql_select_Query = "select * from empleados Order by nombre"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        lista_resultado = cursor.fetchall()
        if lista_resultado == ():
            print("No hay empleados...")
        for row in lista_resultado:
            print('[[+]nombre:',row[0],'\n[+]cuil:',row[1],"\n----------") 
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error reading data from MySQL table", e)
    finally:
        connection.close()
        cursor.close()

def buscar_empleado(cuil):
    try:
        conexion = pymysql.connect(host=host_name, 
                                    user=user_name,      
                                    password=password_name,
                                    db=db_name)
        try:
            with conexion.cursor() as cursor:
                consulta = 'SELECT * FROM empleados WHERE cuil = %s'
                cursor.execute(consulta, cuil)
                lista_contactos = cursor.fetchall()
                if lista_contactos == ():
                    print('empleado no encontrado')
                for lista in lista_contactos:
                    print(lista)
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error consultando la tabla:", e)

def agregar_empleados(cuil, nombre):
    conexion = pymysql.connect(host=host_name, 
                                user=user_name,      
                                password=password_name,
                                db=db_name)
    consulta = conexion.cursor()
    datos = (cuil, nombre)
    sql_select_Query = 'INSERT INTO empleados(cuil, nombre) VALUES (%s,%s)'
    try:
        consulta.execute(sql_select_Query, datos)
        print("Datos guardados con exito")
    except:
        print("Ocurrió un error al intentar guardar los datos")
    conexion.commit()
    conexion.close()

def actualizar_empleados(cuil, nombre, buscar):
    conexion = pymysql.connect(host=host_name,
                                user=user_name,
                                password=password_name,
                                db=db_name)
    consulta = conexion.cursor()
    sql_select_Query = 'UPDATE empleados SET cuil = %s, nombre = %s WHERE (cuil = %s)'
    datos = (cuil, nombre, buscar)
    print(datos)
    try:
        consulta.execute(sql_select_Query, datos)
        print("Datos modificados con exito")
    except:
        print("Ocurrió un error al intentar guardar los datos")
    conexion.commit()

    consulta.close()
    conexion.close()

def eliminar_empleado(cuil):
    try:
        conexion = pymysql.connect(host=host_name, 
                                    user=user_name,      
                                    password=password_name,
                                    db=db_name)
        try:
            with conexion.cursor() as cursor:
                sql_select_Query = 'DELETE FROM empleados WHERE cuil= %s'
                cursor.execute(sql_select_Query, cuil)
                print('empleado eliminado')
        finally:
            conexion.commit()
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error consultando la tabla:", e)

def get_all_data_cuotas_prestamos():
    try:
        connection = pymysql.connect(host=host_name,
                                    user=user_name,
                                    password=password_name,
                                    db=db_name)
        sql_select_Query = "select * from cuotas_prestamos Order by numero_prestamo"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        lista_resultado = cursor.fetchall()
        if lista_resultado == ():
            print("No hay cuotas de prestamos...")
        for row in lista_resultado:
            print('[+]numero_prestamo:',row[0],'\n[+]numero_cuota:',row[1],'\n[+]fecha:',row[2],'\n[+]precio_pagado:',row[3],'\n[+]cuil_empleado:',row[4],"\n----------") 
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error reading data from MySQL table", e)
    finally:
        connection.close()
        cursor.close()

def buscar_cuota_prestamo(numero_prestamo):
    try:
        conexion = pymysql.connect(host=host_name, 
                                    user=user_name,      
                                    password=password_name,
                                    db=db_name)
        try:
            with conexion.cursor() as cursor:
                consulta = 'SELECT * FROM cuotas_prestamos WHERE numero_prestamo = %s'
                cursor.execute(consulta, numero_prestamo)
                lista_contactos = cursor.fetchall()
                if lista_contactos == ():
                    print('cuota prestamo no encontrado')
                for lista in lista_contactos:
                    print(lista)
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error consultando la tabla:", e)

def agregar_cuotas_prestamos(numero_prestamo, numero_cuota, fecha, precio_pagado, cuil_empleado):
    conexion = pymysql.connect(host=host_name, 
                                user=user_name,      
                                password=password_name,
                                db=db_name)
    consulta = conexion.cursor()
    datos = (numero_prestamo, numero_cuota, fecha, precio_pagado, cuil_empleado)
    sql_select_Query = 'INSERT INTO cuotas_prestamos(numero_prestamo, numero_cuota, fecha, precio_pagado, cuil_empleado) VALUES (%s,%s,%s,%s,%s)'
    try:
        consulta.execute(sql_select_Query, datos)
        print("Datos guardados con exito")
    except:
        print("Ocurrió un error al intentar guardar los datos")
    conexion.commit()
    conexion.close()

def actualizar_cuotas_prestamos(numero_prestamo, numero_cuota, fecha, precio_pagado, cuil_empleado,buscar0,buscar1):
    conexion = pymysql.connect(host=host_name,
                                user=user_name,
                                password=password_name,
                                db=db_name)
    consulta = conexion.cursor()
    sql_select_Query = 'UPDATE cuotas_prestamos SET numero_prestamo = %s, numero_cuota = %s, fecha = %s, precio_pagado = %s, cuil_empleado = %s WHERE numero_prestamo = %s and numero_cuota = %s'
    datos = (numero_prestamo, numero_cuota, fecha, precio_pagado, cuil_empleado,buscar0,buscar1)
    try:
        consulta.execute(sql_select_Query, datos)
        print("Datos modificados con exito")
    except:
        print("Ocurrió un error al intentar guardar los datos")
    conexion.commit()
    conexion.close()
    consulta.close()

def eliminar_cuota_prestamo(numero_prestamo, numero_cuota):
    try:
        conexion = pymysql.connect(host=host_name, 
                                    user=user_name,      
                                    password=password_name,
                                    db=db_name)
        try:
            with conexion.cursor() as cursor:
                print("borrando ...")
                datos = (numero_prestamo, numero_cuota)
                sql_select_Query = 'DELETE FROM cuotas_prestamos WHERE (numero_prestamo = %s) AND (numero_cuota = %s)'
                cursor.execute(sql_select_Query, datos)
                print('cuota_prestamo eliminado')
        finally:
            conexion.commit()
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error consultando la tabla:", e)

def get_all_data_prestamos():
    try:
        connection = pymysql.connect(host=host_name,
                                    user=user_name,
                                    password=password_name,
                                    db=db_name)
        sql_select_Query = "select * from prestamos Order by numero_prestamo"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        lista_resultado = cursor.fetchall()
        if lista_resultado == ():
            print("No hay cuotas de prestamos...")
        for row in lista_resultado:
            print('[+]numero_prestamo:',row[0],'\n[+]dni_cliente:',row[1],'\n[+]fecha_autorizacion:',row[2],'\n[+]fecha_tentativa:',row[3],'\n[+]cantidad_de_cuotas:',row[4],'\n[+]monto_prestamo:',row[5],'\n[+]precio_cuota:',row[6],'\n[+]fecha_entrega:',row[7],'\n[+]cuil_empleado:',row[8],"\n----------") 
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error reading data from MySQL table", e)
    finally:
        connection.close()
        cursor.close()

def buscar_prestamo(numero_prestamo):
    try:
        conexion = pymysql.connect(host=host_name, 
                                    user=user_name,      
                                    password=password_name,
                                    db=db_name)
        try:
            with conexion.cursor() as cursor:
                consulta = 'SELECT * FROM prestamos WHERE numero_prestamo = %s'
                cursor.execute(consulta, numero_prestamo)
                lista_contactos = cursor.fetchall()
                if lista_contactos == ():
                    print('prestamo no encontrado')
                for lista in lista_contactos:
                    print(lista)
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error consultando la tabla:", e)

def agregar_prestamos(numero_prestamo, dni_cliente, fecha_autorizacion , fecha_tentativa, cantidad_de_cuotas, monto_prestamo, precio_cuota, fecha_entrega, cuil_empleado):
    conexion = pymysql.connect(host=host_name, 
                                user=user_name,      
                                password=password_name,
                                db=db_name)
    consulta = conexion.cursor()
    datos = (numero_prestamo, dni_cliente, fecha_autorizacion , fecha_tentativa, cantidad_de_cuotas, monto_prestamo, precio_cuota, fecha_entrega, cuil_empleado)
    sql_select_Query = 'INSERT INTO prestamos(numero_prestamo, dni_cliente, fecha_autorizacion , fecha_tentativa, cantidad_de_cuotas, monto_prestamo, precio_cuota, fecha_entrega, cuil_empleado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
        consulta.execute(sql_select_Query, datos)
        print("Datos guardados con exito")
    except:
        print("Ocurrió un error al intentar guardar los datos")
    conexion.commit()
    conexion.close()

def actualizar_prestamos(numero_prestamo, dni_cliente, fecha_autorizacion , fecha_tentativa, cantidad_de_cuotas, monto_prestamo, precio_cuota, fecha_entrega, cuil_empleado, buscar):
    conexion = pymysql.connect(host=host_name,
                                user=user_name,
                                password=password_name,
                                db=db_name)
    consulta = conexion.cursor()
    sql_select_Query = 'UPDATE prestamos SET numero_prestamo = %s, dni_cliente = %s, fecha_autorizacion = %s, fecha_tentativa = %s,cantidad_de_cuotas = %s, monto_prestamo = %s, precio_cuota = %s, fecha_entrega = %s, cuil_empleado = %s WHERE numero_prestamo = %s '
    datos = (numero_prestamo, dni_cliente, fecha_autorizacion , fecha_tentativa, cantidad_de_cuotas, monto_prestamo, precio_cuota, fecha_entrega, cuil_empleado, buscar)
    try:
        consulta.execute(sql_select_Query, datos)
        print("Datos modificados con exito")
    except:
        print("Ocurrió un error al intentar guardar los datos")
    conexion.commit()
    conexion.close()
    consulta.close()

def eliminar_prestamo(numero_prestamo):
    try:
        conexion = pymysql.connect(host=host_name, 
                                    user=user_name,      
                                    password=password_name,
                                    db=db_name)
        try:
            with conexion.cursor() as cursor:
                print("borrando ...")
                datos = (numero_prestamo)
                sql_select_Query = 'DELETE FROM prestamos WHERE numero_prestamo = %s'
                cursor.execute(sql_select_Query, datos)
                print('cuota_prestamo eliminado')
        finally:
            conexion.commit()
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error consultando la tabla:", e)