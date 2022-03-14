#Asociacion de clases para el segundo core
from CuentaBancaria import CuentaBancaria

class User:

    def __init__(self , nombre):
        self.nombre = nombre
        self.cuenta = {
            "Comprobando":CuentaBancaria(4, 1000),
            "Ahorros": CuentaBancaria(5,4000)
        }


    def mostrar_info_cuenta(self):
        print(f"User: {self.nombre}, Comprobando balance: {self.cuenta['Comprobando'].mostrar_info_cuenta()}")
        print(f"User: {self.nombre}, Balance de ahorros: {self.cuenta['Ahorros'].mostrar_info_cuenta()}")
        return self

    

    def transfer_dinero(self, otra_cuenta, cantidad):
        
        self.balance -= cantidad
        otra_cuenta.balance += cantidad
        