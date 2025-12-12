import os
from time import sleep
"""
PROYECTO 1: CRUD DE EMPRESA
NOMBRE: ADRIANO ARMAS
"""

dic_empresas = {
    '100':{
        'razon_social':'TECSUP',
        'direccion' : 'CALLE PERU 123'
    }
}

ANCHO = 50

while(True):
    os.system("clear")
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input('INGRESE OPCIÓN : '))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR ALUMNO")
        print("=" * ANCHO)

    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR ALUMNO")
        print("=" * ANCHO)

    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR  ALUMNO")
        print("=" * ANCHO)

    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR ALUMNO")
        print("=" * ANCHO)

    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL PROGRAMA")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")
