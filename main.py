print("Sistema de Stock")

inventario = {}

while True:
    print("\n=== SISTEMA DE STOCK ===")
    print("1 - Agregar producto")
    print("2 - Mostrar inventario")
    print("3 - Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        inventario[producto] = cantidad
        print("Producto agregado correctamente.")

    elif opcion == "2":
        print("\nInventario actual:")
        for producto, cantidad in inventario.items():
            print(f"{producto}: {cantidad}")

    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")