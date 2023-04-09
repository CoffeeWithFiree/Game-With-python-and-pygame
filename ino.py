import pygame as pg
from random import randrange
from pygame.locals import *
import time
from pygame.math import Vector2

class Ino(pg.sprite.Sprite):
    """Class enemy alone"""

    def __init__(self, screen):
        """initialize and set the initial position"""
        super(Ino, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pg.image.load('Images/SpaceShipEnemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.Orig = self.image

    def Draw(self):
        """Output the Enemy on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self, spaceship):
        """Move the aliens"""
        x, y, w, h = self.rect
        direction = (spaceship.rect.centerx, spaceship.rect.centery) - Vector2(x + w // 2, y + h // 2)
        radius, angle = direction.as_polar()
        self.image = pg.transform.rotate(self.Orig, -angle - 90)
        self.rect = self.image.get_rect(center=self.rect.center)
        SpeedX = float(randrange(-100, 101, 50) + 0.5)
        SpeedY = float(randrange(-100, 101, 50) + 0.5)
        clock = pg.time.Clock()
        dt = clock.tick(60)
        k = 5
        if SpeedX == 50.5 and SpeedY == 0.5 and self.rect.right < self.screen_rect.right:
            for i in range(k):
                self.y += 0
                self.x += SpeedX / k
                self.rect.y = self.y
                self.rect.x = self.x
        elif SpeedX == 50.5 and SpeedY == 50.5 and self.rect.right < self.screen_rect.right and self.rect.bottom < self.screen_rect.bottom:
            for i in range(k):
                self.y += SpeedY / k
                self.x += SpeedX / k
                self.rect.y = self.y
                self.rect.x = self.x
        elif SpeedX == 50.5 and SpeedY == -49.5 and self.rect.right < self.screen_rect.right and self.rect.top > 0:
            for i in range(k):
                self.y += SpeedY / k
                self.x += SpeedX / k
                self.rect.y = self.y
                self.rect.x = self.x
        elif SpeedX == 0.5 and SpeedY == 50.5 and self.rect.bottom < self.screen_rect.bottom:
            for i in range(k):
                self.y += SpeedY / k
                self.x += 0
                self.rect.y = self.y
                self.rect.x = self.x
        elif SpeedX == 0.5 and SpeedY == -49.5 and self.rect.top > 0:
            for i in range(k):
                self.y += SpeedY / k
                self.x += 0
                self.rect.y = self.y
                self.rect.x = self.x
        elif SpeedX == -49.5 and SpeedY == 0.5 and self.rect.left > 0:
            for i in range(k):
                self.y += 0
                self.x += SpeedX / k
                self.rect.y = self.y
                self.rect.x = self.x
        elif SpeedX == -49.5 and SpeedY == 50.5 and self.rect.left > 0 and self.rect.bottom < self.screen_rect.bottom:
            for i in range(k):
                self.y += SpeedY / k
                self.x += SpeedX / k
                self.rect.y = self.y
                self.rect.x = self.x
        elif SpeedX == -49.5 and SpeedY == -49.5 and self.rect.left > 0 and self.rect.top > 0:
            for i in range(k):
                self.y += SpeedY / k
                self.x += SpeedX / k
                self.rect.y = self.y
                self.rect.x = self.x
        else:
            for i in range(k):
                self.y += 0
                self.x += 0
                self.rect.y = self.y
                self.rect.x = self.x
        self.TruePlaceY = self.rect.y
        self.TruePlaceX = self.rect.x
