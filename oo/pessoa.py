class Pessoa :
    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
        
    def cumprimentar(self):
        return f'ola {id(self)}'


if __name__ == "__main__":
    joao = Pessoa(nome = 'João')
    jacson = Pessoa(joao, nome = 'Jacson')
    print(Pessoa.cumprimentar(jacson))
    print(id(jacson))
    print(jacson.cumprimentar())
    print(jacson.nome)
    print(jacson.idade)
    for filho in jacson.filhos:
        print(filho.nome)