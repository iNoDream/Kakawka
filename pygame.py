import pygame
import math
pygame.init()
screen=pygame.display.set_mode((200,200))
run=True
pos=(100, 100)
clock=pygame.time.Clock()
speed=2
move_map={pygame.K_LEFT:(-1,0),
          pygame.K_RIGHT:(1,0),
          pygame.K_DOWN:(0,1),
          pygame.K_UP:(0,-1)}
while run:
    screen.fill((0,255,0))
    pygame.draw.circle(screen, (255,0,0),map(int,pos),10)
    pygame.display.flip()
    pressed=pygame.key.get_pressed
    movevector=(0,0)
    for i in (move_map[key] for key in move_map if pressed[key]):
        movevector= map(sum, zip(move_vector, i))
    if sum(map(abs,movevector))==2:
        movevector=[p/1.4142 for p in movevector]
    movevector=[speed*p for p in movevector]
    pos=map(sim,zip(pos,movevector))
    for i in pygame.event.get():
        if e.type==pygame.QUIT: run=false
    clock.tick(60) 
    
