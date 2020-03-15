'''Exemplo simples de composição, onde é criada a Classe cliente com atributos de instancia nome, idade e endereço, onde o endereço
é advinda de outra classe a classe endereço'''


class Cliente:                                                  #cria a classe cliente com atributos de instancia nome e idade
    def __init__(self, nome, idade):                            #cria os atributos de instância, nome e idade
        self.nome = nome
        self.idade = idade
        self.endereco = []                                      #cria o atributo endereços que será preenchida pelo metodo insere_endereco

    def insere_endereco(self, cidade, estado):                  #cria o método que insere o endereco no atributo tipo lista, os valores são adicionados com base nos atributos da classe endereço
        self.endereco.append(Endereco(cidade, estado))


    def mostra_cliente(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        for enderecos in self.endereco:
            print('Endereço: ', enderecos.cidade, enderecos.estado)
        self.categoria_idade()

    def categoria_idade(self):
        if(self.idade >50) :
            print('Idoso')
        elif(self.idade >21):
            print('Adulto')
        elif(self.idade >12):
            print('Adolescente')
        else:
            print('Criança')



class Endereco:                                                 #cria a classe Endereço, com atributos cidade e estado
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado






cliente1 = Cliente('jacson', 32)
cliente1.insere_endereco('Imarui', 'SC')
cliente1.mostra_cliente()
print('-------------------------')
cliente2 = Cliente('João', 90)
cliente2.insere_endereco('Imarui', 'SC')
cliente2.mostra_cliente()
print('-------------------------')
cliente3 = Cliente('Inês Maria', 2)
cliente3.insere_endereco('Imarui', 'SC')
cliente3.mostra_cliente()
