import os
import decimal
salir=False
datos=0
cod=0
total=0
cantidad=0
producto_carro=0

productos= {
    "001" : {
        "codigo" : "001",
        "nombre" : "Air Force 1",
        "marca": "nike",
        "color": "verde militar",
        "precio": 5800.50,
        "stock": 10,
        "talle": "35",

    },
    "002" : {
        "codigo" : "002",
        "nombre" : "Dunk",
        "marca": "adidas",
        "color": "rosa",
        "precio": 20000.30,
        "stock": 10,
        "talle": "36",

    },
    "003" : {
        "codigo" : "003",
        "nombre" : "Air Max 90",
        "marca": "Nike",
        "color": "celeste",
        "precio": 18000.50,
        "stock": 6,
        "talle": "35",

    },
    "004" : {
        "codigo" : "004",
        "nombre" : "ARCADE LOW",
        "marca": "Fila",
        "color": "negra",
        "precio": 15000,
        "stock": 7,
        "talle": "40",

    },
    "005" : {
        "codigo" : "005",
        "nombre" : "AIR NFH",
        "marca" : "Jordan",
        "color": "gris",
        "precio" : 20000,
        "stock" : 15,
        "talle" : "40",

},
    "006" : {
        "codigo" : "006",
        "nombre" : "ORIGINALS SUPERSTAR",
        "marca": "Adidas",
        "color": "naranja",
        "precio": 16000,
        "stock": 8,
        "talle": "38",

    },
}
carrito={}

def mostrar_productos(productos):
    print ("Los productos que ofrecemos son: ")
    for key, value in productos.items():
        print()
        print("Codigo:", productos[key]["codigo"])
        print("Nombre:", productos[key]["nombre"])
        print("Marca:", productos[key]["marca"])
        print("Color:", productos[key]["color"])
        print("Precio: $", productos[key]["precio"])
        print("Stock:", productos[key]["stock"])
        print("Talle:", productos[key]["talle"])
        print()

def mostrar_productos_breve(productos):
    print ("Información breve: ")
    for key, value in productos.items():
        
        print("Codigo:", productos[key]["codigo"])
        print("Nombre:", productos[key]["nombre"])
        print("Precio: $", productos[key]["precio"])
        print("Stock:", productos[key]["stock"])
        print()

def buscarProducto(cod, productos):
    while(True):
        for key, value in productos.items():

            if cod==key:
                
                print("")
                print ("Producto encontrado:")
                print("Nombre:", productos[key]["nombre"])
                print("Marca:", productos[key]["marca"])
                print("Precio: $", productos[key]["precio"])
                print("Stock:", productos[key]["stock"])
                print("Talle:", productos[key]["talle"])
                print("")

                return
        cod = input("El producto que desea buscar no existe, vuelva a introducir otro codigo: ")

def validar_opcion(opcion):
    while(True):
        if opcion.isnumeric():
            opcion =int(opcion)
            if opcion<6 and opcion>0:
                return opcion
            else:
                opcion= input("La opción ingresada no es correcta, vuelva a ingresar otra opción: ")  
            

        else:
            opcion= input("La opcion ingresada no es un numero, vuelva a ingresar otra opción: ")


#FALATA VALIDAR LA LA CANTIDAD
def agregar_al_carrito(carrito):
        cod=input("Ingrese el código del producto que desea añadir a su carrito: ")
        if cod in productos:       
            producto=productos[cod]
            cantidad=int(input("Ingrese la cantidad que desea de este producto: "))
            if cantidad <= producto["stock"]:
                if cod in carrito:
                    carrito[cod]["cantidad"]+= cantidad
                    carrito[cod]["costo_total"] += cantidad * producto["precio"]
                else:
                    carrito[cod]={
                        "nombre" : producto["nombre"],
                        "cantidad" : cantidad,
                        "precio_unitario" : producto["precio"],
                        "costo_total" : cantidad * producto["precio"]
                    }
                producto["stock"] -= cantidad
                print("Producto agregado al carrito ")
            else: 
                print("La cantidad que usted solicita no esta disponible ")
        else:
            print("No se encontró un producto con ese codigo ")

