class Student:

    znamkaA, znamkaB, znamkaC, znamkaD = 'A', 'B', 'C', 'D'
    znamkaE, znamkaFx = 'E', 'Fx'
    
    def __init__(self, meno, priezvisko, odbor, id, rocnik=1):
        self.meno = meno
        self.priezvisko = priezvisko
        self.odbor = odbor
        self.rocnik = rocnik
        self.id = id
        self.znamky =[]
        
    def __repr__(self):
        return f'Student:{self.meno}, {self.priezvisko}, odbor {self.odbor}, rocnik: {self.rocnik}, id studenta: {self.id}'

    def pridajZnamku(self, znamka):
        if isinstance(znamka, str):
            self.znamky.append(znamka)
        if isinstance(znamka,list):
            for prvok in znamka:
                self.znamky.append(prvok)

    def vypisZnamok(self):
        print(self, 'ma zapisane tieto znamky:')
        for znamka in self.znamky:
            print(znamka, end=', ')
            
    def priemer(self):
        sucet = 0
        pocetZnamok = 0
        for znamka in self.znamky:
            if znamka == 'A':
                sucet += 1
            if znamka == 'B':
                sucet += 1.5
            if znamka == 'C':
                sucet += 2
            if znamka == 'D':
                sucet += 2.5
            if znamka == 'E':
                sucet += 3
            if znamka == 'Fx':
                sucet += 4
        priemer = sucet / len(self.znamky)
        print('Student', self.meno, self.priezvisko, ' ma priemer znamok ', priemer)

class Fakulta:

    def __init_(self, nazov):
        self.fakulta = nazov
        self.zoznamStudentov = []

    
        
                
s = Student('janko','hrasko','informatika',1500)
s.pridajZnamku('A')
s.pridajZnamku(s.znamkaC)
s.pridajZnamku(s.znamkaD)
s.pridajZnamku(s.znamkaA)
s.pridajZnamku([s.znamkaA, 'B', 'E', s.znamkaC, 'A'])             
    
