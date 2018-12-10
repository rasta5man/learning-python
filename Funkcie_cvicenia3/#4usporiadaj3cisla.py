#4 funkcia usporiadaj3(a, b, c) vypíše zadané čísla tak, že najprv vypíše menšie z nich, potom väčšie a nakoniec najväčšie
def usporiadaj3(a,b,c):
    if a<=b<=c:
        print('cisla su: ',a,b,c ,' poradie: ', a, b, c)
    elif a<=c <=b:
        print('cisla su: ',a,b,c ,'poradie: ', a, c, b)
    elif b <=c <=a:
        print('cisla su: ',a,b,c ,'poradie: ', b, c, a)
    elif b <=a <=c:
        print('cisla su: ',a,b,c ,'poradie: ', b, a, c)
    elif c<=a<=b:
        print('cisla su: ',a,b,c ,'poradie: ', c, a, b)
    else:
        print('cisla su: ',a,b,c ,'poradie: ', c, b, a)
from random import randint as ri
for i in range(10):
    a = ri(0,10)
    b = ri(0,10)
    c = ri(0,10)
    usporiadaj3(a,b,c)
#testovy riadok pre git
