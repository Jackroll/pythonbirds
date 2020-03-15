


"""Exemplo programação a objetos canal Otávio Miranda - Aula 35, onde é criada uma classe Pessoa, atributos e métodos
"""
class Pessoa:
    def __init__(self, nome, idade, comendo = False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
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

p1 = Pessoa('Jacson', 22 )
p2 = Pessoa('Diego', 90 )

p1.falar('POO')
p1.parar_comer()
p2.comer('Maçã')
p2.parar_falar()


