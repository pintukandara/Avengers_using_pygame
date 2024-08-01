import pygame 
import random
import math
from pygame import mixer
#initialize the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((800,700))
#creating icon
pygame.display.set_caption("Avengers")
icon = pygame.image.load("book.png")
pygame.display.set_icon(icon)
#player
playerimage = pygame.image.load("comic-book.png")
playerX = 400
playerY = 600
playerX_chage = 0
#creating backgroud
background =  pygame.image.load('back.jpg')
#creating enemy
enemyimage = []
enemy = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemy = 6
for i in range(number_of_enemy):
  enemyimage.append(pygame.image.load("age.png"))
  enemyX.append(random.randint(0,750))
  enemyY.append(random.randint(50,200))
  enemyX_change.append(0.6)
  enemyY_change.append(25)
#Bullet
# ready : bullet is not going show you
bulletimage = pygame.image.load("electric-fire.png")
bulletX = 0
bulletY = 600
bulletX_change = 0
bulletY_change = 1 
bullet_state = "ready"
score_value = 0
font = pygame.font.Font('SuperMario256.ttf',32)
textX = 10
textY = 8
#game over
gameover = pygame.font.Font('SuperMario256.ttf',64)

#backgorund music 
mixer.music.load("thor.wav")
mixer.music.play(-1)
def show_score(x,y):
    score = font.render("Score:" + str(score_value),True,(192,192,192))
    screen.blit(score,(x,y))
def game_over_text():
    game_over = gameover.render("Game Over",True,(192,192,192))
    screen.blit(game_over,(250,350))


def player(x,y):
    screen.blit(playerimage,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimage[i],(enemyX[i],enemyY[i]))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimage,(x ,y))
# defining collision
def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2) )+ (math.pow(enemyY- bulletY,2)))
    if distance <= 40:
        return True
    else:
        return False



#game loop 
running =True
while running :
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
  
    # print(playerX)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            

            if event.key == pygame.K_LEFT:
                playerX_chage = -0.3

                

            if event.key == pygame.K_RIGHT:

                playerX_chage = 0.3 
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("hammer.wav")
                    bullet_sound.play()
                bulletX = playerX
                fire_bullet(bulletX,bulletY)
                # print("right key")
        if event.type == pygame.KEYUP:

            if  event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerX_chage = 0
            #   print("key rel
        
    playerX += playerX_chage 
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        
        playerX = 736
    for i in range(number_of_enemy):
        #game over
        if enemyY[i] >= 550:
            for j in range(number_of_enemy):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.6
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.6
            enemyY[i] += enemyY_change[i]
        collision = iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 600
            bullet_state = "ready"
            score_value += 10
            
            enemyX[i] = random.randint(50,750)
            enemyY[i] = random.randint(50,200)
        enemy(enemyX[i],enemyY[i],i)
    # bullet movement#
    if bulletY <= 0:
        bulletY = 600
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change

    
    #calling iscollision 
   
    player(playerX,playerY)
    show_score(textX,textY)
    # backgroundima(0,0)
    pygame.display.update()
    pass
  
