import random
import time
import pickle

prviPobedjuje = []
drugiPobedjuje = []

file = open("bazaTina.db", "rb")
sve = pickle.load(file)
file.close()



def ispis():
    print("--------------------------")
    for i in matrica:
        print(i)
    print("--------------------------")

def odigraj(gde, sta):
    for i in range(7,-1,-1):
        if(matrica[i][gde] == 0):
            matrica[i][gde] = sta
            break
    k = kraj(i, gde)
    if(k != 0):
        #print(k)
        #ispis()
        return k
    return 0

def randomPotez():
    while True:
        x = random.randrange(30)
        if(x < 1):
            x = 0
        elif(x < 3):
            x = 1
        elif(x < 7):
            x = 2
        elif(x < 15):
            x = 3
        elif(x < 23):
            x = 4
        elif(x < 27):
            x = 5
        elif(x < 29):
            x = 6
        else:
            x = 7 
        if(matrica[0][x] == 0):
            break
    return x

def kraj(potezX, potezY):
    igrao = matrica[potezX][potezY]
    ima = 1
    pomeraj = 1
    while potezX+pomeraj < 8 and matrica[potezX+pomeraj][potezY] == igrao:
        pomeraj+=1
    ima += (pomeraj - 1)
    pomeraj = 1
    while potezX-pomeraj > 0 and matrica[potezX-pomeraj][potezY] == igrao:
        pomeraj+=1
    ima += (pomeraj - 1)
    if(ima > 3):
        return igrao
    
    ima = 1
    pomeraj = 1
    while potezY+pomeraj < 8 and matrica[potezX][potezY+pomeraj] == igrao:
        pomeraj+=1
    ima += (pomeraj - 1)
    pomeraj = 1
    while potezY-pomeraj> 0 and matrica[potezX][potezY-pomeraj] == igrao:
        pomeraj+=1
    ima += (pomeraj - 1)
    if(ima > 3):
        return igrao

    ima = 1
    pomeraj = 1
    while potezY+pomeraj < 8 and  potezX+pomeraj < 8 and matrica[potezX+pomeraj][potezY+pomeraj] == igrao:
        pomeraj+=1
    ima += (pomeraj - 1)
    pomeraj = 1
    while potezY-pomeraj > 0 and potezX-pomeraj > 0 and matrica[potezX-pomeraj][potezY-pomeraj] == igrao:
        pomeraj+=1
    ima += (pomeraj - 1)
    if(ima > 3):
        return igrao

    ima = 1
    pomeraj = 1
    while potezY+pomeraj < 8 and potezX-pomeraj > 0 and matrica[potezX-pomeraj][potezY+pomeraj] == igrao:
        pomeraj+=1
    ima += (pomeraj - 1)
    pomeraj = 1
    while potezX+pomeraj < 8 and potezY-pomeraj > 0 and matrica[potezX+pomeraj][potezY-pomeraj] == igrao:
        pomeraj+=1
    ima += (pomeraj - 1)
    if(ima > 3):
        return igrao
    
    return 0

prviPobedjuje += sve[1]
drugiPobedjuje += sve[2]

kec = 0
dva = 0
vreme = time.time()
for j in range(100000):
    potezi = []
    matrica = [[0 for i in range(8)] for i in range(8)]
    ko = 0
    for i in range(64):
        x = randomPotez()
        d = odigraj(x, ko+1)
        potezi.append(x)
        ko+=1
        ko%=2
        if(d != 0):
            break
    if(d == 1):
        if(potezi not in prviPobedjuje):
            prviPobedjuje.append(potezi)
        kec += 1
    else:
        if(potezi not in drugiPobedjuje):
            drugiPobedjuje.append(potezi)
        dva += 1

print(kec,dva)
print(time.time() - vreme)

print(len(prviPobedjuje))
print(len(drugiPobedjuje))

stat = [0 for i in range(8)]
for i in prviPobedjuje:
    stat[i[0]] += 1
print("Prvi pobedjuje: ", stat)

vreme = time.time()
stat = [0 for i in range(8)]
for i in drugiPobedjuje:
    stat[i[0]] += 1
print("Drugi pobedjuje: ", stat)


prviPobedjuje.sort()
drugiPobedjuje.sort()

sve[1] = prviPobedjuje
sve[2] = drugiPobedjuje

file = open("bazaTina.db", "wb")
pickle.dump(sve, file)
file.close()
print(time.time() - vreme)
