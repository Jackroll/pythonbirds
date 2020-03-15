class Pessoa :
    olhos = 2   #Atributo de classe (pode ser acessado pela classe, ou objeto) - criar sempre que o valor for igual para todos os objetos
    def __init__(self, *filhos, nome = None, idade = 35): #Atributo de instância só pode ser acessado pelo objeto - criar se o valor for diferente para cada objeto
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
        
    def cumprimentar(self):
        return f'ola {id(self)}'

    @staticmethod        #Decorator - método 01 para criar um método de classe, pode ser acessado pela classe ou objeto
    def metodo_estatico ():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):             #decorator - método 2 para criar um método de classe
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):        #Criada classe Homem que herda os atributos da classe pai - Pessoa
    pass

if __name__ == "__main__":
    joao = Pessoa(nome = 'João')
    jacson = Homem(joao, nome = 'Jacson')       #Substituida o tipo Pessoa pelo tipo Homem e continua funcionando por conta da herança
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
    print(Pessoa.metodo_estatico(), jacson.metodo_estatico())   #método de classe acessado pela classe e pelo objeto
    print(Pessoa.nome_e_atributo_de_classe(), jacson.nome_e_atributo_de_classe()) #método de classe acessado pela classe e pelo objeto
    pessoa = Pessoa('Anonimo')
    print( isinstance(pessoa, Pessoa))      #Função que verifica se um objeto é de um tipo especifico, no caso verifica se o obejto pessoa é do tipo Pessoa = True - Toda pessoa é uma Pessoa
    print( isinstance(pessoa, Homem))       #Verifica se o objeto pessoa é do tipo Homem = False, nem toda pessoa é um Homem
    print( isinstance(jacson, Pessoa))       #Jacson é um objeto do tipo Pessoa
    print( isinstance(jacson, Homem))       #Jacson é um objeto do Tipo Homem

    
    
    