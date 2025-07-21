class contabancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo #Atributo privado
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__mostrar_saldo()
        else:
            print("Valor de deposito invalido")
        
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            self.__mostrar_saldo()
        else:
            print('Saldo insuficiente')

    def __mostrar_saldo(self): #Metodo privado
        print(f'Saldo atual de {self.titular}: R${self.__saldo:.2f}')

    #def _contabancaria__mostrar_saldo(self):
        pass


conta = contabancaria('Mateus', 1000)
conta.depositar(400)
conta.sacar(10)

#conta._contabancaria__mostrar_saldo()
        
