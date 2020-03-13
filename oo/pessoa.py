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
    jacson.sobrenome = 'Jeremias' #Criando atributos dinamicamente em tempo de execução
    del jacson.filhos             #Deleta um atributo dinamicamente
    print(jacson.__dict__)        #__dict__ mostra os atributos de instancia
    print(joao.__dict__)          #__dict__ mostra os atributos de instancia  
    
    
    
    
    