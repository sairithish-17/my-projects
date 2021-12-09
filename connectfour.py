import pygame
import time
pygame.init()
dis=pygame.display.set_mode((740,740))
pygame.display.set_caption('CONNECT FOUR')
pygame.display.update()
white=(255,255,255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80) 
green = (0, 255, 0)
blue = (50, 153, 213)
m=[
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
]
dis.fill(blue)
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 50)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[300,200]) 
def message1(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[10,350])  
# def matrix():
# def player1():
#     pygame.draw.ellipse(dis,yellow,[5,105,100,100])
#     for event in pygame.event.get():
#         if event.type==pygame.KEYDOWN
#ball1=pygame.Rect(x1,5,100,100)
# def p1():
#     global x1
#     ball1=pygame.Rect(x1,5,100,100)
#     pygame.draw.ellipse(dis,red,ball1)
    # for event in pygame.event.get():
    #     if event.type==pygame.KEYDOWN:
    #         if event.key==pygame.K_LEFT:
    #             if x1<=5:
    #                 x1=5
    #             else:
    #                 x1-=105      
    #         if event.key==pygame.K_RIGHT:
    #             if ball1.right>=735:
    #                 ball1.right=735
    #             else:
    #                 x1+=105     
    # pygame.draw.ellipse(dis,red,ball1)
    # pygame.display.update()                    

# l=0                
# ball=[]
# x.append(5)
    # y.append(5)    
z=0
w=''
def game_loop():
    global z,w
    
    x1=0
    y1=0
    # x=[]
    # y=[]
    c=0
    d=0
    # def won(v):
    #     for y in range(1,400):
    #         n=4
    #         j=n
    #         k=j+n
    #         print(' ')
    #     dis.fill(white)
    #     message(f"{v}",black)
    #     message1('Q-QUIT P-PLAYAGAIN',blue)
    #     pygame.display.update()
    #     for event in pygame.event.get():
    #         if event.type==pygame.KEYDOWN:
    #             if event.key==pygame.K_q:
    #                 pygame.quit()
    #             if event.key==pygame.K_p:
    #                 game_loop()            
    #     pygame.display.update()
    game_close=False
    game_over=False
    while not game_over:
        while game_close == True:
            for y in range(1,400):
                n=4
                j=n
                k=j+n
                print(' ')
            dis.fill(blue)
            message1("Press C-Play Again or Q-Quit", red)
            if w=='p1':
                message("player 1 won",black)
            elif w=='p2':
                message("player 2 won",black)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        game_close = False
                    if event.key == pygame.K_c:
                        import connectfour
        
        ball1=pygame.Rect(x1,y1,100,100)    
        # ball.append(ball1)
        dis.fill(blue)
        if z%2==0:                                             
            pygame.draw.ellipse(dis,red,ball1)
        else:
            pygame.draw.ellipse(dis,yellow,ball1)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:    
                    if x1<=5:
                        x1 =5
                    else:
                        x1-=105
                        c-=1
                    dis.fill(blue)                                            
                    pygame.draw.ellipse(dis,red,ball1)                          
                if event.key==pygame.K_RIGHT:
                    if ball1.right>=735:
                        ball1.right=735
                    else:
                        x1+=105
                        c+=1
                    dis.fill(blue)                                            
                    pygame.draw.ellipse(dis,red,ball1)
                if event.key==pygame.K_q:
                    pygame.quit()                             
                if event.key==pygame.K_DOWN:
                    for k in range(0,6):
                        if m[5-k][c]==0:
                            y1=(6-k)*105
                            if z%2==0:
                                m[5-k][c]=1
                            elif z%2!=0: 
                                m[5-k][c]=2   
                            dis.fill(blue)                                            
                            if z%2==0:                                             
                                pygame.draw.ellipse(dis,red,ball1)
                            elif z%2!=0: 
                                pygame.draw.ellipse(dis,yellow,ball1)
                            z=z+1
                            game_loop()
                            # l=l+1
                            # x.append(5)
                            # y.append(5) 
                            break
                        else:
                            continue    
                    # if ball1.bottom>=735:
                    #     ball1.bottom=735 
                    # else:
                    #     y1=635
                
        for i in range(0,6):
            for j in range(0,7):
                if m[i][j]==0:
                    pygame.draw.ellipse(dis,black,[(5*(j+1))+(100*(j)),(105+(5*(i+1))+(100*(i))),100,100]) 
                elif m[i][j]==1:
                    pygame.draw.ellipse(dis,red,[(5*(j+1))+(100*(j)),(105+(5*(i+1))+(100*(i))),100,100])
                elif m[i][j]==2:
                    pygame.draw.ellipse(dis,yellow,[(5*(j+1))+(100*(j)),(105+(5*(i+1))+(100*(i))),100,100])
        pygame.display.flip()
        clock.tick(100)
            
        for i in range(0,6):
            for j in range(0,4):
                if m[5-i][j]==1 and m[5-i][j+1]==1 and m[5-i][j+2]==1 and m[5-i][j+3]==1:
                    w='p1'
                    game_close=True
                elif m[5-i][j]==2 and m[5-i][j+1]==2 and m[5-i][j+2]==2 and m[5-i][j+3]==2:
                    w='p2'
                    game_close=True
        for j in range(0,7):
            for i in range(0,3):
                if m[5-i][j]==1 and m[4-i][j]==1 and m[3-i][j]==1 and m[2-i][j]==1:
                    w='p1'
                    game_close=True
                elif m[5-i][j]==2 and m[4-i][j]==2 and m[3-i][j]==2 and m[2-i][j]==2:
                    w='p2'
                    game_close=True    
        for j in range(0,4):
            for i in range(0,3):
                if m[i][j]==1 and m[i+1][j+1]==1 and m[i+2][j+2]==1 and m[i+3][j+3]==1:
                    w='p1'
                    game_close=True
                elif m[i][j]==2 and m[i+1][j+1]==2 and m[i+2][j+2]==2 and m[i+3][j+3]==2:
                    w='p2'
                    game_close=True
                if m[5-i][j]==1 and m[5-i-1][j+1]==1 and m[5-i-2][j+2]==1 and m[5-i-3][j+3]==1:
                    w='p1'
                    game_close=True
                elif m[5-i][j]==2 and m[5-i-1][j+1]==2 and m[5-i-2][j+2]==2 and m[5-i-3][j+3]==2:
                    w='p2'
                    game_close=True        
                                            
    pygame.quit()
    quit() 
game_loop()           