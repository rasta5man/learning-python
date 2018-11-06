class Student:

    znamkaA, znamkaB, znamkaC, znamkaD = 'A', 'B', 'C', 'D'
    znamkaE, znamkaFx = 'E', 'Fx'
    
    def __init__(self, meno, priezvisko, odbor, rocnik, id, znamky):
        self.meno = meno
        self.priezvisko = priezvisko
        self.odbor = odbor
        self.rocnik = rocnik
        self.id = id
        self.znamky =znamky
        
    def __repr__(self):
        return f'Student: {self.meno}, {self.priezvisko}, Odbor: {self.odbor}, Rocnik: {self.rocnik}, Id studenta: {self.id}, Znamky: {self.znamky}'

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

    def __init__(self, nazov):
        self.fakulta = nazov
        self.zoznamStudentov = []
        self.poleZoSuboru = []

        
    def najdi(self, id):
        for student in self.zoznamStudentov:
            if int(student.id) == id:
                return student

    def pridajStudenta(self, student):
        if isinstance(student, Student):
            self.zoznamStudentov.append(student)
        if isinstance(student, list):
            for student in list:
                self.zoznamStudentov.append(student)

    def vypisStudentov(self):
        print('***************************************')
        print('Aktualny zoznam studentov fakulty:', self.fakulta.upper())
        print('***************************************')
        for student in self.zoznamStudentov:
            print(student)
    
    def citaj(self, subor):
        print('***********************************')
        print('Vypis Studentov fakulty pred zmenou:')
        print('***********************************')
        with open(subor) as subor:
            for riadok in subor:
                self.poleZoSuboru.append([udaj.strip() for udaj in riadok.split(';')])
        for i in range (len(self.poleZoSuboru)):
            self.zoznamStudentov.append(Student(self.poleZoSuboru[i][0], self.poleZoSuboru[i][1], self.poleZoSuboru[i][2], self.poleZoSuboru[i][3], self.poleZoSuboru[i][4], self.poleZoSuboru[i][5]))
        for riadok in self.zoznamStudentov:
            print(riadok)
        
    def zapis(self):
        with open('7_projekt_studenti.txt', 'w') as subor:
            for pole in self.zoznamStudentov:
                subor.write(str(pole))
                subor.write('\n')
            

def main(subor1, subor2, nazovFakulty):
    fakulta = Fakulta(nazovFakulty)
    fakulta.citaj(subor1)
    with open(subor2) as subor:
        riadok = subor.readline()
        while riadok != '':
            if riadok[0:5] == 'novy:':
                zmenenyRiadok = riadok[6:]
                fakulta.poleZoSuboru = []
                fakulta.poleZoSuboru.append([udaj.strip() for udaj in zmenenyRiadok.split(';')])
                for i in range(len(fakulta.poleZoSuboru)):
                    fakulta.pridajStudenta(Student(fakulta.poleZoSuboru[i][0], fakulta.poleZoSuboru[i][1], fakulta.poleZoSuboru[i][2], fakulta.poleZoSuboru[i][3], fakulta.poleZoSuboru[i][4], fakulta.poleZoSuboru[i][5]))
            if riadok[0:6] == 'vyhod:':
                pozicia = riadok.find('id = ')
                idNaZmenu = int(riadok[pozicia+5:-1])
                fakulta.zoznamStudentov.remove(fakulta.najdi(idNaZmenu))
            if riadok[0:5] == 'zmen:':
                pass
            if riadok[0:7] == 'znamka:':
                pass
            if riadok[0:7] == 'postup:':
                pass
            if riadok[0:7] == 'ukonci:':
                pass
            riadok = subor.readline()
    fakulta.vypisStudentov()
main('7_projekt_studenti.txt', '7_projekt_zmeny.txt','Narodohospodarska')
input('stlac enter')
