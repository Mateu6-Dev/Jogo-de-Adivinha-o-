class Pessoa:
    def __init__(self, nome):
        self.__nome = nome  # atributo privado (com dois underlines)

    # Getter
    def get_nome(self):
        return self.__nome

    # Setter
    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
        else:
            print("Nome inválido!")

p = Pessoa("João")
print(p.get_nome())       # Acessa o nome (getter)

p.set_nome("Lucas")       # Altera o nome (setter)
print(p.get_nome())

p.set_nome(123)           # Tenta passar um valor inválido
