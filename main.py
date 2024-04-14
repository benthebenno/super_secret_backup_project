import random
import pygame
from pygame.locals import *
import time


class Bomb:
    def  __init__(self):
        self.x=random.randint(0,9)
        self.y=random.randint(0,9)


    
class Squirrel():
    def  __init__(self, num, x,y):
        
        self.num=num
        self.x=x
        self.y=y
        self.alive = True

    def boomquestionmark(self, bomblist_x,bomblist_y):
        for i in range(3):
            if bomblist_x[i]==self.x and bomblist_y[i]==self.y:
                return True
        return False
    
        
    

def coor(x):
    return (x)*100


def findadeadyeo(list):
    mynum=1
    for i in range(10):
        for k in list:
            if i!=k.num:
                return i
    return i




def main():
    pygame.init()
    time_count = 0
    bomblist_x=[]
    bomblist_y=[]

    active = True

    screen = pygame.display.set_mode((1000,1000))
    background = pygame.image.load('background.png').convert()
    screen.blit(background, (0, 0))
    firstsquirrel = Squirrel(1,5,5)
    numberofsquirrels = 1


    image1_not_scaled = pygame.image.load("whitesquirrel.png")
    image1 = pygame.transform.scale(image1_not_scaled, (90, 90))  

    screen.blit(image1, (coor(firstsquirrel.x),coor(firstsquirrel.y)))
    alivesquirrels = []
    alivesquirrels.append(firstsquirrel)


    bomb_not_scaled = pygame.image.load("bomb.png")
    bomb_image = pygame.transform.scale(bomb_not_scaled, (90, 90))  
    bomb1=Bomb()
    bomb2=Bomb()
    bomb3=Bomb()
    
    bomb1.x=5
    bomb1.y=5
    bomb2.x=5
    bomb2.y=5
    bomb3.x=5
    bomb3.y=5

    # This is Jesses pride and joy, please appriciate 
    while( ( (bomb1.x==5 and bomb1.y==5))) or  (bomb2.x==5 and bomb2.y==5) or ( (bomb3.x==5 and bomb3.y==5)) or ((bomb3.x==bomb1.x and bomb3.y==bomb1.y) or (bomb2.x==bomb3.x and bomb2.y==bomb3.y)) or(bomb2.x==bomb1.x and bomb2.y==bomb1.y):
        bomb1=Bomb()
       


        bomb2=Bomb()
        

        
        bomb3=Bomb()
        
    screen.blit(bomb_image, (coor(bomb1.x),coor(bomb1.y)))
    bomblist_x.append(bomb1.x)
    bomblist_y.append(bomb1.y)
    screen.blit(bomb_image, (coor(bomb2.x),coor(bomb2.y)))
    bomblist_x.append(bomb2.x)
    bomblist_y.append(bomb2.y)
    screen.blit(bomb_image, (coor(bomb3.x),coor(bomb3.y)))
    bomblist_x.append(bomb3.x)
    bomblist_y.append(bomb3.y)
    print("bomblist x")
    print(bomblist_x)
    print("bomblist y")
    print(bomblist_y)

    pygame.display.set_caption('Save Yobie')
   
    line_color = (255,255,255)

    for i in range (11):
        pygame.draw.line(screen,line_color, ( (99.9*i), 0), ((99.9 *i), 1000))
        pygame.draw.line(screen,line_color, (0, (99.9*i)), (1000, (99.9*i)))

    pygame.display.update()

    turns = 0
    con = 0
    key = "none"


    while active:

        
        if  numberofsquirrels<8:
            i = numberofsquirrels+1
            nextaddedsquirrel = Squirrel(i,random.randint(0,9),random.randint(0,9))
            alivesquirrels.append(nextaddedsquirrel)
            numberofsquirrels += 1

        con = str(input('Squirrel Choice:'))
        key = str(input("Movement:"))
        
        if key == "p":
            pygame.quit()
            quit()
    
        #This for loop will iterate through all the current squirrels and move them
        for squirrel in alivesquirrels:
            replacement = pygame.image.load('background.png')
            rep = pygame.transform.scale(replacement, (90, 90))
            screen.blit(rep, (coor(squirrel.x),coor(squirrel.y)))
            pygame.display.update()
            #print("Squirrel x:"+str(squirrel.x))
            #print("Squirrel y:"+str(squirrel.y))
            
            
            #This if will check if a Squirrel is on a bomb
            if squirrel.boomquestionmark(bomblist_x,bomblist_y):

                explosion = pygame.image.load("explosion.png")
                screen.blit(explosion, (0,0))
                pygame.display.update()
                print("boo hooo")
                print("Well Done")
                time.sleep(4)
                pygame.quit()
                quit()

            squirrel_file = str(squirrelImage(squirrel.num))

        # If this is the Squirrel you selected it will allow you to move it, depending on the direction specified
            if str(squirrel.num) == str(con):
 
                if key == "w":
                    temp_image_not_scaled = pygame.image.load(squirrel_file)
                    temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                    squirrel.y =squirrel.y - 1 
                    if squirrel.y<0:
                        squirrel.y=9
                    screen.blit(temp_image, (coor(squirrel.x),coor(squirrel.y)))
                    
                    
                    #print("Squirrel y changed:"+str(squirrel.y))

                if key == "s":
                    temp_image_not_scaled = pygame.image.load(squirrel_file)
                    temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                    
                    squirrel.y = squirrel.y + 1
                    if squirrel.y>9:
                        squirrel.y=0
                    screen.blit(temp_image, (coor(squirrel.x),coor(squirrel.y)))  
                    
                if key == "a":
                    temp_image_not_scaled = pygame.image.load(squirrel_file)
                    temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                    
                    squirrel.x = squirrel.x - 1 
                    if squirrel.x<0:
                        squirrel.x=9
                    screen.blit(temp_image, (coor(squirrel.x),coor(squirrel.y))) 
                if key == "d":

                    temp_image_not_scaled = pygame.image.load(squirrel_file)
                    temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                    
                    squirrel.x = squirrel.x + 1
                    if squirrel.x>9:
                        squirrel.x=0
                    screen.blit(temp_image, (coor(squirrel.x),coor(squirrel.y))) 
              
                    
            #This will move the Squirrel in a random direction
            else:
            
                rand_num = random.randint(0,3)

                #up
                if rand_num == 0:
                    temp_image_not_scaled = pygame.image.load(squirrel_file)
                    temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                    
                    squirrel.y =squirrel.y-1
                    if squirrel.y>9:
                        squirrel.y=0
                    screen.blit(temp_image, (coor(squirrel.x),coor(squirrel.y)))
                    
                    #down
                if rand_num == 1:
                    temp_image_not_scaled = pygame.image.load(squirrel_file)
                    temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                    
                    squirrel.y = squirrel.y + 1
                    if squirrel.y<0:
                        squirrel.y=9
                    screen.blit(temp_image, (coor(squirrel.x),coor(squirrel.y)))  
                    
                    #left
                if rand_num == 2:
                    temp_image_not_scaled = pygame.image.load(squirrel_file)
                    temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                    
                    squirrel.x = squirrel.x -1
                    if squirrel.x<0:
                        squirrel.x=9
                    screen.blit(temp_image, (coor(squirrel.x),coor(squirrel.y)))
                    
                    #right
                if rand_num == 3:
                    temp_image_not_scaled = pygame.image.load(squirrel_file)
                    temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                    
                    squirrel.x = squirrel.x +1
                    if squirrel.x>9:
                        squirrel.x=0
                    screen.blit(temp_image, (coor(squirrel.x),coor(squirrel.y))) 
            #print("squirrel number "+str(squirrel.num)+" squirrel square ("+str(squirrel.x)+','+str(squirrel.y)+")")
                    
          
            pygame.display.update()
        time_count = time_count + 1
        print("Congrats you have protected your squirrels for " + str(time_count) + " turns")
        turns+=1
 
                


def squirrelImage(numb):
    hope = True
    if (numb==1):
        return 'whitesquirrel.png'
    if (numb==2):
        return 'squirrel_template_2.png'
    if (numb==3):
        return 'squirrel_template_3.png'
    if (numb==4):
        return 'squirrel_template_4.png'
    if (numb==5):
        return 'squirrel_template_5.png'
    if (numb==6):
        return 'squirrel_template_6.png'
    if (numb==7):
        return 'squirrel_template_7.png'
    if (numb==8):
        return 'squirrel_template_8.png'
    if (numb==9):
        return 'squirrel_template_9.png'
    else:
        return "failed"
    
        
if __name__ == "__main__":
    main()



