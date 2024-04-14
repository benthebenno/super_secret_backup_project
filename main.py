import random
import pygame
from pygame.locals import *
import time




class Bomb:
    def  __init__(self):
        self.x=random.randint(0,10)
        self.y=random.randint(0,10)


    
class Squirell:
    def  __init__(self, num, x,y):
        self.num=num
        self.x=x
        self.y=y
        self.alive = True
        
    def nextrandommove(self):
        rando= random.randint(0,4)
        if rando==0:
            self.x-=1
        elif rando==1:
            self.x+=1
        elif rando==2:
            self.y+=1
        elif rando==3:
            self.y+=1


    def nextcontrolmove(self, int):
        if int=="left":
            self.x-=1
        elif int=="right":
            self.x+=1
        elif int=="up":
            self.y+=1
        elif int=="down":
            self.y+=1

    def boomquestionmark(self, list):
        for i in list:
            if list[1]==self.x:
                return True
            if list[2]==self.y:
                return True
        return False
        

def coor(x):
    return (x-1)*100


def findadeadyeo(list):
    mynum=1
    for i in range(10):
        for k in list:
            if i!=k.num:
                return i
    return i




def main():
    pygame.init()
    
    bomblist=[]
    list = []
    active = True

    screen = pygame.display.set_mode((1000,1000))
    clock = pygame.time.Clock()
    background = pygame.image.load('background.png').convert()
    screen.blit(background, (0, 0))
    firstsquirrel = Squirell(1,5,5)
    numberofsquirells = 1


    image1_not_scaled = pygame.image.load("squirrel_template_1.png")
    image1 = pygame.transform.scale(image1_not_scaled, (90, 90))  

    list.append(firstsquirrel)
    screen.blit(image1, (coor(firstsquirrel.x-1),coor(firstsquirrel.y)))
    alivesquirrels=[firstsquirrel]


    bomb_not_scaled = pygame.image.load("bomb.png")
    bomb_image = pygame.transform.scale(bomb_not_scaled, (90, 90))  

    bomb1=Bomb()
    screen.blit(bomb_image, (coor(bomb1.x),coor(bomb1.y)))
    bomblist.append(bomb1)


    bomb2=Bomb()
    screen.blit(bomb_image, (coor(bomb2.x),coor(bomb2.y)))
    bomblist.append(bomb2)

    
    bomb3=Bomb()
    screen.blit(bomb_image, (coor(bomb3.x),coor(bomb3.y)))
    bomblist.append(bomb3)

    bomb1=Bomb()
    screen.blit(bomb_image, (coor(bomb1.x),coor(bomb1.y)))
    bomblist.append(bomb1)


    bomb2=Bomb()
    screen.blit(bomb_image, (coor(bomb2.x),coor(bomb2.y)))
    bomblist.append(bomb2)

    
    bomb3=Bomb()
    screen.blit(bomb_image, (coor(bomb3.x),coor(bomb3.y)))
    bomblist.append(bomb3)



    pygame.display.set_caption('Save Yobie')
   
    line_color = (255,255,255)

    for i in range (11):
        pygame.draw.line(screen,line_color, ( (99.9*i), 0), ((99.9 *i), 1000))
        pygame.draw.line(screen,line_color, (0, (99.9*i)), (1000, (99.9*i)))

    pygame.display.update()
    turns = 0
    numberofsquirells = 0
    while active:
        
        con=0
        key = "none"
        
        
        if turns%3==0 and numberofsquirells<9:
            i=findadeadyeo(alivesquirrels)
            nextaddedsquirrell = Squirell(i,random.randint(0,10),random.randint(0,10))
            alivesquirrels.append(nextaddedsquirrell)
            numberofsquirells += 1

        for event in pygame.event.get():
            
            keypressed=False

            
            if event.type == pygame.KEYDOWN:
                keypressed=True
                print( "A key is pressed down" )

                if event.key == pygame.K_1:
                    con = 1
                if event.key == pygame.K_2:
                    con = 2
                if event.key == pygame.K_3:
                    con = 3
                if event.key == pygame.K_4:
                    con = 4
                if event.key == pygame.K_5:
                    con = 5
                if event.key == pygame.K_6:
                    con = 6
                if event.key == pygame.K_7:
                    con = 7
                if event.key == pygame.K_8:
                    con = 8
                if event.key == pygame.K_9:
                    con =9

                

                if event.key == pygame.K_UP:
                   key = "up"
                if event.key == pygame.K_LEFT:
                    key = "left"
                if event.key == pygame.K_RIGHT:
                    key = "right"
                if event.key == pygame.K_DOWN:
                    key = "down"
                if event.key == pygame.K_ESCAPE:
                    active = False
                    pygame.quit()
                    quit()
         

            con = con +1     
            
            count=0
            for squirell in alivesquirrels:
                if keypressed:
                    if squirell.num==con:
                        squirell.move(key)
                else: 
                    squirell.nextrandommove()
            
            for bomb in bomblist:
                for squirell in alivesquirrels:
                    if bomb.x==squirell.x:
                        if bomb.y==squirell.y:
                            alivesquirrels.remove(squirell)
            
            print(con)
            pygame.display.update()
            time.sleep(1)
            


        turns+=1
 
                
        
if __name__ == "__main__":
    main()