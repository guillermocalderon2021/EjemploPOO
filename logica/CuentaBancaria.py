

class CuentaBancaria:
    def __init__(self,numero_cuenta, titular,saldo):
        self.__numero_cuenta=numero_cuenta
        self.__titular=titular
        self.__saldo=saldo
    
    @property # Decorador getter para __numero_cuenta
    def numero_cuenta(self):
        return self.__numero_cuenta
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter # decorador setter para __titular
    def titular(self, nuevo_titular):
        self.__titular= nuevo_titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self,monto):
        self.__saldo+=monto
    
    def retirar(self,monto):
        if(self.__saldo>=monto):
            self.__saldo-=monto
            print('Retiro realizado exitosamente')
            return True
        print('El monto del retiro supera el saldo de la cuenta')
        return False
    
    def transferir(self,destino, monto):
        if(self.__saldo>=monto):
            self.__saldo-=monto
            destino.__saldo+=monto
            print('Transferencia realizada exitosamente')
            return True
        print('El monto de la transferencia supera el saldo de la cuenta')
        return False