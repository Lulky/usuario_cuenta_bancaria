class CuentaBancaria:
    nombre_banco = "Banco Dojo"
    lista_cuentas= []
    
    def __init__(self, tasa_int, balance = 0):
        self.tasa_int = float(tasa_int/100)
        self.balance = balance
        CuentaBancaria.lista_cuentas.append(self) #Agregamos una cuenta mas a la lista de cuentas

    def hacer_retiro(self, cantidad):
        if CuentaBancaria.puede_retirar(self.balance, cantidad):
            self.balance -= cantidad
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self

    def hacer_deposito(self, cantidad):
        self.balance += cantidad
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_int)
        else:
            print("Necesitas más dinero para ganar más")
        return self

    @classmethod
    def cambio_banco(cls, nombre):
        cls.nombre_banco = nombre

    @classmethod
    def imprimir_cuentas(cls):
        for cuenta in cls.lista_cuentas:
            cuenta.mostrar_info_cuenta()
        

    def mostrar_info_cuenta(self):
        return f"Balance: {self.balance}"
        
    


    @staticmethod
    def puede_retirar(balance, cantidad_retirar):
        if(balance - cantidad_retirar) <0:
            return False
        else:
            return True
