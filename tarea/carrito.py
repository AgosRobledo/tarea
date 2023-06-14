import os

salir=False
datos=0
cod=0
productos= {
    "11" : {
        "nombre" : "Air Force 1",
        "marca": "nike",
        "precio": 5800.50,
        "stock": 10,
        "talle": "35",

    },
    "12" : {
        "nombre" : "Dunk",
        "marca": "adidas",
        "precio": 20000.30,
        "stock": 10,
        "talle": "36",

    },
    "13" : {
        "nombre" : "Air Max 90",
        "marca": "Nike",
        "precio": 18000.50,
        "stock": 6,
        "talle": "35",

    },
    "14" : {
        "nombre" : "ARCADE LOW",
        "marca": "Fila",
        "precio": 15000,
        "stock": 7,
        "talle": "40",

    },
    "15" : {
        "nombre" : "AIR NFH",
        "marca" : "Jordan",
        "precio" : 20000,
        "stock" : 15,
        "talle" : "40",

},
    "16" : {
        "nombre" : "ORIGINALS SUPERSTAR",
        "marca": "Adidas",
        "precio": 16000,
        "stock": 8,
        "talle": "38",

    },
}
carrito={}

primer_producto = productos["11"]
segundo_producto = productos["12"]
tercero_producto = productos["13"]
cuarto_producto = productos["14"]
quinto_producto = productos["15"]
sexto_producto = productos["16"]

def mostrar_productos(productos):
    print ("Los productos que ofrecemos son: ")
    for key, value in productos.items():
        
        print("Nombre:", productos[key]["nombre"])
        print("Marca:", productos[key]["marca"])
        print("Precio: $", productos[key]["precio"])
        print("Stock:", productos[key]["stock"])
        print("Talle:", productos[key]["talle"])
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
            if opcion<5 and opcion>0:
                return opcion
            else:
                opcion= input("La opcion ingresada no es correcta, vuelva a ingresar otra opción: ")    
            #validar que las primeras opciones sean correctas
        else:
            opcion= input("La opcion ingresada no es un numero, vuelva a ingresar otra opción: ")






while (salir==False):
    print (""" Bienvenido a tienda SHOES:
    1)mostrar productos en detalle
    2)ver producto por codigo
    3)realizar compra
    4)finalizar compra
    5)salir
    """)
    
    opcion= validar_opcion(input("Ingrese una opción: "))
    
    #como limpiar pantalla
    if opcion == 1:
        print()
        mostrar_productos(productos)
    if opcion ==2:
        buscarProducto(input("Ingrese el codigo del producto a buscar: "),productos)
        #asi llamo una función
        continuar = input("Ingrese ENTER para continuar")
        os.system("cls")
    

    if opcion == 3:
        cod = input ("Ingrese el producto que desea agregar a su carrito ")
        cantidad =int(input("Cantidad:"))
        #agregar producto a un nuevo diccionario
        #y 




"""#funcion para mostrar los datos del diccionario en pantalla
def imprimir_datos(productos):
    for key in productos.items():
        print("Nombre:",key)
        print("Marca:",productos[key]["marca"])
        print("Precio: $",productos[key]["precio"])
        print("Stock:",productos[key]["stock"])
        print("Talle:",productos[key]["talle"])
        print()
        imprimir_datos(productos)
        
#preguntar como hago para llamar a una función

def imprimir_lista(datos):
    for i in range (len(datos)):

        print("Nombre: ", datos[i]["nombre"])
        print("Marca: ", datos[i]["marca"])
        print("Precio: $", datos[i]["precio"])
        print("Stock: ", datos[i]["stock"])
        print("Talle: ", datos[i]["talle"])
        imprimir_lista(datos)"""