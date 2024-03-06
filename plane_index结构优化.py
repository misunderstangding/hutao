import pygame
from pygame.locals import *
import random
import time

class Plane(object):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.bullet_list = []
        self.image = pygame.image

    def display(self):
        del_bullet = []
        for a in self.bullet_list:
            if a.judge():
                del_bullet.append(a)
        for i in del_bullet:
            self.bullet_list.remove(i)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def shoot_bullet(self):
        new_bullet = Bullet(self.x, self.y, self.screen)
        self.bullet_list.append(new_bullet)


class HeroPlane(Plane):
    def super(self):
        self.image = pygame.image.load('./resource/我方飞机.jpg')

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

class Bullet(object):
    def __init__(self, x, y, screen):
        self.screen = screen
        self.image = pygame.image
        self.x = x
        self.y = y

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

def judge(self):
    if self.y > 600 or self.y < 0:
        return True

def key_control():
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                HeroPlane.move_left()
            if event.key == K_d or event.key == K_RIGHT:
                HeroPlane.move_right()
            if event.key == K_SPACE:
                HeroPlane.shoot_bullet()


def main():
    screen = pygame.display.set_mode((400, 600))
    background = pygame.image.load("./resource/背景.jpg")
    pygame.display.set_caption("打飞机游戏")
    pygame.mixer.init()
    pygame.mixer.music.load("./resource/HOYO-MiX,Jonathan Steingard - 野火 Wildfire.mp3")
    pygame.mixer.music.set_volume(0.005)
    pygame.mixer.music.play(-1)
    hero = HeroPlane(180, 550, screen)
    # enemy = EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        hero.display()
        # enemy.display()
        # enemy.move()
        # enemy.shoot_bullet()
        key_control(hero)
        pygame.display.update()
        # time.sleep(0.005)   #休息0.005秒钟
        pygame.time.Clock().tick(1000000)  #控制频率


if __name__ == "__main__":
    main()