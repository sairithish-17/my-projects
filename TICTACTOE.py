m=0
q,w,e,a,s,d,z,x,c=(0,0,0,0,0,0,0,0,0)
l=[q,w,e,a,s,d,z,x,c]
l1=[]
def comp():
    import pygame
    import time
    import random
    pygame.init()
    dis=pygame.display.set_mode((600,600))
    pygame.display.update()
    pygame.display.set_caption('TIC TAC TOE')

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80) 
    green = (0, 255, 0)
    blue = (50, 153, 213)
    
    font_style = pygame.font.SysFont("bahnschrift", 20)
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [300,300])

    def message1(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg,[150,350])    
    game_over=False
    while not game_over:
        def p1(colour,v):
            global m,q,w,e,a,s,d,z,x,c
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.draw.rect(dis,colour,[100,100,30,30])
                        pygame.display.update()
                        m=m+1
                        q=v
                    elif event.key==pygame.K_w:
                        pygame.draw.rect(dis,colour,[300,100,30,30])
                        pygame.display.update()
                        m=m+1
                        w=v
                    elif event.key==pygame.K_e:
                        pygame.draw.rect(dis,colour,[500,100,30,30])
                        pygame.display.update()
                        m=m+1
                        e=v    
                    elif event.key==pygame.K_a:
                        pygame.draw.rect(dis,colour,[100,300,30,30])
                        pygame.display.update()
                        m=m+1
                        a=v
                    elif event.key==pygame.K_s:
                        pygame.draw.rect(dis,colour,[300,300,30,30])
                        pygame.display.update()
                        m=m+1
                        s=v    
                    elif event.key==pygame.K_d:
                        pygame.draw.rect(dis,colour,[500,300,30,30])
                        pygame.display.update()
                        m=m+1
                        d=v
                    elif event.key==pygame.K_z:
                        pygame.draw.rect(dis,colour,[100,500,30,30])
                        pygame.display.update()
                        m=m+1
                        z=v    
                    elif event.key==pygame.K_x:
                        pygame.draw.rect(dis,colour,[300,500,30,30])
                        pygame.display.update()
                        m=m+1
                        x=v    
                    elif event.key==pygame.K_c:
                        pygame.draw.rect(dis,colour,[500,500,30,30])
                        pygame.display.update()
                        m=m+1
                        c=v                                                  
                    elif event.key==pygame.K_o:
                        pygame.quit()

        def comp(colour,v):
            global m,q,w,e,a,s,d,z,x,c
            for item in l:
                if item==0:
                    l1.append(item)
                for y in range(1,500):
                    n=4
                    j=n
                    k=j+n
                    print(' ')        
            r=random.choice(l1)    
            if r==s:
                pygame.draw.rect(dis,colour,[300,300,30,30])
                pygame.display.update()
                m=m+1
                s=v 
            elif r==w:
                pygame.draw.rect(dis,colour,[300,100,30,30])
                pygame.display.update()
                m=m+1
                w=v
            elif r==e:
                pygame.draw.rect(dis,colour,[500,100,30,30])
                pygame.display.update()
                m=m+1
                e=v    
            elif r==z:
                pygame.draw.rect(dis,colour,[100,500,30,30])
                pygame.display.update()
                m=m+1
                z=v        
            elif r==q:
                pygame.draw.rect(dis,colour,[100,100,30,30])
                pygame.display.update()
                m=m+1
                q=v      
            elif r==d:
                pygame.draw.rect(dis,colour,[500,300,30,30])
                pygame.display.update()
                m=m+1
                d=v
            elif r==x:
                pygame.draw.rect(dis,colour,[300,500,30,30])
                pygame.display.update()
                m=m+1
                x=v     
            elif  r==c:
                pygame.draw.rect(dis,colour,[500,500,30,30])
                pygame.display.update()
                m=m+1
                c=v              
            elif r==a:
                pygame.draw.rect(dis,colour,[100,300,30,30])
                pygame.display.update()
                m=m+1
                a=v                                                   
            elif r==o:
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
            p1(red,1)
        elif m%2!=0:
            comp(blue,2)

        if (q==1 and w==1 and e==1) or (a==1 and s==1 and d==1) or (z==1 and x==1 and c==1) or (q==1 and s==1 and c==1) or (z==1 and s==1 and e==1) or (q==1 and a==1 and z==1 ) or (w==1 and s==1 and x==1) or (e==1 and d==1 and c==1 ):
            for y in range(1,400):
                    n=4
                    j=n
                    k=j+n
                    print(' ')
            dis.fill(white)
            message("p1 won",black)
            message1('Q-QUIT P-PLAYAGAIN',blue)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.quit()
                    if event.key==pygame.K_p:
                        import TICTACTOEGAME
            pygame.display.update()
        elif (q==2 and w==2 and e==2) or (a==2 and s==2 and d==2) or (z==2 and x==2 and c==2) or (q==2 and s==2 and c==2) or (z==2 and s==2 and e==2) or (q==2 and a==2 and z==2 ) or (w==2 and s==2 and x==2) or (e==2 and d==2 and c==2 ):
            for y in range(1,400):
                    n=4
                    j=n
                    k=j+n
                    print(' ')
            dis.fill(white)
            message("computer won",black)
            message1('Q-QUIT P-PLAYAGAIN',blue)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.quit()
                    if event.key==pygame.K_p:
                        import TICTACTOEGAME
            pygame.display.update()      
        elif m==9:
            for y in range(1,400):
                    n=4
                    j=n
                    k=j+n
                    print(' ')
            dis.fill(white)
            message("tie",black)
            message1('Q-QUIT P-PLAYAGAIN',blue)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.quit()
                    if event.key==pygame.K_p:
                        import TICTACTOEGAME
            pygame.display.update()

comp()
pygame.quit()
quit()

                              



