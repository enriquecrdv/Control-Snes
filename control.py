import pygame
pygame.init()
clk=pygame.time.Clock()
size=width,height=300,169
screen=pygame.display.set_mode(size)
background_image=pygame.image.load('control.png').convert()
frameRect=pygame.Rect((0,0),(width,height))
crosshair=pygame.surface.Surface((10,10))
pygame.draw.circle(crosshair,pygame.Color('black'),(5,5),5,0)
crosshairb=pygame.surface.Surface((10,10))
pygame.draw.circle(crosshairb,pygame.Color('red'),(5,5),5,0)
while True:
    pygame.event.pump()
    screen.blit(background_image,(0,0))
    Keys=pygame.key.get_pressed()
    if Keys[pygame.K_i]:screen.blit(crosshair,(228,61))
    if Keys[pygame.K_l]:screen.blit(crosshair,(255,84))
    if Keys[pygame.K_k]:screen.blit(crosshair,(228,108))
    if Keys[pygame.K_j]:screen.blit(crosshair,(198,84))
    x=-1 if Keys[pygame.K_a] else 1 if Keys[pygame.K_d]else 0
    y=-1 if Keys[pygame.K_w] else 1 if Keys[pygame.K_s]else 0
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(crosshairb,((x*20)+64-5,(y*20)+89-5))
    pygame.display.flip()

    clk.tick(40)
