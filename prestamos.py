import pymysql
from bdprestamos import*

def crear_instancia_cuotas_prestamos():
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
            numero_cuota = int(input('ingrese el numero de la cuota: '))
            if (numero_cuota != 0) and (numero_cuota < 7):
                break
        except:
            print('intente de nuevo')
    fecha = input('ingrese la fecha del pago: ')
    while True:
        try:
            precio_pagado = int(input('ingrese la cantidad del pago: '))
            if (precio_pagado > 0):
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
    return cuotas_prestamos(numero_prestamo, numero_cuota, fecha, precio_pagado, cuil_empleado)

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
    return prestamos(numero_prestamo, dni_cliente , fecha_autorizacion, fecha_tentativa, cantidad_cuotas, monto, precio_cuota, fecha_entrega, cuil_empleado)

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

class cuotas_prestamos:
    def __init__(self,numero_prestamo,numero_cuota,fecha,precio_pagado,cuil_empleado):
        self.numero_prestamo = numero_prestamo
        self.numero_cuota = numero_cuota
        self.fecha = fecha
        self.precio_pagado = precio_pagado
        self.cuil_empleado = cuil_empleado

    def registrar_pago(self):
        agregar_cuotas_prestamos(self.numero_prestamo,self.numero_cuota,self.fecha,self.precio_pagado,self.cuil_empleado)

    def eliminar(self):
        eliminar_cuota_prestamo(self.numero_prestamo,self.numero_cuota)

    def listar(self):
        get_all_data_cuotas_prestamos()

    def modificar(self,buscar0,buscar1):
        actualizar_cuotas_prestamos(self.numero_prestamo,self.numero_cuota,self.fecha,self.precio_pagado,self.cuil_empleado,buscar0,buscar1)

class clientes:
    def __init__(self,dni,nombres,apellidos,telefono,celular):
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.celular = celular

    def eliminar(self):
        eliminar_cliente(self.dni)

    def listar(self):
        get_all_data_clientes()

    def modificar(self,buscar):
        update_data_cliente(self.dni,self.nombres,self.apellidos,self.telefono,self.celular,buscar)

    def registrar_cliente(self):
        agregar_cliente(self.dni,self.nombres,self.apellidos,self.telefono,self.celular)

class empleados:
    def __init__(self,nombre,cuil):
        self.nombre = nombre
        self.cuil = cuil
    
    def listar(self):
        get_all_data_empleados()
    
    def nuevo(self):
        agregar_empleados(self.cuil,self.nombre)

    def eliminar(self):
        eliminar_empleado(self.cuil)

    def modificar(self,buscar):
        actualizar_empleados(self.cuil, self.nombre,buscar)

class prestamos:
    def __init__(self,numero_prestamo, dni_cliente, fecha_autorizacion , fecha_tentativa, cantidad_de_cuotas, monto_prestamo, precio_cuota, fecha_entrega, cuil_empleado):
        self.numero_prestamo = numero_prestamo
        self.dni_cliente = dni_cliente
        self.fecha_autorizacion = fecha_autorizacion
        self.fecha_tentativa = fecha_tentativa
        self.cantidad_de_cuotas = cantidad_de_cuotas
        self.monto_prestamo = monto_prestamo
        self.precio_cuota = precio_cuota
        self.fecha_entrega = fecha_entrega
        self.cuil_empleado = cuil_empleado
    def verificar_monto(self):
        pass
    def registrar_prestamo(self):
        agregar_prestamos(self.numero_prestamo,self.dni_cliente,self.fecha_autorizacion,self.fecha_tentativa,self.cantidad_de_cuotas,self.monto_prestamo,self.precio_cuota,self.fecha_entrega,self.cuil_empleado)
    def modificar(self,numero_prestamo):
        actualizar_prestamos(self.numero_prestamo,self.dni_cliente,self.fecha_autorizacion,self.fecha_tentativa,self.cantidad_de_cuotas,self.monto_prestamo,self.precio_cuota,self.fecha_entrega,self.cuil_empleado,self.numero_prestamo) 
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
        ['11. Salir del sistema'],
        ['12. lista de cuotas'],
        ['13. agregar cuota'],
        ['14. buscar cuota'],
        ['15. modificar cuota'],
        ['16. eliminar cuota'],
        ['17. lista de prestamos'],
        ['18. agregar prestamo'],
        ['19. buscar prestamo'],
        ['20. modificar prestamo'],
        ['21. eliminar prestamo'],
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
        buscar = input('ingrese el cliente a buscar: ')
        x = crear_instancia_clientes()
        x.modificar(buscar)
    elif opcion == 5:
        buscar = input('ingrese el cliente a buscar: ')
        buscar_cliente_nombres(buscar)
        controlardatos = input('SEGURO DESEA BORRAR LOS DATOS "1" para continuar: ')
        if controlardatos == "1":    
            eliminar_cliente(buscar)
    elif opcion == 6:
        get_all_data_empleados()
    elif opcion == 7:
        x=crear_instancia_empleados()
        x.nuevo()
    elif opcion == 8:
        buscar = input('ingrese el cuil del empleado a buscar: ')
        buscar_empleado(buscar)
    elif opcion == 9:
        buscar = input('ingrese el cuil del empleado a buscar: ')
        x = crear_instancia_empleados()
        x.modificar(buscar)
    elif opcion == 10:
        buscar = input('ingrese el empleado a buscar: ')
        buscar_empleado(buscar)
        controlardatos = input('SEGURO DESEA BORRAR LOS DATOS "1" para continuar: ')
        if controlardatos == "1":    
            eliminar_empleado(buscar)
    elif opcion == 11:
        print("Saliendo del sistema ...")
        exit()
    elif opcion == 12:
        get_all_data_cuotas_prestamos()
    elif opcion == 13:
        x = crear_instancia_cuotas_prestamos()
        x.registrar_pago()
    elif opcion == 14:
        buscar = int(input('ingrese el numero del prestamo a buscar: '))
        buscar_cuota_prestamo(buscar)
    elif opcion == 15:      
        buscar0 = input('ingrese el numero del prestamo a buscar: ')
        buscar1 = input('ingrese el numero de la cuota a buscar: ')
        x = crear_instancia_cuotas_prestamos()
        x.modificar(buscar0,buscar1)
    elif opcion == 16:
        buscar0 = input('ingrese el numero de prestamo a buscar: ')
        buscar1 = input('ingrese el numero de la cuota a buscar: ')
        buscar_cuota_prestamo(buscar0)
        controlardatos = input('SEGURO DESEA BORRAR LOS DATOS "1" para continuar: ')
        if controlardatos == "1":    
            eliminar_cuota_prestamo(buscar0,buscar1)
    elif opcion == 17:
        get_all_data_prestamos()
    elif opcion == 18:
        x = crear_instancia_prestamos()
        x.registrar_prestamo()
    elif opcion == 19:
        buscar = int(input('ingrese el numero del prestamo a buscar: '))
        buscar_prestamo(buscar)
    elif opcion == 20:      
        buscar = input('ingrese el numero del prestamo a buscar: ')
        x = crear_instancia_prestamos()
        x.modificar(buscar)
    elif opcion == 21:
        buscar = input('ingrese el numero de prestamo a buscar: ')
        buscar_prestamo(buscar)
        controlardatos = input('SEGURO DESEA BORRAR LOS DATOS "1" para continuar: ')
        if controlardatos == "1":    
            eliminar_prestamo(buscar)
    
