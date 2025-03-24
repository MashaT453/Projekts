print("adasasd")
print("helllo")

class Persona:
    def __init__(self, vards, vecums): # konstruktora definēšana
        self.vards = vards # šeit tiek izveidots lauks vards
        self.vecums = vecums # šeit tiek izveidots lauks vecums
    def drukat(self): # metodes definēšana
        print(self.vards, self.vecums)
persona = Persona("Pēteris ", 20) # objekta izveidošana un konstruktora izsaukšana
persona.drukat()
# Pēteris 20 