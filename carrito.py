salir=False
datos=0
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
    "15" : ([
        ("nombre" , "AIR NFH"),
        ("marca" , "Jordan"),
        ("precio" , 20000),
        ("stock" , 15),
        ("talle" , "40"),

    ]),
    "16" : {
        "nombre" : "ORIGINALS SUPERSTAR",
        "marca": "Adidas",
        "precio": 16000,
        "stock": 8,
        "talle": "38",

    },
}

primer_producto = productos["11"]
segundo_producto = productos["12"]
tercero_producto = productos["13"]
cuarto_producto = productos["14"]
quinto_producto = productos["15"]
sexto_producto = productos["16"]

while (salir==False):
    print (""" Bienvenido a tienda SHOES:
    1)mostrar productos en detalle
    2)ver producto por codigo
    3)realizar compra
    4)finalizar compra
    5)salir
    """)
    opcion= int(input("Ingrese una opción: "))
    #como limpiar pantalla
    if opcion == 1:
        #como hacer para que salga ordenado y sin llaves
        for i in productos:
            print (productos)
    if opcion ==2:
        cod = input ("Ingresa el código de la zapatilla que deseas ver: ")
        if cod==11:
            #algo anda mallllllllll, validar, el primer print
            print ("Producto encontrado:")
        print("Nombre:", primer_producto["nombre"])
        print("Marca:", primer_producto["marca"])
        print("Precio: $", primer_producto["precio"])
        print("Stock:", primer_producto["stock"])
        print("Talle:",primer_producto["talle"])

        if cod==12:
            #algo anda mallllllllll, validar, el primer print
            print ("Producto encontrado:")
        print("Nombre:", segundo_producto["nombre"])
        print("Marca:", segundo_producto["marca"])
        print("Precio: $", segundo_producto["precio"])
        print("Stock:", segundo_producto["stock"])
        print("Talle:",segundo_producto["talle"])

        if cod==13:
            #algo anda mallllllllll, validar, el primer print
            print ("Producto encontrado:")
        print("Nombre:", tercero_producto["nombre"])
        print("Marca:", tercero_producto["marca"])
        print("Precio: $", tercero_producto["precio"])
        print("Stock:", tercero_producto["stock"])
        print("Talle:", tercero_producto["talle"])

        if cod==14:
            #algo anda mallllllllll, validar, el primer print
            print ("Producto encontrado:")
        print("Nombre:", cuarto_producto["nombre"])
        print("Marca:", cuarto_producto["marca"])
        print("Precio: $", cuarto_producto["precio"])
        print("Stock:", cuarto_producto["stock"])
        print("Talle:", cuarto_producto["talle"])

        if cod==15:
            #algo anda mallllllllll, validar, el primer print
            print ("Producto encontrado:")
        print("Nombre:", quinto_producto["nombre"])
        print("Marca:", quinto_producto["marca"])
        print("Precio: $", quinto_producto["precio"])
        print("Stock:", quinto_producto["stock"])
        print("Talle:", quinto_producto["talle"])

        if cod==15:
            #algo anda mallllllllll, validar, el primer print
            print ("Producto encontrado:")
        print("Nombre:", sexto_producto["nombre"])
        print("Marca:", sexto_producto["marca"])
        print("Precio: $", sexto_producto["precio"])
        print("Stock:", sexto_producto["stock"])
        print("Talle:", sexto_producto["talle"])

    

    if opcion == 3:
        cod = input ("Ingrese el producto que desea agregar a su carrito ")
        cantidad =int(input("Cantidad:"))
        #agregar producto a un nuevo diccionario




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