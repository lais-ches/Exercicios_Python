# AUTORA:LAÍS RODRIGUES

###
# Exercícios para praticar o assunto de Programação Orientada a Objetos 

class Human:
    def __init__(self, name, race, power):
        self.name = name
        self.race = race
        self.power = power

    def descricao(self):
        return f"{self.name} é {self.race}. E seu poder é {self.power}."

human1 = Human('Ishida Uryuu', 'Quincy', 'Heilig Bogen')
human2 = Human('Yukio Hans Vorarlberna', 'Fullbringer', 'Invaders Must Die')
print(human1.descricao())  
print(human2.descricao())



class Spirit(Human):
    def __init__(self, name, race, power, release):
        self.release = release
        super().__init__(name, race, power)

    def descricao(self):
        return super().descricao() + f" de nome {self.release}."

spirit1 = Spirit('Hitsugaya Toushirou', 'Shinigami', 'Zanpakutou', 'Hyourinmaru')
spirit2 = Spirit('Grimmjow Jaegerjaquez', 'Arrancar', 'Resurrección', 'Pantera')
print(spirit1.descricao())  
print(spirit2.descricao())

