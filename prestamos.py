import pymysql
from bdprestamos import*

def crear_instancia_cuota_prestamo():
    print('datos de cuota de un prestamo ')
    while True:
        try:
            numero_prestamo = int(input('ingrese el numero de prestamo: '))
            if (numero_prestamo != 0):
                break
        except:
            print('intente de nuevo')
    while True:
        try:
            numero_cuota = int(input('ingrese el numero de prestamo: '))
            if (numero_cuota != 0) and (numero_cuota < 7):
                break
        except:
            print('intente de nuevo')
    fecha = input('ingrese la fecha del pago: ')
    while True:
        try:
            precio = int(input('ingrese el numero de prestamo: '))
            if (precio > 0):
                break
        except:
            print('intente de nuevo')
    while True:
        try:
            cuil_empleado = int(input('ingrese el cuil del empleado: '))
            if (cuil_empleado > 0):
                break
        except:
            print('intente de nuevo')
    return pago_coutas(numero_prestamo, numero_cuota, fecha, precio, cuil_empleado)

def crear_instancia_prestamos():
    print('datos del prestamo ')
    while True:
        try:
            numero_prestamo = int(input('ingrese el numero de prestamo: '))
            if (numero_prestamo != 0):
                break
        except:
            print('intente de nuevo')
    while True:
        try:
            dni_cliente = int(input('ingrese el dni del cliente: '))
            if (dni_cliente > 0):
                break
        except:
            print('intente de nuevo')
    fecha_autorizacion = input('ingrese  la fecha de autorizacion: ')
    while True:
        try:
            monto = int(input('ingrese el monto del prestamo: '))
            if (monto > 0):
                break
        except:
            print('intente de nuevo')
    while True:
        try:
            cantidad_cuotas = int(input('ingrese la cantidad de cuotas del prestamo: '))
            if (cantidad_cuotas < 7) and (cantidad_cuotas > 0):
                break
        except:
            print('intente de nuevo')
    while True:
        try:
            precio_cuota = int(input('ingrese el precio de las cuotas: '))
            if (precio_cuota > 0):
                break
        except:
            print('intente de nuevo')
    fecha_tentativa = input('ingrese la fecha tentativa: ')
    fecha_entrega = input('ingrese la fecha de entrega: ')
    while True:
        try:
            cuil_empleado = int(input('ingrese el cuil del empleado: '))
            if (cuil_empleado > 0):
                break
        except:
            print('intente de nuevo')
    return prestamos(numero_prestamo, fecha_autorizacion, monto, cantidad_cuotas, precio_cuota, fecha_tentativa, fecha_entrega, cuil_empleado)

def crear_instancia_empleados():
    print('datos del empleado ')
    nombre = input('ingrese el nombre: ')
    while True:
        try:
            cuil = int(input('ingrese cuil: '))
            break
        except:
            print('intente de nuevo')
    return empleados(nombre, cuil)

def crear_instancia_clientes():
    print('datos del cliente ')
    while True:
        try:
            dni = int(input('ingrese dni: '))
            break
        except:
            print('intente de nuevo')
    nombres = input('ingrese nombre/s: ')
    apellidos = input ('ingrese apellido/s: ')
    while True:
        try:
            telefono = int(input('ingrese telefono: '))
            break
        except:
            print('intente de nuevo')
    while True:
        try:
            celular = int(input('ingrese celular: '))
            break
        except:
            print('intente de nuevo')
    clientes(dni, nombres, apellidos,telefono,celular)
    return clientes(dni, nombres, apellidos,telefono,celular)

class pago_coutas:
    def __init__(self,numero_prestamo,numero_cuota,fecha_pago,monto_pagado,cuil_empleado):
        self.numero_prestamo = numero_prestamo
        self.numero_cuota = numero_cuota
        self.fecha_pago = fecha_pago
        self.monto_pagado = monto_pagado
        self.cuil_empleado = cuil_empleado
    def registrar_pago(self):
        print()

class clientes:
    def __init__(self,dni,nombres,apellidos,telefono,celular):
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.celular = celular

    def baja(self):
        eliminar_cliente(self.dni)

    def listar(self):
        get_all_data_clientes()

    def modificar(self):
        update_data_cliente(self.dni,self.nombres,self.apellidos,self.telefono,self.celular,self.dni)

    def registrar_cliente(self):
        agregar_cliente(self.dni,self.nombres,self.apellidos,self.telefono,self.celular)

class empleados:
    def __init__(self,nombre,cuil):
        self.nombre = nombre
        self.cuil = cuil
    
    def listar(self):
        get_all_data_empleados()
    
class prestamos:
    def __init__(self, numero_prestamo, fecha_autorizacion, monto, cantidad_cuotas, precio_cuota, fecha_tentativa, fecha_entrega,cuil_empleado):
        self.numero_prestamo = numero_prestamo
        self.fecha_autorizacion = fecha_autorizacion
        self.monto = monto
        self.cantidad_cuotas = cantidad_cuotas
        self.precio_cuota = precio_cuota
        self.fecha_tentativa = fecha_tentativa
        self.fecha_entrega = fecha_entrega
        self.cuil_empleado = cuil_empleado
    def verificar_monto(self):
        pass
    def registrar_prestamo(self):
        pass
    def modificar(self):
        pass 
    def calcular_fechapago(self):
        pass 
    def calcular_fechatentativa(self):
        pass 
    def autorizar_prestamo(self):
        pass 
    def calcular_fechaentrega(self):
        pass 
    def consultar_cliente(self):
        pass 


create_tablas()
opcion = 0
while (opcion != 11):
    print()
    menu = [
        ['sistema de prestamos'],
        ['1. Lista de cliente'],
        ['2. Agregar de cliente'],
        ['3. Buscar cliente'],
        ['4. Modificar cliente'],
        ['5. Eliminar cliente'],
        ['6. Lista de empleado'],
        ['7. Agregar de empleado'],
        ['8. Buscar empleado'],
        ['9. Modificar empleado'],
        ['10. Eliminar empleado'],
        ['11. Salir del sistema']
    ]
    for x in range(len(menu)):
        print(menu[x])
    opcion = int(input("Introduzca la opción deseada: "))
    if opcion == 1:
        get_all_data_clientes()
    elif opcion == 2:
        x=crear_instancia_clientes()
        x.registrar_cliente()
    elif opcion == 3:
        buscar = input('ingrese el cliente a buscar: ')
        buscar_cliente_nombres(buscar)
    elif opcion == 4:
        modificar = input('ingrese el cliente a modificar: ')
        x = crear_instancia_clientes()
        update_data_cliente(x.dni,x.nombres,x.apellidos,x.telefono,x.celular,modificar)
    elif opcion == 5:
        buscar = input('ingrese el cliente a buscar: ')
        buscar_cliente_nombres(buscar)
        controlardatos = input('SEGURO DESEA BORRAR LOS DATOS "1" para continuar: ')
        if controlardatos == "1":    
            eliminar_cliente(buscar)
        print('hola')
    elif opcion == 11:
        print("Saliendo del sistema ...")
        exit()