#funcion para mostrar el carrito armado por los clientes
def ver_carrito():
    if len(carrito)>0:
        print("Productos de  tu carrito: ")
        total=0
        for codigo, producto in carrito.items():
            nombre_producto= producto ["nombre"]
            cantidad=producto ["cantidad"]
            precio_unitario= producto ["precio_unitario"] 
            costo_total = producto ["costo_total"]
            print("")
            print("-"*25)
            print("Codigo del Producto:", codigo)
            print("Nombre del Producto:", nombre_producto)
            print("cantidad: ", cantidad )
            print("Precio Unitario: $", precio_unitario)
            print("Costo Total: $", costo_total)
            print("-"*25)
            total += costo_total
        print("El costo total de su compra es: $", total)
    else:
        print("Su carrito se encuentra vacio")


def validar_opcion_menu(opcion_menu):
    while True:
        if opcion_menu.isdigit() and int(opcion_menu) in range(1, 6):
            return int(opcion_menu)
        else:
            opcion_menu=input("EROR: opción invalida, ingrese nuevamente: ")

def validar_codigo_producto(codigo, producto):
    while True:
        if codigo in productos:
            return codigo
        else:
            codigo=input("EROR: opción invalida, ingrese nuevamente: ")

def validar_codigo_producto(codigo, productos):
    while True:
        if codigo in productos:
            return codigo
        else:
            codigo=input("EROR: opción invalida, ingrese nuevamente: ")


def validar_cantidad(cantidad):
    while True:
        if cantidad.isdigit() and int(cantidad)>0:
            return int(cantidad)
        else:
            cantidad=input("EROR: opción invalida, ingrese nuevamente: ")




def modificar_carrito():
    opcion=int(input("""
¿Desea modificar el carrito? (Ingrese números, no letras)
1)si
2)no
"""))

    if opcion==1:
        print (""" 
1)Modificar cantidad
2)Eliminar producto
""")
        
        opcion2=validar_opcion_menu(input("Ingrese el número de la acción que desea realizar: "))

        if opcion2==1:
            codigo = str(input("Ingrese el código del producto que quiere aumentar el stock: "))
            codigo=validar_codigo_producto(codigo, carrito)

            if codigo in carrito:
                producto= carrito[codigo]
                cantidad_actualizada=validar_cantidad(input("Ingrese la nueva cantidad: "))

                if cantidad_actualizada>0:
                    producto["cantidad"]=cantidad_actualizada
                    producto["costo_total"]= producto["precio_unitario"]*cantidad_actualizada
                    print("Cantidad modificada correctamente ")
                else:
                    print("La cantidad debe ser mayor a 0")
            else: 
                print("El producto no existe ")
        elif opcion2==2:
            codigo= input("Ingrese el codigo del producto que desea eliminar ")
            codigo=validar_codigo_producto(codigo, carrito)

            if codigo in carrito:
                productos[codigo]["stock"] += carrito[codigo]["cantidad"]
                del carrito [codigo]
                print("El producto fue eliminado correctamente de su carrito")
        else: 
            print("su respuesta es invalida ")
                
    elif opcion==2:
        finalizar= int(input("""
Desea finalizar la compra? ("Ingrese número, no letras)
1)si
2)No
"""))
        if finalizar==1:
            print("Muchas gracias por su visita ")

    else:
        print("su respuesta es invalida ")





while salir==False:
    print (""" Bienvenido a tienda SHOES:
    1)Mostrar productos en detalle
    2)ver producto por código
    3)Agregar productos al carrito
    4)Mostrar carrito
    5)Salir      
    """)
    
    opcion= validar_opcion(input("Ingrese una opción: "))
    
    if opcion == 1:
        print()
        mostrar_productos(productos)
    if opcion ==2:
        buscarProducto(input("Ingrese el código del producto a buscar: "),productos)
        #asi llamo una función
        continuar = input("Ingrese ENTER para continuar")
        #limpiar pantalla
        os.system("cls")

    if opcion == 3: #agregar productos al carrito
        agregar_al_carrito(carrito)
        continuar = input("Ingrese ENTER para continuar")
        os.system("cls")
    if opcion==4:#realizar la compra si es que hay productos en el carrito
        ver_carrito()
        print("")
        modificar_carrito()
        continuar = input("Ingrese ENTER para continuar")
        os.system("cls")
        print("")
    if opcion==5:
        print("Gracias por la visita")
        salir=True

