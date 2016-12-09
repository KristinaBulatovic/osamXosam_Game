import pygame
import random

pygame.init()

display_width = 500
display_height = 500

black = (0,0,0)
white = (255,255,255)

yellow = (20,121,243)
pink = (237,28,36)

bright_yellow = (9,85,179)
bright_pink = (173,14,22)

narandzasta = (239,16,145)
tamno_narandzasta = (200,13,120)

zelena = (0,157,0)
tamno_zelena = (0,121,0)


prazno = " "
figura = ""
igraj = ""


txt = [[0 for i in range(8)] for i in range(8)]

for i in range (8):
    for j in range (8):
        txt[i][j] = " "
    

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Game 8x8')


def things(thingx, thingy, thingw, thingh,debljina_linije, color):
    pygame.draw.line(gameDisplay, color, [thingx, thingy],[thingw, thingh],debljina_linije)

def X_O(txt):
    font = pygame.font.SysFont("comicsansms", 100)
    text = font.render(txt, True, black)

def pozicija(txt,i,j):
    x = (j+1)*50+5
    y = i*50+40
    font = pygame.font.SysFont("comicsansms", 50)
    text = font.render(txt, True, black)
    gameDisplay.blit(text,(x,y))

def tekst(txt,x,y):
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render(txt, True, black)
    gameDisplay.blit(text,(x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    

def button(msg,x,y,w,h,ic,ac,action=None,a="",b=""):
    global figura, igraj

    figura = a
    igraj = b
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)

    

def quitgame():
    pygame.quit()
    quit()

def kraj_igre(a):

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)       
        largeText = pygame.font.SysFont("comicsansms",70)
        TextSurf, TextRect = text_objects(a, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("PLAY 1",20,400,100,50,yellow,bright_yellow,game_loop,"X", "Igraj")
        button("PLAY 2",140,400,100,50,narandzasta,tamno_narandzasta,game_loop,"O","Igraj")
        button("PLAY 3",260,400,100,50,zelena,tamno_zelena,game_loop,"X")
        button("Quit",380,400,100,50,pink,bright_pink,quitgame)
        
        pygame.display.update()

            
def pobednik(txt,broj):
    
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            brojX = [0,0,0,0,0,0,0,0]
            brojO = [0,0,0,0,0,0,0,0]
            for k in range(broj):
                if(i+k < 8):
                    if(txt[i+k][j] == "X"): brojX[0]+=1
                    if(txt[i+k][j] == "O"): brojO[0]+=1
                if(i-k > 0):
                    if(txt[i-k][j] == "X"): brojX[1]+=1
                    if(txt[i-k][j] == "O"): brojO[1]+=1
                if(j+k < 8):
                    if(txt[i][j+k] == "X"): brojX[2]+=1
                    if(txt[i][j+k] == "O"): brojO[2]+=1
                if(j-k > 0):
                    if(txt[i][j-k] == "X"): brojX[3]+=1
                    if(txt[i][j-k] == "O"): brojO[3]+=1
                if(j+k < 8 and i+k < 8):
                    if(txt[i+k][j+k] == "X"): brojX[4]+=1
                    if(txt[i+k][j+k] == "O"): brojO[4]+=1
                if(j-k > 0 and i-k > 0):
                    if(txt[i-k][j-k] == "X"): brojX[5]+=1
                    if(txt[i-k][j-k] == "O"): brojO[5]+=1
                if(j-k > 0 and i+k < 8):
                    if(txt[i+k][j-k] == "X"): brojX[6]+=1
                    if(txt[i+k][j-k] == "O"): brojO[6]+=1
                if(j+k < 8 and i-k > 0):
                    if(txt[i-k][j+k] == "X"): brojX[7]+=1
                    if(txt[i-k][j+k] == "O"): brojO[7]+=1
            for p in brojX:
                if(p == broj):
                    return True
            for f in brojO:
                if(f == broj):
                    return True
    return False


def racunar_igra():
    global figura

    # ako ima polje da rac pobedi da stavi tu
    for i in range(8):
        if provera(i) == True:
            a,b = prazno_polje(i)
            txt[a][b] = figura     
            if pobednik(txt,4):
                txt[a][b] = prazno
                return a,b
            txt[a][b] = prazno
            

    # ako ima polje da covek pobedi da ga blokira
    figura = zamena(figura)
    for i in range(8):
        if provera(i) == True:
            a,b = prazno_polje(i)
            txt[a][b] = figura     
            if pobednik(txt,4):
                txt[a][b] = prazno
                figura = zamena(figura)
                return a,b
            txt[a][b] = prazno
    figura = zamena(figura)
    

    for i in range(7,-1,-1):
        for j in range(3,-1,-1):
            if provera(j) == True:
                if txt[i][j] == prazno:
                    txt[i][j] =  figura
                    return i,j

        for k in range(4,8,1):
            if provera(k) == True:
                if txt[i][k] == prazno:
                    txt[i][k] =  figura
                    return i,k 
                

def zamena(figura):
    if figura == "X":
        figura = "O"
    elif figura == "O":
        figura = "X"

    return figura
        

def prazno_polje(broj):

    j = 0
    for i in range(8):
        j -= 1
        if txt[j][broj] == prazno:
            return j, broj

def provera(broj):
    
    j = 0
    for i in range(8):
        j -= 1
        if txt[j][broj] == prazno:
            return True
    return False
    

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",70)
        TextSurf, TextRect = text_objects("Game 8x8", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("PLAY 1",20,400,100,50,yellow,bright_yellow,game_loop,"X", "Igraj")
        button("PLAY 2",140,400,100,50,narandzasta,tamno_narandzasta,game_loop,"O","Igraj")
        button("PLAY 3",260,400,100,50,zelena,tamno_zelena,game_loop,"X")
        button("Quit",380,400,100,50,pink,bright_pink,quitgame)
            
        pygame.display.update()

def igra(broj):
    global figura, txt
    a = provera(broj)
    if a == True:
        a,b = prazno_polje(broj)
        txt[a][b] = figura
        if pobednik(txt,4):
            a = figura + " je pobedio"
            kraj_igre(a)
        figura = zamena(figura)
                        
def game_loop():
    
    global figura, txt
    
    txt = [[0 for i in range(8)] for i in range(8)]
    
    for i in range (8):
        for j in range (8):
            txt[i][j] = " "


    if figura == "O":
        broj = random.randrange(1,1000)
        if broj < 500:
           broj = 4
        else:
           broj = 5
           
        a,b = prazno_polje(broj)
        figura = zamena(figura)
        txt[a][b] = figura
        figura = zamena(figura)
    

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_1:
                    broj = 0
                    
                elif event.key == pygame.K_2:
                    broj = 1
                          
                elif event.key == pygame.K_3:
                    broj = 2
                       
                elif event.key == pygame.K_4:
                    broj = 3
                       
                elif event.key == pygame.K_5:
                    broj = 4
                       
                elif event.key == pygame.K_6:
                    broj = 5
                       
                elif event.key == pygame.K_7:
                    broj = 6
                    
                elif event.key == pygame.K_8:
                    broj = 7
                    
                else:
                    continue
                
                igra(broj)
                
                if igraj == "Igraj":
                    a,b = racunar_igra()
                    txt[a][b] = figura
                    if pobednik(txt,4):
                        a = figura + " je pobedio"
                        kraj_igre(a)
                    figura = zamena(figura)

                

        gameDisplay.fill(white)
        
        for i in range(50,500,50):
            things(50, i, 450, i, 3, black)
            things(i, 50, i, 450, 3, black)

        for i in range(8):
            for j in range(8):
                pozicija(txt[i][j],i,j)

        pa = tekst("1",70,10)
        pb = tekst("2",120,10)
        pc = tekst("3",170,10)
        pd = tekst("4",220,10)
        pe = tekst("5",270,10)
        pf = tekst("6",320,10)
        pg = tekst("7",370,10)
        ph = tekst("8",420,10)


        pygame.display.update()


    

game_intro()
game_loop()
pygame.quit()
quit()
