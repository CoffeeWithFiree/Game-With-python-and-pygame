import pygame as pg
import math
from random import randrange

class BulletEnemy(pg.sprite.Sprite):
    def __init__(self, screen, ino, spaceship):
        """creating a bullet on enemy positions"""
        super(BulletEnemy, self).__init__()
        self.screen = screen
        self.rect = pg.Rect(0, 0, 5, 5)
        self.color = 148, 0, 211
        self.speed = 10.5
        self.rect.centerx = ino.rect.x
        self.rect.centery = ino.rect.y
        self.y = float(self.rect.y)
        RandX = float(randrange(-500, 501, 100))
        RandY = float(randrange(-500, 501, 100))
        AngleX = spaceship.rect.centerx + RandX
        AngleY = spaceship.rect.centery + RandY
        distance_x = AngleX - ino.rect.x
        distance_y = AngleY - ino.rect.y
        angle = math.atan2(distance_y, distance_x)
        self.speed_x = self.speed * math.cos(angle)
        self.speed_y = self.speed * math.sin(angle)

    def update(self):
        """bullet movement"""
        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y

    def DrawBulletEnemies(self):
        """Draw a bullet on the screen"""
        pg.draw.rect(self.screen, self.color, self.rect)