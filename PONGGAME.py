import pygame
pygame.init()
dis=pygame.display.set_mode((600,600))
pygame.display.set_caption("TIC TAC TOE")
yellow = (255, 255, 102)
font_style = pygame.font.SysFont("bahnschrift", 25)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [100,300])
game_over=False                               
while not game_over:
    message("""A.2PLAYER    B.WITHCOMPUTER""",yellow)
    pygame.display.update()           
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                import PONG1GAME
            elif event.key==pygame.K_b:
                import PONG
            if event.type==pygame.QUIT:
                game_over=True             
pygame.quit()
quit()         