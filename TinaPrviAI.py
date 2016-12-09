#Prvi AI
import pickle
file = open("bazaTina.db", "rb")
sve = pickle.load(file)

matricaPopunjenihPolja = [[0 for i in range(8)] for i in range(8)]
#matricaVrednosti = [[0 for i in range(8)] for i in range(8)]

potezi = []

def ispis(matrica):
    print("--------------------------")
    for i in matrica:
        print(i)
    print("--------------------------")

def odigraj(gde, sta):
    for i in range(7,-1,-1):
        if(matrica[i][gde] == 0):
            
            matrica[i][gde] = sta
            matricaPopunjenihPolja[i][gde] = 1
            
            break
    k = kraj(i, gde)
    if(k != 0):
        #print(k)
        #ispis()
        return k
    return 0

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

def odluka():
    #for i in range(8):
        #j = 7
        #while(matricaPopunjenihPolja[i][j] == 1): j-=1
    nizVrednosti = izracunajVrednosti()
    print("nizVrednosti: " + str(nizVrednosti))
    max = nizVrednosti[0]
    maxI = 0
    for i in range(8):
        if(nizVrednosti[i] > max):
            max = nizVrednosti[i]
            maxI = i
    print(maxI)
    return maxI
    

def izracunajVrednosti():
    nizVrednosti = [0 for i in range(8)]
    for i in range(8):
        p = potezi[:] + [i]
        print("Potezi: " + str(p))
        for k in sve[1]: #ovde ide ja omesto 1, 1 je ako igram prvi
            if(k[:len(p)] == p):
                x = len(k[len(p):])
                #print("X1: " + x)
                if(x == 0): nizVrednosti[i] += 100000000
                elif(x == 2): nizVrednosti[i] += 10
                else: nizVrednosti[i] += 1
                
        for k in sve[2]: #ovde ide ja omesto 2, 2 je ako igram prvi
            if(k[:len(p)] == p):
                x = len(k[len(p):])
                #print("X2: " + x)
                if(x == 0): nizVrednosti[i] -= 100000000
                elif(x == 2): nizVrednosti[i] -= 10
                else: nizVrednosti[i] -= 1
    return nizVrednosti



potezi = []
matrica = [[0 for i in range(8)] for i in range(8)]
ko = 0
for i in range(64):
    if(ko == 0):
        x = odluka()
        print("Odluka je: " + str(x))
    else:
        ispis(matrica)
        x = int(input("0-7: "))
    d = odigraj(x, ko+1)
    potezi.append(x)
    ko+=1
    ko%=2
    
    if(d == 1):
        print("Pobedio 1")
    elif(d == 2):
        print("Pobedio 2")
    
    if(d != 0):
        break
    



    
    
    
