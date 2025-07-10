#Martin Ignacio Reyes Guajardo

ejecutando_programa = True

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
}
2
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
}
def stock():
      while True:
            marca =  input("consulte marca: ").capitalize().upper()
            for marca in stock:
                if marca not in marca:
                    print("no existe")
                else:
                    print(f"stock: {stock}")
            opcion3 = input("consultar otra marca S/N: ").upper()
            if opcion3 == "S":
                continue
            else:
                break
def mostrar():
     print(stock)
mostrar()
def busqueda():
    try:
        maxram = int(input("minimo de ram: "))
        minram =  int(input("maximo de ram: "))
        precio = input("precio: ")

        
        if minram and maxram and precio in productos:
            print(productos)
        else:
            print("no hay notebook")
    except ValueError:
        print("ngrese un valor valido")

def eliminar():
    try:
        while True:
            eliminar=  input("Ingrese modelo a elimibar: ")
            
            if eliminar not in productos:
                print("No se pudo eliminar el producto")
            else:
                print("eliminado")
            opcion2 =  input("eliminar otro producto S/N: ").upper()
            if opcion2 == "S":
                continue
            else:
                break
    except ValueError:
        print("opcion incorrecta")
while ejecutando_programa: 
    print("\n===== Menu principal =====")
    print("1. stock marca")
    print("2. busqueda por precio")
    print("3.listado de productos")
    print("4. SALIRRRRR")
    
    opcion = input("Seleccione una opción: ") 

    if opcion == '1': 
        stock()
    elif opcion == '2': 
        busqueda() 
    elif opcion == '3':
        print(productos)
    elif opcion == '4':
        print("Gracias por usar el sistema.")
    else:
        ejecutando_programa = False 
        print("Opción no válida. Por favor, intente de nuevo.") 
