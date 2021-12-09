import pygame
import time
import sys
import random
pygame.init()
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
font_style = pygame.font.SysFont("bahnschrift", 15)
font_style1 = pygame.font.SysFont("bahnschrift", 50)
#bg_color=pygame.Color('grey12')
clock=pygame.time.Clock()
dis=pygame.display.set_mode((800,600))
pygame.display.set_caption("pong game")
pygame.display.update()    
ball=pygame.draw.rect(dis,white,[800/2-10,600/2-10,20,20])
player1=pygame.Rect(800-10,600/2-50,10,100)
player2=pygame.Rect(0,600/2-50,10,100)
l=[1,-1]
ball_sign_x=random.choice(l)
ball_sign_y=random.choice(l)
player1_speed=0
player2_speed=3
p1=0
p2=0
def message(msg,color,x,y):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,[x,y])

def message1(msg,color,x,y):
    mesg=font_style1.render(msg,True,color)
    dis.blit(mesg,[x,y])

def new_ball():
    global ball_sign_x,ball_sign_y,ball
    ball=pygame.draw.ellipse(dis,white,[800/2-10,600/2-10,20,20])
    ball_sign_x=random.choice(l)
    ball_sign_y=random.choice(l)
    pygame.display.update()

def ball_working():
    global ball_sign_x,ball_sign_y,p1,p2
    if ball.left<=0:
        p1+=1
        new_ball()
        for y in range(1,1000):
                    n=4
                    j=n
                    k=j+n
                    print(' ') 
    if ball.right>=800:
        p2+=1
        new_ball()
        for y in range(1,1000):
                    n=4
                    j=n
                    k=j+n
                    print(' ') 
    if ball.bottom>=600 or ball.top<=0:
        ball_sign_y*=-1    
    if ball.colliderect(player1):
        ball_sign_x*=-1
    if ball.colliderect(player2):
        ball_sign_x*=-1
    ball_change_x=2*ball_sign_x
    ball_change_y=2*ball_sign_y
    ball.x=ball.x+ball_change_x
    ball.y=ball.y+ball_change_y
    pygame.draw.ellipse(dis,white,[ball.x,ball.y,20,20])
    message(f'{p1}',blue,780,0)
    message(f'{p2}',blue,60,0)
    pygame.display.update()
def player1_working():
    player1.y+=player1_speed
    if player1.top<=0:
        player1.top=0
    if player1.bottom>=600:
        player1.bottom=600
def player2_working():
    if player2.top<=0:
        player2.top=0
    if player2.bottom>=600:
        player2.bottom=600

    
        
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                player1_speed+=3
            if event.key==pygame.K_UP:
                player1_speed-=3   
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                player1_speed-=3
            if event.key==pygame.K_UP:
                player1_speed+=3
    if player2.top<ball.y:
       player2.top+=player2_speed 
    if player2.bottom>ball.y:
        player2.bottom-=player2_speed   
    
    
    player1_working()
    player2_working()

    dis.fill(black)
    message('SCORE:',blue,10,0)
    message('SCORE:',blue,730,0)
    pygame.draw.rect(dis,white,player2)
    pygame.draw.rect(dis,white,player1)
    pygame.draw.rect(dis,white,[399,0,1,600])
    
    if p1==5:
        dis.fill(black)
        message1('P1 WON',blue,360,275)
        for y in range(1,15000):
                    n=4
                    j=n
                    k=j+n
                    print(' ')
        pygame.display.flip()            
        break            
    if p2==5:
        dis.fill(black)
        message1('P2 WON',blue,360,275)
        for y in range(1,15000):
                    n=4
                    j=n
                    k=j+n
                    print(' ')
        pygame.display.flip()            
        break 
    ball_working()           
    pygame.display.flip()
    clock.tick(200)
pygame.quit()
quit()    
