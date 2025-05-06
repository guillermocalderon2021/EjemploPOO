from CuentaBancaria import CuentaBancaria
import csv

class Banco:
    def __init__(self):
        self.cuentas={}
    
    def crear_cuenta(self, numero_cuenta, titular, saldo_inicial):

        if isinstance(saldo_inicial, float) == False and isinstance(saldo_inicial, int) == False:
            print('El saldo inicial debe ser un valor numerico')
            return

        if saldo_inicial<100:
            print('El monto minimo de apertura de cuenta es $100')
            return

        if numero_cuenta in self.cuentas:
            print('Ya existe una cuenta con este mismo numero')
            return
        cuenta=CuentaBancaria(numero_cuenta, titular, saldo_inicial) # Creando la instancia de la clase CuentaBancaria
        self.cuentas[numero_cuenta]=cuenta

    def crear_deposito(self,numero_cuenta, monto):
        if isinstance(monto, float) == False and isinstance(monto, int) == False:
            print('El monto del deposito debe ser un valor numerico')
            return

        if monto<=0:
            print('El monto del deposito debe ser mayor que cero')
            return

        if numero_cuenta not in self.cuentas:
            print('No existe la cuenta')
            return

        cuenta=self.cuentas[numero_cuenta]
        cuenta.depositar(monto)
        print("Deposito realizado exitosamente")
        print(cuenta.saldo)

    def crear_retiro(self,numero_cuenta, monto):
        if isinstance(monto, float) == False and isinstance(monto, int) == False:
            print('El monto del retiro debe ser un valor numerico')
            return

        if monto<=0:
            print('El monto del retiro debe ser mayor que cero')
            return

        if numero_cuenta not in self.cuentas:
            print('No existe la cuenta')
            return

        cuenta=self.cuentas[numero_cuenta]    
        cuenta.retirar(monto)
        print(cuenta.saldo)
    
    def crear_transferencia(self,numero_cuenta_origen, numero_cuenta_destino, monto):
        if isinstance(monto, float) == False and isinstance(monto, int) == False:
            print('El monto de la transferencia debe ser un valor numerico')
            return

        if monto<=0:
            print('El monto de la transferencia debe ser mayor que cero')
            return

        if numero_cuenta_origen not in self.cuentas:
            print('No existe la cuenta de origen')
            return

        if numero_cuenta_destino not in self.cuentas:
            print('No existe la cuenta de destino')
            return

        cuenta_origen=self.cuentas[numero_cuenta_origen]    
        cuenta_destino= self.cuentas[numero_cuenta_destino]
        cuenta_origen.transferir(cuenta_destino,monto)
        print(cuenta_origen.saldo)
        print(cuenta_destino.saldo)
    
    def guardar_cuentas(self):
        with open("cuentas.csv","w", newline="") as f1:
            columnas=["numero_cuenta","titular","saldo"]
            csv_writer=csv.DictWriter(f1,delimiter=",", fieldnames=columnas)
            csv_writer.writeheader()
            for cuenta in self.cuentas.values():
                fila={
                    "numero_cuenta": cuenta.numero_cuenta,
                    "titular": cuenta.titular,
                    "saldo":cuenta.saldo
                }
                csv_writer.writerow(fila)
    
    def cargar_cuentas(self):
         with open("cuentas.csv","r", newline="") as f1:
            self.cuentas={}
            csv_reader=csv.DictReader(f1,delimiter=",")
            for linea in csv_reader:
                cuenta=CuentaBancaria(linea['numero_cuenta'], linea['titular'], float(linea['saldo']))
                self.cuentas[linea['numero_cuenta']]=cuenta