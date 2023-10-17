#Підключення модулів
import pygame
from sys import exit

#Ініціалізація бібліотеки
pygame.init()

#Вказання розміру вікна
screen = pygame.display.set_mode((800,400))

#Вказаня назви вікна
pygame.display.set_caption('Runner')

#Ініцілазація часу
clock = pygame.time.Clock()

#Ініціалазіація тексту
test_front = pygame.font.Font('font/Pixeltype.ttf', 50)
test_surface = test_front.render('My game',False, 'Green')
#Ініціалазіація фонів
sky_surface = pygame.image.load('graphics/Screenshot_3.jpg').convert()
ground_surface = pygame.image.load('graphics/Screenshot_4.jpg').convert()

#Ініціалазіація обєктів 
snail_surf = pygame.image.load('graphics/Screenshot_2_2.jpg').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('graphics/Screenshot_1.jpg').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (100,300))

'''
Приклад червоного куба
test_surface = pygame.Surface((100,200))
test_surface.fill('Red')
'''

#Початок програми
while True:
    #Перевірка евентів
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #Відображення обєектів
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(test_surface,(300,50))
    
    snail_rect.x -= 4
    if snail_rect.right <=0: 
        snail_rect.left = 800
    
    screen.blit(player_surf,player_rect)
    screen.blit(snail_surf,snail_rect)

    #if player_rect.colliderect(snail_rect):
    #    print('collision')

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())

    #Оновлення відображення
    pygame.display.update()
    #Кількість кадрів в секунду
    clock.tick(60)