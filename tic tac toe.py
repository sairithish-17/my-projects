import pygame
import time
pygame.init()
dis=pygame.display.set_mode((600,600))

pygame.display.update()
pygame.display.set_caption('TIC TAC TOE')

white=(255,255,255)
red = (213, 50, 80)
blue = (50, 153, 213)
m=0
q,w,e,a,s,d,z,x,c=(0,0,0,0,0,0,0,0,0,)
font_style = pygame.font.SysFont("bahnschrift", 25)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [300,300])
game_over=False
while not game_over:
    def p1():
        global m,q,w,e,a,s,d,z,x,c
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.draw.rect(dis,red,[100,100,60,60])
                    pygame.display.update()
                    m=m+1
                    q=1
                elif event.key==pygame.K_w:
                    pygame.draw.rect(dis,red,[300,100,60,60])
                    pygame.display.update()
                    m=m+1
                    w=1
                elif event.key==pygame.K_e:
                    pygame.draw.rect(dis,red,[500,100,60,60])
                    pygame.display.update()
                    m=m+1
                    e=1    
                elif event.key==pygame.K_a:
                    pygame.draw.rect(dis,red,[100,300,60,60])
                    pygame.display.update()
                    m=m+1
                    a=1
                elif event.key==pygame.K_s:
                    pygame.draw.rect(dis,red,[300,300,60,60])
                    pygame.display.update()
                    m=m+1
                    s=1    
                elif event.key==pygame.K_d:
                    pygame.draw.rect(dis,red,[500,300,60,60])
                    pygame.display.update()
                    m=m+1
                    d=1
                elif event.key==pygame.K_z:
                    pygame.draw.rect(dis,red,[100,500,60,60])
                    pygame.display.update()
                    m=m+1
                    z=1    
                elif event.key==pygame.K_x:
                    pygame.draw.rect(dis,red,[300,500,60,60])
                    pygame.display.update()
                    m=m+1
                    x=1    
                elif event.key==pygame.K_c:
                    pygame.draw.rect(dis,red,[500,500,60,60])
                    pygame.display.update()
                    m=m+1
                    c=1                                                  
                elif event.key==pygame.K_o:
                    pygame.quit()
                    
    def p2():
        global m,q,w,e,a,s,d,z,x,c
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.draw.rect(dis,blue,[100,100,20,20])
                    pygame.display.update()
                    m=m+1
                    q=2
                elif event.key==pygame.K_w:
                    pygame.draw.rect(dis,blue,[300,100,20,20])
                    pygame.display.update()
                    m=m+1
                    w=2
                elif event.key==pygame.K_e:
                    pygame.draw.rect(dis,blue,[500,100,20,20])
                    pygame.display.update()
                    m=m+1
                    e=2    
                elif event.key==pygame.K_a:
                    pygame.draw.rect(dis,blue,[100,300,20,20])
                    pygame.display.update()
                    m=m+1
                    a=2
                elif event.key==pygame.K_s:
                    pygame.draw.rect(dis,blue,[300,300,20,20])
                    pygame.display.update()
                    m=m+1
                    s=2    
                elif event.key==pygame.K_d:
                    pygame.draw.rect(dis,blue,[500,300,20,20])
                    pygame.display.update()
                    m=m+1
                    d=2
                elif event.key==pygame.K_z:
                    pygame.draw.rect(dis,blue,[100,500,20,20])
                    pygame.display.update()
                    m=m+1
                    z=2    
                elif event.key==pygame.K_x:
                    pygame.draw.rect(dis,blue,[300,500,20,20])
                    pygame.display.update()
                    m=m+1
                    x=2    
                elif event.key==pygame.K_c:
                    pygame.draw.rect(dis,blue,[500,500,20,20])
                    pygame.display.update()
                    m=m+1
                    c=2                                                  
                elif event.key==pygame.K_o:
                    pygame.quit()                                  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis,white,[200,0,10,600])
    pygame.draw.rect(dis,white,[400,0,10,600])
    pygame.draw.rect(dis,white,[0,200,600,10])
    pygame.draw.rect(dis,white,[0,400,600,10])
    pygame.display.update() 
    if m%2==0:
        p1()
    elif m%2!=0:
        p2()
    if (q==1 and w==1 and e==1) or (a==1 and s==1 and d==1) or (z==1 and x==1 and c==1) or (q==1 and s==1 and c==1) or (z==1 and s==1 and e==1) or (q==1 and a==1 and z==1 ) or (w==1 and s==1 and x==1) or (e==1 and d==1 and c==1 ):
        dis.fill(white)
        message("p1 won",blue)
        pygame.display.update()
    elif (q==2 and w==2 and e==2) or (a==2 and s==2 and d==2) or (z==2 and x==2 and c==2) or (q==2 and s==2 and c==2) or (z==2 and s==2 and e==2) or (q==2 and a==2 and z==2 ) or (w==2 and s==2 and x==2) or (e==2 and d==2 and c==2 ):
        dis.fill(white)
        message("p2 won",blue)
        pygame.display.update()      
    elif m==9:
        dis.fill(white)
        message("tie",blue)
        pygame.display.update()

pygame.quit()
quit()