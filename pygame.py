import pygame
import random 
# إعدادات الشاشة
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("لعبتي الأولى!")

# الألوان
white = (255, 255, 255)

# البدء باللعبة
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    pygame.display.update()

pygame.quit()

#import pygame
#import pygame

#pygame.init()

# إعدادات الشاشة
#screen = pygame.display.set_mode((800, 600))
#pygame.display.set_caption("لعبتي الأولى!")

# الألوان
#white = (255, 255, 255)

# البدء باللعبة
#running = True
#while running:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
      #running = False
    #screen.fill(white)
    #pygame.display.update()

#pygame.quit()
#pygame.init()

#screen = pygame.display.set_mode((800, 600))
#pygame.display.set_caption("كرة متحركة!")

# الألوان
#white = (255, 255, 255)
#ball_color = (0, 0, 255)

# إعدادات الكرة
#ball_pos = [100, 100]
#ball_speed = [2, 2]

#running = True
#while running:
    #for event in pygame.event.get():
        
        #if event.type == pygame.QUIT:
            
            #running = False

    
    #ball_pos[0] += ball_speed[0]
    
    
    #ball_pos[1] += ball_speed[1]



