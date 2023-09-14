import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_front = pygame.font.Font('font/Pixeltype.ttf', 50)

'''
Приклад червоного куба
test_surface = pygame.Surface((100,200))
test_surface.fill('Red')
'''

sky_surface = pygame.image.load('graphics/Screenshot_3.jpg')
ground_surface = pygame.image.load('graphics/Screenshot_4.jpg')
test_surface = test_front.render('My game',False, 'Green')

snail_surface = pygame.image.load('graphics/Screenshot_2.jpg')
snail_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(test_surface,(300,50))
    snail_x_pos -= 4
    if snail_x_pos < -100: snail_x_pos = 800
    screen.blit(snail_surface,(snail_x_pos,200))
    
    pygame.display.update()
    clock.tick(60)