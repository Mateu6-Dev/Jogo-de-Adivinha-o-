class Pessoa:
    def __init__(self, nome: object, idade: object, genero: object) -> None: #Metodo construtor
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def apresentacao(self): #Metodo
        print(f'Ola meu nome é {self.nome} e tenho {self.idade} de idade e sou do genero {self.genero}.')


p1 = Pessoa("Marcos", 23, "masculino")
p2 = Pessoa("Julia", 34, "feminino")

p1.apresentacao()
p2.apresentacao()