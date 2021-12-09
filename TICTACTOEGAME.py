# import TICTACTO
# import TICTACTOE
import pygame
pygame.init()
dis=pygame.display.set_mode((600,600))
pygame.display.set_caption("TIC TAC TOE")
yellow = (255, 255, 102)
blue=(0,0,255)
font_style = pygame.font.SysFont("bahnschrift", 25)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[100,300]) 
def message1(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[150,350])                                    
while True:
    message("""A.2PLAYER    B.WITHCOMPUTER""",yellow)
    pygame.display.update()           
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                import TICTACTO 
            elif event.key==pygame.K_b:
                import TICTACTOE   
            if event.type==pygame.QUIT:
                pygame.quit()                                
pygame.quit()
quit()         
  


