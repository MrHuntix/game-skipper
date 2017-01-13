import pygame
import time
import random
pygame.init()

white=(255,255,255)
red=(255,0,0)
asq=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
black=(0,0,0)
blue=(0,0,255)
pb=(0,255,255)
clock=pygame.time.Clock()
icon=pygame.image.load("jumper.png")
smallfont=pygame.font.SysFont("comicsansms",25)
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("comicsansms",80)
img=pygame.image.load('player.png')
img1=pygame.image.load('player2.png')
img2=pygame.image.load('object.png')
front=pygame.image.load('forward.png')
back=pygame.image.load('backward.png')
bnq=40
obj_disp=50
bgd=pygame.image.load('back.png')
gb=(255,255,108)
gnd=(130,65,0)
GameSurface=pygame.display.set_mode((800,600))
pygame.display.set_caption("skipper")
pygame.display.set_icon(icon)


def score(score):
    text=smallfont.render("Score: "+str(score),True,black)
    GameSurface.blit(text,[0,0])


def text_objects(text,colour,size):
    if size == "small":
        textSurface=smallfont.render(text,True,colour)
    elif size == "medium":
        textSurface=medfont.render(text,True,colour)
    elif size == "large":
        textSurface=largefont.render(text,True,colour)
    return textSurface,textSurface.get_rect()


def print_msg(msg,colour,y_displace,size="small"):
    textSurf,textRect=text_objects(msg,colour,size)
    textRect.center=400,(300)+y_displace
    GameSurface.blit(textSurf,textRect)


def pause():
    GamePause=True
    while GamePause:
        GameSurface.fill(pb)
        print_msg("GAME PAUSED",asq,-50,"large")
        print_msg('c:continue or q:quit',black,0,"small")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN and event.key==pygame.K_c:
                gamePause=False
                return


def GameLoop():
    ppos_x=400
    ppos_y=300
    px=0
    py=0
    obj_x=700
    obj_y=300
    GameOver=False
    GameStart=True
    scor=0
    while not GameOver:
    
        while GameStart==True:
            GameSurface.fill(gb)
            print_msg("JUMPER",asq,-50,"large")
            print_msg('s:start or q:quit or p:pause',black,0,"small")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
                    GameOver=True
                    GameStart=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_s:
                        GameStart=False

        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
                GameOver=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    pause()
                elif event.key==pygame.K_SPACE and (ppos_x==400 and ppos_y==300):
                    py=-150
                    ppos_x+=px
                    ppos_y+=py
                    GameSurface.fill(gb)
                    GameSurface.blit(img1,(ppos_x,ppos_y))
        clock.tick(random.randint(5,8)) 
        score(scor)
        pygame.display.update()
        obj_x-=obj_disp
        GameSurface.blit(img2,(obj_x,obj_y))
        if obj_x==ppos_x and obj_y==ppos_y:
            scor=0
            GameSurface.fill(gb)
            print_msg("Game Over",asq,-50,"large")
            pygame.display.update()
            clock.tick(20)
            GameStart=True
            obj_x=700
        if obj_x==300 and obj_y==300:
            scor+=1
            obj_x=700
            obj_y=300
            obj_x-=obj_disp
            GameSurface.blit(img2,(obj_x,obj_y))
            pygame.display.update()
        pygame.draw.line(GameSurface,gnd,(-300,335),(794,335),3)
        pygame.display.update()
        clock.tick(30)
        GameSurface.fill(gb)
        ppos_x=400
        ppos_y=300
        GameSurface.blit(img,(ppos_x,ppos_y))
    pygame.quit()
    quit()

GameLoop()
