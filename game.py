import pygame
import random
import math
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1000, 800))

# Background images
backgroundimg = pygame.image.load("C:/Users/merry/Space-game-main/Space-game-main/Space game/background.jpg").convert()
backgroundimg2 = pygame.image.load("C:/Users/merry/Space-game-main/Space-game-main/Space game/background2.jpg").convert()
backgroundimg3 = pygame.image.load("C:/Users/merry/Space-game-main/Space-game-main/Space game/background.jpg").convert()

# Background music
mixer.music.load('C:/Users/merry/Space-game-main/Space-game-main/Space game/music.mp3')
mixer.music.set_volume(0.4)
mixer.music.play(-1)

# Game title and icon
pygame.display.set_caption("SPACEventure")
icon = pygame.image.load('C:/Users/merry/Space-game-main/Space-game-main/Space game/launch.png').convert_alpha()
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('C:/Users/merry/Space-game-main/Space-game-main/Space game/space-invaders.png').convert_alpha()
playerx = 468
playery = 700
pcx, pcy = 0, 0

# Enemy
enemy1 = pygame.image.load('C:/Users/merry/Space-game-main/Space-game-main/Space game/alien (1).png').convert_alpha()
enemy2 = pygame.image.load('C:/Users/merry/Space-game-main/Space-game-main/Space game/alien.png').convert_alpha()
enemy3 = pygame.image.load('C:/Users/merry/Space-game-main/Space-game-main/Space game/space-ship.png').convert_alpha()
enemyx = random.randint(64, 936)
enemyy = 64
ey = 0.4

# Bullets
bulletp = pygame.image.load('C:/Users/merry/Space-game-main/Space-game-main/Space game/bullet (1).png').convert_alpha()
bullete = pygame.image.load('C:/Users/merry/Space-game-main/Space-game-main/Space game/bullet (3).png').convert_alpha()
bulletpp = pygame.image.load('C:/Users/merry/Space-game-main/Space-game-main/Space game/bullet (2).png').convert_alpha()

bulletx, bullety = 0, 690
bullx, bully = 0, 1.6
bulletstate = "ready"

bulletppx, bulletppy = 0, 690
bullppx, bullppy = 0, 1.6
bulletbigstate = "r"

# Score and life
scorevalue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
tx, ty = 10, 10

lifevalue = 3
lifefont = pygame.font.Font('freesansbold.ttf', 32)
lx, ly = 890, 10

over = pygame.font.Font('freesansbold.ttf', 64)

# Level and Boss
level = 1
bossimg = pygame.image.load('C:/Users/merry/Space-game-main/Space-game-main/Space game/alien.png').convert_alpha()
bossx, bossy = 400, 50
boss_hp = 5  # Boss now has 5 lives
boss_speed_x = 0.3
boss_speed_y = 0.3

# Functions
def showscore(x, y):
    score = font.render("Score: " + str(scorevalue), True, (255, 255, 255))
    screen.blit(score, (x, y))

def live(x, y):
    life = lifefont.render("Life: " + str(lifevalue), True, (255, 0, 0))
    screen.blit(life, (x, y))

def gameover():
    overfont = over.render("GAME OVER", True, (255, 255, 255))
    screen.blit(overfont, (300, 350))

def youwin():
    win_text = over.render("YOU WIN!", True, (255, 255, 255))
    screen.blit(win_text, (350, 350))
    pygame.display.update()
    pygame.time.wait(2000)  # Wait for 2 seconds before transitioning or ending the game

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemya(x, y):
    screen.blit(enemy2, (x, y))

def enemy(x, y):
    screen.blit(enemy1, (x, y))

def fire(x, y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletp, (x, y))

def firee(x, y):
    global bulletbigstate
    bulletbigstate = "firee"
    screen.blit(bulletpp, (x, y))

def collision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((enemyx - bulletx)**2 + (enemyy - bullety)**2)
    return distance < 27

def collide(playerx, playery, enemyx, enemyy):
    distance = math.sqrt((enemyx - playerx)**2 + (enemyy - playery)**2)
    return distance < 27

def show_level(x, y):
    level_text = font.render("Level: " + str(level), True, (255, 255, 255))
    screen.blit(level_text, (x, y + 40))

