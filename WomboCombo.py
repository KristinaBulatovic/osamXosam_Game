import copy
"""
matrica = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 2, 2, 0, 0, 0],
           [0, 0, 0, 2, 2, 0, 2, 0],
           [0, 0, 0, 1, 2, 0, 1, 0],
           [0, 0, 1, 2, 1, 0, 1, 0],
           [0, 0, 1, 1, 2, 0, 2, 1]]

matrica = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 2, 0, 0, 0, 0],
           [0, 0, 0, 2, 2, 0, 0, 0],
           [0, 0, 0, 1, 2, 0, 0, 0],
           [0, 0, 1, 2, 1, 0, 0, 0],
           [0, 0, 1, 1, 2, 0, 2, 1]]"""

matrica = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 2, 2, 0, 0, 0]]


matricaPoteza = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]

ja = 1
on = 2

def nadjiWomboCombo(): #preventivno, to jest trazimo mesto gde treba da se blokira wombo combo
    """m = odigrajSveNjegove()
    for i in m:
        for x in range(8):
            for y in range(8):
                if(i[x][y] == 0 and kraj(x,y,i)):
                    matricaPoteza[x][y] = 2
        
    for i in matricaPoteza:
        print(i)"""
    odigrajSveNjegove()
    for i in matricaPoteza:
        print(i)

    

def odigrajSveNjegove(): 
    ret = []
    for i in range(8): #ovo moze preko len(matrica) ako se pravi xox koji nije 8x8
        for j in range(7,-1,-1):
            if(matrica[j][i] == 0):
                matrica[j][i] = on
                
                if(nadjiUspesanWC(matrica)):
                    matricaPoteza[j][i] = 9
                #ret.append(copy.deepcopy(matrica)) #mora da ti objasnim :D
                matrica[j][i] = 0
                break
    #return ret #vraca 8 matrica, u svakoj drugacije odigran potez protivnika

def nadjiUspesanWC(i):
    matricaPoteza = [[0 for i in range(8)] for i in range(8)]
    for x in range(8):
        for y in range(8):
            if(i[x][y] == 0 and kraj(x,y,i)):
                matricaPoteza[x][y] = 2

    for x in range(8): #1. tip WC-a, onaj sa 2x po 3 horizontalno ili dijagonalno
        for y in range(8):
            if(matricaPoteza[y][x] == 2): #ovde je sjeban x i y xD
                for k in range(y+1,8):
                    if(matricaPoteza[k][x] == 2 and k%2 != y%2):
                        return True

    for x in range(8): #2. tip WC-a, onaj sa 2. na podu, prepravka ako je kraj moguc "odmah"
        for y in range(8):
             if(matricaPoteza[y][x] == 2 and ((y+1 < 8 and matrica[y+1][x] != 0) or (y == 7))):
                matricaPoteza[y][x] = 3

    b = 0
    for x in range(8): 
        for y in range(8):
             if(matricaPoteza[y][x] == 3):
                 b+=1
    if(b > 1):
        return True

    return False
            
    

def kraj(potezX, potezY, matrica):
    igrao = on
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
        return True
    
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
        return True

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
        return True

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
        return True
    
    return False

                
                
nadjiWomboCombo()
            
        
    
    





