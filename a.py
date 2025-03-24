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

class A:
    pass
class B(A): # klase B mantojas no A
    pass
a = A()
b = B()

class A1:
    pass
class B(A1):
    pass
class C(B):
    pass
a1 = A1()
b = B()
c = C()

class A1:
    pass
class A2:
    pass
class B(A1, A2): # daudzkāršā mantošana
    pass
a1 = A1()
a2 = A2()
b = B()
c = C()

class Persona: # bāzes klase
    def __init__(self, vards, vecums):
        self.vards = vards
        self.vecums = vecums
    def drukat(self):
        print(self.vards, self.vecums)

class Students(Persona): # klase Students manto no klases Persona
    def __init__(self, vards, vecums, studiju_gads):
        super().__init__(vards, vecums) # bāzes klases konstruktors
        self.studiju_gads = studiju_gads # šīs klases specifisks lauks
    def drukat(self): # metodes pārdefinēšana (overriding)
        super().drukat() # bāzes klases output
        print(self.studiju_gads) # vēl klāt specifiskā lauka izdruka

persona = Persona("Pēteris", 20) # objekta izveidošana ar Persona
persona.drukat() # personas izdruka
students = Students("Linda", 19, 2) # objekta izveidošana ar Students
students.drukat() # studenta izdruka
# Pēteris 20
# Linda 19
# 2