class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
        self.volume = 30

    def volume_mais(self):
        if self.volume < 100:
            self.volume += 10

    def volume_menos(self):
        if self.volume > 0:
            self.volume -= 10

    def mudo (self):
        self.volume = 0

    def canal_mais(self):
        if self.ligada:
            self.canal += 1

    def canal_menos(self):
        if self.ligada:
            self.canal -= 1

    def power (self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True


televisao = Televisao()

print("televisao está ligada: {}" .format(televisao.ligada))
televisao.power()
print("televisao está ligada: {}" .format(televisao.ligada))

print("canal: {}" .format(televisao.canal))
print("volume: {}" .format(televisao.volume))
televisao.canal_mais()
televisao.canal_mais()
print("canal: {}" .format(televisao.canal))
televisao.canal_menos()
#televisao.mudo()
televisao.volume_mais()
televisao.volume_mais()
televisao.volume_mais()
televisao.volume_mais()

print("volume: {}" .format(televisao.volume))
print("canal: {}" .format(televisao.canal))