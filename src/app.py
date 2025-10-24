from ingestion.load_data import ingesta_data
from pyspark.sql import SparkSession


def __init__():

    while True: 
        print("Bienvenido al sistema de gestación ETL para un super mercado")
        user_option = app_menu()

        if user_option == 1:
            ingesta_data()
        if user_option == 4: 
            break


def app_menu():

    print("Que desea realizar?")

    print("1. Ingesta de datos\n2. Mostrar los datos.\n3. Reportes.\n4. Salir")
    option = int(input(": "))

    if option in [1,2,3,4]:
        return option 
    else:
        print("La opcion ingresada no es valida")
        app_menu()