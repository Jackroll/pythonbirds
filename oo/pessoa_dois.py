from datetime import datetime


"""Exemplo programação a objetos canal Otávio Miranda - Aula 35, onde é criada uma classe Pessoa, atributos e métodos
"""
class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))            #Atributo de classe, é igual para todos os obejtos criados, usar quando o valor for igual para todos os objetos

    def __init__(self, nome, idade, comendo = False, falando=False):    #Atributo de instância valor independente de cada objeto criado, usar quando for algo com valor diferente entre os objetos
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):                                          #método do atributo
        if self.comendo:
            print(f'{self.nome} já esta comendo ')
            return
        if self.falando:
            print(f'{self.nome} esta falando, não pode comer')
            return
        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if self.comendo:
            print(f'{self.nome} parou de comer')
            self.comendo = False
            return
        if self.falando:
            print(f'{self.nome} já não esta comendo, pois esta falando')
            return

    def falar(self, assunto):
        if not self.comendo:
            print(f'{self.nome} esta falando sobre {assunto}')
            self.falando = True
            return
        print(f'{self.nome} esta comendo não pode falar')
        self.comendo = False

    def parar_falar(self):
        if self.falando:
            print(f'{self.nome} parou de falar')
            self.falando = False
            return
        if self.comendo:
            print(f'{self.nome} já não esta falando pois esta comendo')
            return

    def get_ano_nascimento(self):
        self.ano_nascimento = self.ano_atual - self.idade
        print(f'{self.nome} nasceu em {self.ano_nascimento}')


p1 = Pessoa('Jacson', 33 )
p2 = Pessoa('Diego', 90 )

print('--------------------------')
p1.falar('POO')
p1.parar_comer()
p1.get_ano_nascimento()
print('--------------------------')
p2.comer('Maçã')
p2.parar_falar()
p2.get_ano_nascimento()


