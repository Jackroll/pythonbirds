



class PartyAnimal:              #Cria a classe
    x = 0                       #Cria atributo de classe

    def party(self):            #Cria o método
        self.x += 1
        print(self.x)


an = PartyAnimal()              #Cria um objeto do tipo Partyanimal
an.party()                     #Executa o método
an.party()                     #Executa o método
an.party()                     #Executa o método
an.party()                     #Executa o método
an.party()                     #Executa o método
PartyAnimal.party(an)

print('type', type(an))
print('type', type(an.party))
print('type', type(an.x))
print('type', type(PartyAnimal()))

