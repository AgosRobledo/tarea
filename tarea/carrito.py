salir=False
productos= {
    "1" : {
        "nombre" : "Air Force 1",
        "marca": "nike",
        "precio": 5800.50,
        "stock": 10,
        "talle": "35",

    },
    "2" : {
        "nombre" : "Dunk",
        "marca": "adidas",
        "precio": 20000.30,
        "stock": 10,
        "talle": "36",

    },
    "3" : {
        "nombre" : "Air Max 90",
        "marca": "Nike",
        "precio": 18000.50,
        "stock": 6,
        "talle": "35",

    },
    "4" : {
        "nombre" : "",
        "marca": "",
        "precio": "",
        "stock": "",
        "caracteristicas": "",

    },
    "5" : {
        "nombre" : "",
        "marca": "",
        "precio": "",
        "stock": "",
        "caracteristicas": "",

    },
    "6" : {
        "nombre" : "",
        "marca": "",
        "precio": "",
        "stock": "",
        "caracteristicas": "",

    },
}








while (salir==False):
    print (""" Bienvenido a tienda SHOES:
    1)mostrar productos en detalle
    2)ver producto por codigo
    3)realizar compra
    4)finalizar compra
    5)salir
    """)
    opcion= int(input("Ingrese una opción: "))
    if (opcion==1):
        print (productos.items())

