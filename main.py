import pygame
import random
import sys
from tkinter import *
from os import path
from pygame import mixer

pygame.init()
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255,255,255)
NEW = (102,255,255)

HighScore = "HighScore.txt"
L2Score = "L2Score.txt"
L3Score = "L3Score.txt"

pygame.display.set_caption('Dodger Game')
levelNo = 1
screen = pygame.display.set_mode((WIDTH, HEIGHT))

startVisible = True
myFont3 = pygame.font.SysFont("Times", 32)
while startVisible:
    screen.fill((0, 0, 0))
    bgimage = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\DodgerHomeNew.png")
    screen.blit(bgimage, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            startVisible = False
    pygame.display.update()


def start():
    with open(HighScore, 'r') as f:
        try:
            hs = int(f.read())
        except:
            hs = 0
    prevHS = hs

    with open(L2Score, 'r') as f:
        try:
            hs2 = int(f.read())
        except:
            hs2 = 0
    L2sc = hs2

    with open(L3Score, 'r') as f:
        try:
            hs3 = int(f.read())
        except:
            hs3 = 0
    L3sc = hs3

    player_size = 50
    player_pos = [WIDTH / 2, HEIGHT - 2 * player_size]

    enemy_size = 50
    enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
    enemy_list = [enemy_pos]  

    SPEED = 10
    game_over = False
    score = 0
    clock = pygame.time.Clock()
    myFont = pygame.font.SysFont("monospace", 35)

    PAUSE_MUSIC = False

    def set_level(SPEED, lno):
        if lno == 1:
            SPEED = 10
        elif lno == 2:
            SPEED = 14
        else:
            SPEED = 17
        return SPEED

    def detect_collision(player_pos, enemy_pos):
        p_x = player_pos[0]
        p_y = player_pos[1]

        e_x = enemy_pos[0]
        e_y = enemy_pos[1]

        if (e_x >= p_x and e_x < (p_x + player_size) or p_x >= e_x and p_x < (e_x + enemy_size)):
            if (e_y >= p_y and e_y < (p_y + player_size) or p_y >= e_y and p_y < (e_y + enemy_size)):
                return True
            return False

    def drop_enemies(enemy_list):  # 2 start
        delay = random.random()
        if len(enemy_list) < 10 and delay < 0.1:
            x_pos = random.randint(0, WIDTH - enemy_size)
            y_pos = 0
            enemy_list.append([x_pos, y_pos])

    def draw_enemies(enemy_list, lno):
        if game_over == True:
            return
        for enemy_pos in enemy_list:
            if lno == 1:
                pygame.draw.rect(screen, BLUE,
                                 (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
                # removed below same line
            elif lno == 2:
                pygame.draw.rect(screen, (72, 217, 214), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
            elif lno == 3:
                pygame.draw.rect(screen, (194, 237, 66), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    def update_enemy_positions(enemy_list, score):
        for idx, enemy_pos in enumerate(enemy_list):
            if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:  # commented same code below
                enemy_pos[1] += SPEED
            else:
                enemy_list.pop(idx)
                score += 1
        return score

    def collision_check(enemy_list, player_pos):
        for enemy_pos in enemy_list:
            if detect_collision(enemy_pos, player_pos):
                mixer.music.stop()
                hitSound = mixer.Sound("C:\\Users\\Priyansi\\Downloads\\Oops.mp3")
                hitSound.play()
                return True
        return False  # 2 end

    def bg_levels(lno):
        if game_over == True:
            return
        if lno == 1:
            i2 = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\level12.jpg")
        elif lno == 2:
            i2 = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\level2.jpg")

        elif lno == 3:
            i2 = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\level31.jpeg")
        screen.blit(i2, (0, 0))

    levelScreen = True

    myFont4 = pygame.font.SysFont("Times", 18)
    while levelScreen:
        screen.fill((0, 0, 0))
        des = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\Description.png")
        screen.blit(des, (WIDTH - 790, HEIGHT - 600))
        start1 = myFont4.render("TO START :", 1, YELLOW)
        screen.blit(start1, (WIDTH - 175, HEIGHT - 260))
        start1 = myFont4.render("Press 1 to play level 1", 1, YELLOW)
        screen.blit(start1, (WIDTH - 200, HEIGHT - 240))
        start2 = myFont4.render("Press 2 to play level 2", 1, YELLOW)
        screen.blit(start2, (WIDTH - 200, HEIGHT - 220))
        start3 = myFont4.render("Press 3 to play level 3", 1, YELLOW)
        screen.blit(start3, (WIDTH - 200, HEIGHT - 200))
        l1 = myFont4.render("How To Dodge?", 1, RED)
        l2 = myFont4.render("To move player : 'Left Arrow Key to move left' and 'Right Arrow Key to move Right'", 1, YELLOW)
        l3 = myFont4.render("Music On/Off : Spacebar", 1, YELLOW)
        screen.blit(l1, (WIDTH - 450, HEIGHT - 110))
        screen.blit(l2, (WIDTH - 660, HEIGHT - 70))
        screen.blit(l3, (WIDTH - 450, HEIGHT - 40))

        i1 = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\a1.png")
        screen.blit(i1, (WIDTH - 600, HEIGHT - 350))
        # i2 = pygame.image.load("a1.png")
        # screen.blit(i2, (WIDTH-370, HEIGHT-450))

        ol1 = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\UnlockGreen.jpeg")
        screen.blit(ol1, (WIDTH - 660, HEIGHT - 240))

        if prevHS < 50:
            ol2 = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\LockRed.jpeg")
        else:
            i2 = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\a1.png")
            screen.blit(i2, (WIDTH - 370, HEIGHT - 450))
            ol2 = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\UnlockGreen.jpeg")
        screen.blit(ol2, (WIDTH - 450, HEIGHT - 380))

        if L2sc < 80:
            ol3 = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\LockRed.jpeg")
        else:
            ol3 = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\UnlockGreen.jpeg")
        screen.blit(ol3, (WIDTH - 230, HEIGHT - 460))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1:
                    # print("Level 1 started")
                    levelNo = 1
                    levelScreen = False
                elif event.key == pygame.K_KP2:
                    if prevHS > 50:
                        levelNo = 2
                        levelScreen = False
                elif event.key == pygame.K_KP3:
                    if L2sc > 80:
                        levelNo = 3
                        levelScreen = False
        pygame.display.update()

    mixer.music.load("C:\\Users\\Priyansi\\Downloads\\keysOfMoonMp3Cut.mp3")
    mixer.music.play(-1)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                x = player_pos[0]
                y = player_pos[1]

                if event.key == pygame.K_LEFT:
                    x -= player_size

                elif event.key == pygame.K_RIGHT:
                    x += player_size

                elif event.key == pygame.K_SPACE:
                    if PAUSE_MUSIC == False:
                        mixer.music.pause()
                        PAUSE_MUSIC = True

                    else:
                        mixer.music.unpause()
                        PAUSE_MUSIC = False
                player_pos = [x, y]

        screen.fill((0, 0, 0))

        drop_enemies(enemy_list)
        score = update_enemy_positions(enemy_list, score)
        SPEED = set_level(SPEED, levelNo)
        bg_levels(levelNo)


        text = "Score : " + str(score)
        label = myFont.render(text, 1, YELLOW)
        screen.blit(label, (WIDTH - 250, HEIGHT - 40))

        if PAUSE_MUSIC == False:
            # nFont = pygame.font.SysFont("monospace", 20)
            # mutedTxt = nFont.render("Music muted ..", 1, (255,255,255))
            # screen.blit(mutedTxt, (WIDTH-200, HEIGHT-575))
            image = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\SoundOn2.png")
            screen.blit(image, (WIDTH - 70, HEIGHT - 575))

        if PAUSE_MUSIC == True:
            image = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\SoundOff2.png")
            screen.blit(image, (WIDTH - 70, HEIGHT - 575))

        if levelNo == 1:
            if score > hs:
                hs = score
                with open(HighScore, 'w') as f:
                    f.write(str(hs))

        if levelNo == 2:
            if score > hs2:
                hs2 = score
                with open(L2Score, 'w') as f:
                    f.write(str(hs2))

        if levelNo == 3:
            if score > hs3:
                hs3 = score
                with open(L3Score, 'w') as f:
                    f.write(str(hs3))

        if collision_check(enemy_list, player_pos):
            game_over = True
            break

        draw_enemies(enemy_list, levelNo)

        pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

        clock.tick(30)

        pygame.display.update()

    myFont2 = pygame.font.SysFont("Times", 62)
    endVisible = True
    while endVisible:
        screen.fill((0, 0, 0))
        i2 = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\go.jpg")
        screen.blit(i2, (0, 0))
        l1 = myFont2.render("Level " + str(levelNo), 1, NEW)
        screen.blit(l1, (WIDTH - 630, HEIGHT - 470))
        label2 = myFont2.render("Game Over !!", 1, WHITE)
        screen.blit(label2, (WIDTH - 550, HEIGHT - 570))
        text = "Score : " + str(score)
        label = myFont2.render(text, 1, NEW)
        screen.blit(label, (WIDTH - 630, HEIGHT - 390))
        if levelNo == 1:
            if hs > prevHS:
                scoreTxt = "New High Score"
                # image = pygame.image.load("C:\\Users\\Priyansi\\Downloads\\celebration2.png")
                # screen.blit(image, (0, 300))
            else:
                scoreTxt = "High Score : " + str(hs)

        elif levelNo == 2:
            if hs2 > L2sc:
                scoreTxt = "New High Score"
            else:
                scoreTxt = "High Score : " + str(hs2)

        else:
            if hs3 > L3sc:
                scoreTxt = "New High Score"
            else:
                scoreTxt = "High Score : " + str(hs3)
        label3 = myFont2.render(scoreTxt, 1, NEW)
        screen.blit(label3, (WIDTH - 630, HEIGHT - 290))
        label4 = myFont2.render("Play Again? Press : y or n", 1, WHITE)
        screen.blit(label4, (WIDTH - 720, HEIGHT - 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    levelScreen = True
                    start()
                elif event.key == pygame.K_n:
                    sys.exit()
        pygame.display.update()


start()