def boss(x, y):
    # Scale the boss image to make it bigger (e.g., double the size)
    scaled_boss = pygame.transform.scale(bossimg, (150, 150))  # Adjust the size as needed
    screen.blit(scaled_boss, (x, y))

# Game loop
run = True
while run:
    # Level progression based on score
    if scorevalue >= 10 and level == 1:
        level = 2  # Move to level 2 when score reaches 10
    elif scorevalue >= 20 and level == 2:
        level = 3  # Move to level 3 when score reaches 20
    
    # Background for different levels
    if level == 1:
        screen.blit(backgroundimg, (-400, -500))
    elif level == 2:
        screen.blit(backgroundimg2, (0, 0))
    elif level == 3:
        screen.blit(backgroundimg3, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pcx = -0.5
            if event.key == pygame.K_RIGHT:
                pcx = 0.5
            if event.key == pygame.K_UP:
                pcy = -0.5
            if event.key == pygame.K_DOWN:
                pcy = 0.5
            if event.key == pygame.K_SPACE and bulletstate == "ready":
                bulletsound = mixer.Sound('C:/Users/merry/Space-game-main/Space-game-main/Space game/blaster-2-81267.mp3')
                bulletsound.play()
                bulletx, bullety = playerx, playery
                fire(bulletx, bullety)
            if event.key == pygame.K_RCTRL and bulletbigstate == "r":
                bulletsound1 = mixer.Sound('C:/Users/merry/Space-game-main/Space-game-main/Space game/laser-gun-81720.mp3')
                bulletsound1.play()
                bulletppx, bulletppy = playerx, playery
                firee(bulletppx, bulletppy)

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                pcx, pcy = 0, 0

    if lifevalue > 0:
        playerx += pcx
        playery += pcy

        if playerx < 0:
            playerx = 0
        elif playerx > 936:
            playerx = 936

        if playery < 0:
            playery = 0
        elif playery > 736:
            playery = 736

        # Level 1 and 2 enemies
        if level < 3:
            enemyy += ey
            if enemyy >= 864:
                enemyy = -32
                enemyx = random.randint(64, 936)

            if collision(enemyx, enemyy, bulletx, bullety):
                explodesound = mixer.Sound('C:/Users/merry/Space-game-main/Space-game-main/Space game/explosion-6055.mp3')
                explodesound.play()
                bullety = playery
                bulletstate = "ready"
                scorevalue += 1
                enemyx = random.randint(64, 936)
                enemyy = 64

            if collide(playerx, playery, enemyx, enemyy):
                lifevalue -= 1
                enemyx, enemyy = random.randint(64, 936), 64
                playerx, playery = 468, 700

            if bullety <= 0:
                bulletstate = "ready"

            if bulletstate == "fire":
                fire(bulletx, bullety)
                bullety -= bully

            # Rendering all game elements
            player(playerx, playery)
            enemy(enemyx, enemyy)
            showscore(tx, ty)
            live(lx, ly)
            show_level(tx, ty)

        # Boss level
        if level == 3:
            bossx += boss_speed_x
            bossy += boss_speed_y

            if bossx <= 50 or bossx >= 950:
                boss_speed_x *= -1
            if bossy <= 50 or bossy >= 500:
                boss_speed_y *= -1

            if collision(bossx, bossy, bulletx, bullety):
                explodesound = mixer.Sound('C:/Users/merry/Space-game-main/Space-game-main/Space game/explosion-6055.mp3')
                explodesound.play()
                bullety = playery
                bulletstate = "ready"
                scorevalue += 5
                boss_hp -= 1

                if boss_hp <= 0:
                    explodesound.play()
                    scorevalue += 20  # Extra points for defeating the boss
                    level = 4  # Transition to level 4 after defeating the boss
                    youwin()  # Show win message
                    pygame.time.wait(2000)  # Wait for 2 seconds before stopping the game or transitioning

            if collide(playerx, playery, bossx, bossy):
                lifevalue -= 1
                playerx, playery = 468, 700

            if bullety <= 0:
                bulletstate = "ready"

            if bulletstate == "fire":
                fire(bulletx, bullety)
                bullety -= bully

            player(playerx, playery)
            boss(bossx, bossy)  # Render the boss here

            showscore(tx, ty)
            live(lx, ly)
            show_level(tx, ty)

    else:
        gameover()

    pygame.display.update()
