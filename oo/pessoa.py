class Pessoa :
    olhos = 2   #Atributo de classe (pode ser acessado pela classe, ou objeto) - criar sempre que o valor for igual para todos os objetos
    def __init__(self, *filhos, nome = None, idade = 35): #Atributo de instância só pode ser acessado pelo objeto - criar se o valor for diferente para cada objeto
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
    print(Pessoa.olhos)           #atributo sendo acessado pela classe
    print(jacson.olhos)           #atributo sendo acessado pelo objeto
    
    
    
    
    