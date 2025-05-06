from CuentaBancaria import CuentaBancaria
from Banco import Banco



banco=Banco()
'''
banco.crear_cuenta("111","Guillermo",500)
banco.crear_cuenta("222","Rogelio",500.0)
banco.crear_cuenta("333","Mario",5000)
'''
banco.cargar_cuentas()
banco.crear_transferencia("333","111",400)
banco.guardar_cuentas()


'''
cuenta1=CuentaBancaria()
cuenta2=CuentaBancaria()
cuenta1.titular="Guillermo Calderon"
print(cuenta1.titular)
cuenta1.depositar(50)
print(cuenta1.saldo)
print(cuenta2.saldo)
cuenta1.retirar(10)
print(cuenta1.saldo)
cuenta2.transferir(cuenta1,100)
print(cuenta1.saldo)
print(cuenta2.saldo)
'''

