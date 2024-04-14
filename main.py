import random
import pygame
from pygame.locals import *
import time




class Bomb:
    def  __init__(self):
        self.x=random.randint(0,10)
        self.y=random.randint(0,10)


    
class Squirrel():
    def  __init__(self, num, x,y):
        
        self.num=num
        self.x=x
        self.y=y
        self.alive = True
        
    # def nextrandommove(self):
    #     rando= random.randint(0,4)
    #     if rando==0:
    #         self.x-=1
    #     elif rando==1:
    #         self.x+=1
    #     elif rando==2:
    #         self.y+=1
    #     elif rando==3:
    #         self.y+=1


    # def nextcontrolmove(self, int):
    #     if int=="left":
    #         if self.x-1<0:
    #             self.x=10
    #         self.x-=1
    #     elif int=="right":
    #         if self.x+1>9:
    #             self.x=-1
    #         self.x+=1
    #     elif int=="up":
    #         if self.x+1>9:
    #             self.x=0
    #         self.y+=1
    #     elif int=="down":
    #         if self.x+1>9:
    #             self.x=-1
    #         self.y+=1

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
    # clock = pygame.time.Clock()
    background = pygame.image.load('background.png').convert()
    screen.blit(background, (0, 0))
    firstsquirrel = Squirrel(1,5,5)
    numberofsquirrels = 1


    image1_not_scaled = pygame.image.load("squirrel_template_1.png")
    image1 = pygame.transform.scale(image1_not_scaled, (90, 90))  

    # list.append(firstsquirrel)
    screen.blit(image1, (coor(firstsquirrel.x),coor(firstsquirrel.y)))
    alivesquirrels = []
    alivesquirrels.append(firstsquirrel)
    # [firstsquirrel]


    bomb_not_scaled = pygame.image.load("bomb.png")
    bomb_image = pygame.transform.scale(bomb_not_scaled, (90, 90))  

    bomb1=Bomb()
    screen.blit(bomb_image, (coor(bomb1.x),coor(bomb1.y)))
    bomblist_x.append(bomb1.x)
    bomblist_y.append(bomb1.y)


    bomb2=Bomb()
    screen.blit(bomb_image, (coor(bomb2.x),coor(bomb2.y)))
    bomblist_x.append(bomb2.x)
    bomblist_y.append(bomb2.y)

    
    bomb3=Bomb()
    screen.blit(bomb_image, (coor(bomb3.x),coor(bomb3.y)))
    bomblist_x.append(bomb3.x)
    bomblist_y.append(bomb3.y)



    pygame.display.set_caption('Save Yobie')
   
    line_color = (255,255,255)

    for i in range (11):
        pygame.draw.line(screen,line_color, ( (99.9*i), 0), ((99.9 *i), 1000))
        pygame.draw.line(screen,line_color, (0, (99.9*i)), (1000, (99.9*i)))

    pygame.display.update()
    turns = 0
    con=0
    key = "none"


    while active:
        
        if turns%9==0 and numberofsquirrels<8:
            i=numberofsquirrels+1
            nextaddedsquirrel = Squirrel(i,random.randint(0,10),random.randint(0,10))
            alivesquirrels.append(nextaddedsquirrel)
            numberofsquirrels += 1

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                print( "A key is pressed down" )

                if event.key == pygame.K_1:
                    print("hellodedfe")
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
                   print("uppies")
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
         

            
            count=0
            
            # for bomb in range(3):
            #     for squirrel in alivesquirrels:
            #         if bomblist_x[bomb]==squirrel.x:
            #             if bomblist_y[bomb]==squirrel.y:
            #                 alivesquirrels.remove(squirrel)

            # list.clear()

            # for i in alivesquirrels:
            #     list.append(i.x)
            #     list.append(i.y)

            for squirrel in alivesquirrels:

                
                replacement = pygame.image.load('background.png')
                rep = pygame.transform.scale(replacement, (90, 90))
                screen.blit(rep, (coor(squirrel.x),coor(squirrel.y)))
                pygame.display.update()

                if squirrel.boomquestionmark(bomblist_x,bomblist_y):

                    explosion = pygame.image.load("explosion.png")
                    # explosion_image = pygame.transform.scale(explosion, (90, 90)) 
                    screen.blit(explosion, (0,0))
                    pygame.display.update()
                    print("boo hooo")
                    time.sleep(4)
                    pygame.quit()
                    quit()


                #This replaces the Squirrel with a green block
                

                # print(alivesquirrels)
                # print(squirrel.num)
                squirrel_file = str(squirrelImage(squirrel.num))


                print(squirrel.num)
                print(con)
                print("1 num, 2 con")
                if squirrel.num == con:
                    if key == "up":
                        temp_image_not_scaled = pygame.image.load(squirrel_file)
                        temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                        if squirrel.y+1>9:
                            squirrel.y=0
                        screen.blit(temp_image, (coor(squirrel.x),coor(squirrel.y+1)))
                        squirrel.y =squirrel.y + 1 
                    if key == "down":
                        temp_image_not_scaled = pygame.image.load(squirrel_file)
                        temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                        if squirrel.y-1<0:
                            squirrel.y=9
                        screen.blit(temp_image, (coor(squirrel.x),coor(squirrel.y-1)))  
                        squirrel.y = squirrel.y - 1
                    if key == "left":
                        temp_image_not_scaled = pygame.image.load(squirrel_file)
                        temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                        if squirrel.x-1<0:
                            squirrel.x=9
                        screen.blit(temp_image, (coor(squirrel.x-1),coor(squirrel.y))) 
                        squirrel.x = squirrel.x - 1 
                    if key == "right":
                        temp_image_not_scaled = pygame.image.load(squirrel_file)
                        temp_image = pygame.image.transform.scale(temp_image_not_scaled, (90, 90))
                        if squirrel.x+1>9:
                            squirrel.x=0
                        screen.blit(temp_image, (coor(squirrel.x+1),coor(squirrel.y)))    
                        squirrel.x = squirrel.x + 1
                    pygame.display.update()

                else:
                    rand_num = random.randint(0,4)
                    if rand_num == 0:
                        temp_image_not_scaled = pygame.image.load(squirrel_file)
                        temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                        if squirrel.y+1>9:
                            squirrel.y=0
                        screen.blit(temp_image, (coor(squirrel.x),coor(squirrel.y+1)))
                        squirrel.y =squirrel.y+1

                    if rand_num == 1:
                        temp_image_not_scaled = pygame.image.load(squirrel_file)
                        temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                        if squirrel.y-1<0:
                            squirrel.y=9
                        screen.blit(temp_image, (coor(squirrel.x),coor(squirrel.y-1)))  
                        squirrel.y = squirrel.y -1
                        
                    if rand_num == 2:
                        temp_image_not_scaled = pygame.image.load(squirrel_file)
                        temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                        if squirrel.x-1<0:
                            squirrel.x=9
                        screen.blit(temp_image, (coor(squirrel.x-1),coor(squirrel.y)))
                        squirrel.x = squirrel.x -1

                    if rand_num == 3:
                        temp_image_not_scaled = pygame.image.load(squirrel_file)
                        temp_image = pygame.transform.scale(temp_image_not_scaled, (90, 90))
                        if squirrel.x+1>9:
                            squirrel.x=0
                        screen.blit(temp_image, (coor(squirrel.x+1),coor(squirrel.y))) 
                        squirrel.x = squirrel.x +1
                
                
            pygame.display.update()
            time.sleep(1)
            time_count = time_count + 1
            print("Congrats you have protected your squirrels for " + str(time_count) + " seconds")
            
            


        turns+=1
 
                


def squirrelImage(numb):
    hope = True
    if (numb==1):
        return 'squirrel_template_1.png'
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



