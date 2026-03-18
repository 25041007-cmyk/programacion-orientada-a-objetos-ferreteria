## LISTAS ##
inventario = []
clientes = []
ventas = []
# Lista de usuarios para el inicio de sesión
usuarios_sistema = {"admin": "1234", "empleado1": "ferre2024"}

## CLASES FERRETERIA ##

# --- IMPLEMENTACIÓN DE HERENCIA ---
class Persona:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class Cliente(Persona): # Cliente hereda de Persona
    def __init__(self, id, nombre, telefono, correo):
        # Uso de super() para heredar atributos de Persona
        super().__init__(nombre, telefono)
        self.id = id
        self.correo = correo

    def mostrar_info(self):
        print("\nID:", self.id)
        print("Nombre:", self.nombre)
        print("Teléfono:", self.telefono)
        print("Correo:", self.correo)

class Producto:
    def __init__(self, codigo, nombre, categoria, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_info(self):
        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
        print("Categoría:", self.categoria)
        print("Precio:", self.precio)

class Inventario:
    def __init__(self, producto, cantidad, vendidos):
        self.producto = producto
        self.cantidad = cantidad
        self.vendidos = vendidos

    def disponibles(self):
        return self.cantidad - self.vendidos

    def vender(self, cantidad):
        if cantidad <= self.disponibles():
            self.vendidos += cantidad
            print("Venta realizada")
        else:
            print("No hay suficiente inventario")

    def agregar_stock(self, cantidad):
        self.cantidad += cantidad

    def mostrar_estado(self):
        print("\nProducto:", self.producto.nombre)
        print("Código:", self.producto.codigo)
        print("Cantidad total:", self.cantidad)
        print("Vendidos:", self.vendidos)
        print("Disponibles:", self.disponibles())

class Venta:
    def __init__(self, folio, id_cliente, codigo, fecha, cantidad, total):
        self.folio = folio
        self.id_cliente = id_cliente
        self.codigo = codigo
        self.fecha = fecha
        self.cantidad = cantidad
        self.total = total

    def mostrar_info(self):
        print("\nFolio:", self.folio)
        print("Cliente:", self.id_cliente)
        print("Producto:", self.codigo)
        print("Fecha:", self.fecha)
        print("Cantidad:", self.cantidad)
        print("Total:", self.total)


## FUNCIONES ##

# --- IMPLEMENTACIÓN DE INICIO DE SESIÓN ---
def inicio_sesion():
    print("--- ACCESO AL SISTEMA ---")
    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        if usuario in usuarios_sistema and usuarios_sistema[usuario] == password:
            print(f"\n¡Bienvenido al sistema, {usuario}!")
            return True
        else:
            intentos -= 1
            print(f"Datos incorrectos. Intentos restantes: {intentos}")
    return False

def alta_producto():
    print("\n⊹ Alta de producto ⊹")
    codigo = input("Código del producto: ")
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad inicial: "))
    nuevo_producto = Producto(codigo, nombre, categoria, precio)
    inventario_producto = Inventario(nuevo_producto, cantidad, 0)
    inventario.append(inventario_producto)
    print("¡Producto registrado correctamente!")

def mostrar_inventario():
    print("\n⊹ Inventario ⊹")
    if len(inventario) == 0:
        print("No hay productos registrados")
        return
    for item in inventario:
        item.mostrar_estado()

def consultar_producto():
    print("\n⊹ Consultar producto ⊹")
    codigo = input("Ingrese el código del producto: ")
    for item in inventario:
        if item.producto.codigo == codigo:
            item.mostrar_estado()
            return
    print("Producto no encontrado")

def registrar_cliente():
    print("\n⊹ Registrar cliente ⊹")
    id_cliente = input("ID del cliente: ")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    nuevo_cliente = Cliente(id_cliente, nombre, telefono, correo)
    clientes.append(nuevo_cliente)
    print("¡Cliente registrado!")

def consultar_cliente():
    print("\n⊹ Consultar cliente ⊹")
    id_buscar = input("Ingrese ID del cliente: ")
    for c in clientes:
        if c.id == id_buscar:
            c.mostrar_info()
            return
    print("Cliente no encontrado")

def mostrar_clientes():
    print("\n⊹ Lista de clientes ⊹")
    if len(clientes) == 0:
        print("No hay clientes registrados")
        return
    for c in clientes:
        c.mostrar_info()

def registrar_venta():
    print("\n⊹ Registrar venta ⊹")
    folio = len(ventas) + 1
    id_cliente = input("ID cliente (999999 público general): ")
    codigo = input("Código del producto: ")
    fecha = input("Fecha: ")
    cantidad = int(input("Cantidad: "))
    for item in inventario:
        if item.producto.codigo == codigo:
            if cantidad <= item.disponibles():
                item.vender(cantidad)
                total = cantidad * item.producto.precio
                nueva_venta = Venta(folio, id_cliente, codigo, fecha, cantidad, total)
                ventas.append(nueva_venta)
                print("Venta registrada. Folio:", folio)
                return
            else:
                print("No hay suficiente inventario")
                return
    print("Producto no encontrado")

def mostrar_historial():
    print("\n⊹ Historial de ventas ⊹")
    if len(ventas) == 0:
        print("No hay ventas registradas")
        return
    for v in ventas:
        v.mostrar_info()


## MENU ##

def menu():
    # Validamos el inicio de sesión antes de mostrar el menú
    if not inicio_sesion():
        print("Acceso denegado. Cerrando programa.")
        return

    while True:
        print("\n⋆.˚ SISTEMA DE FERRETERÍA ⋆.˚")
        print("1. Dar de alta producto")
        print("2. Mostrar inventario de productos")
        print("3. Consultar producto por código")
        print("4. Registrar cliente")
        print("5. Consultar cliente por ID")
        print("6. Mostrar todos los clientes")
        print("7. Registrar una venta")
        print("8. Mostrar historial de ventas")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            consultar_producto()
        elif opcion == "4":
            registrar_cliente()
        elif opcion == "5":
            consultar_cliente()
        elif opcion == "6":
            mostrar_clientes()
        elif opcion == "7":
            registrar_venta()
        elif opcion == "8":
            mostrar_historial()
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida")

# Ejecución
menu()