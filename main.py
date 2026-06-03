import json

def cargar_inventario():
    try:
        with open("inventario.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_inventario(inventario):
    with open("inventario.json", "w") as archivo:
        json.dump(inventario, archivo, indent=4)

print("Sistema de Stock")

inventario = cargar_inventario()

while True:
    print("\n=== SISTEMA DE STOCK ===")
    print("1 - Agregar producto")
    print("2 - Mostrar inventario")
    print("3 - Buscar producto")
    print("4 - Modificar stock")
    print("5 - Eliminar producto")
    print("6 - Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Nombre del producto: ").strip().lower()
        cantidad = int(input("Cantidad: "))
        inventario[producto] = cantidad
        guardar_inventario(inventario)
        print("Producto agregado correctamente.")

    elif opcion == "2":
        if len(inventario) == 0:
            print("No hay productos cargados.")
        else:
            print("\nInventario actual:")
            for producto, cantidad in inventario.items():
                print(f"{producto}: {cantidad}")

    elif opcion == "3":
        producto = input("Ingrese el producto a buscar: ").strip().lower()

        if producto in inventario:
            print(f"Stock disponible: {inventario[producto]}")
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        producto = input("Producto a modificar: ").strip().lower()

        if producto in inventario:
            nueva_cantidad = int(input("Nueva cantidad: "))
            inventario[producto] = nueva_cantidad
            guardar_inventario(inventario)
            print("Stock actualizado.")
        else:
            print("Producto no encontrado.")

    elif opcion == "5":
        producto = input("Producto a eliminar: ").strip().lower()

        if producto in inventario:
            del inventario[producto]
            guardar_inventario(inventario)
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    elif opcion == "6":
        guardar_inventario(inventario)
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")