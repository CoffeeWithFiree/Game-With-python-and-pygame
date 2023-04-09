import random
import pygame as pg
from pygame.math import Vector2
import sys
from Bullet import Bullet
from BulletEnemy import BulletEnemy
from random import randint
from ino import Ino

class SpaceShip():

    def __init__(self, screen):
        """initialize of SpaceShip"""
        self.screen = screen
        self.image = pg.image.load('images/SpaceShip.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.centerX = float(self.rect.centerx)
        self.centerY = float(self.rect.centery)
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.Orig = self.image
        self.mright = False
        self.mleft = False
        self.mUp = False
        self.mDown = False

    def Output(self):
        """Draw a SpaceShip"""
        self.screen.blit(self.image, self.rect)

    def UpdateSpaceShip(self):
        """Update the position of the spaceship"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.centerX += 5.5
        elif self.mleft and self.rect.left > 0:
            self.centerX -= 5.5
        elif self.mUp and self.rect.top > 0:
            self.centerY -= 5.5
        elif self.mDown and self.rect.bottom < self.screen_rect.bottom:
            self.centerY += 5.5

        self.rect.centerx = self.centerX
        self.rect.centery = self.centerY

    def Controls(self, screen, spaceship, bullets, Ino, inos, bulletsenemy):
        """Rotate and move the spaceship"""
        x, y, w, h = self.rect
        direction = pg.mouse.get_pos() - Vector2(x + w // 2, y + h // 2)
        radius, angle = direction.as_polar()
        self.image = pg.transform.rotate(self.Orig, -angle - 90)
        self.rect = self.image.get_rect(center=self.rect.center)

        for event in pg.event.get():
            flag = False
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()
                    #Right
                if event.key == pg.K_d:
                    self.mright = True
                    #Left
                elif event.key == pg.K_a:
                    self.mleft = True
                    #Up
                elif event.key == pg.K_w:
                    self.mUp = True
                    #Down
                elif event.key == pg.K_s:
                    self.mDown = True
                elif event.key == pg.K_SPACE and flag == False:
                    starttime = pg.time.get_ticks()
                    NewBullet = Bullet(screen, spaceship)
                    bullets.add(NewBullet)
                    flag = True
                elif flag == True and pg.time.get_ticks() - starttime >= 2000:
                    flag = False

            elif event.type == pg.KEYUP:
                    #right
                if event.key == pg.K_d:
                    self.mright = False
                    #left
                elif event.key == pg.K_a:
                    self.mleft = False
                    #Up
                elif event.key == pg.K_w:
                    self.mUp = False
                    #Down
                elif event.key == pg.K_s:
                    self.mDown = False
        k = random.randint(0, 10)
        if k == 1 or k == 2:
            for Ino in inos:
                NewBulletEnemy = BulletEnemy(screen, Ino, spaceship)
                bulletsenemy.add(NewBulletEnemy)

    def CreateGun(self):
        """Draw gun after death"""
        self.centerX = self.screen_rect.centerx
        self.centerY = self.screen_rect.centery
        self.rect.centerx = self.centerX
        self.rect.centery = self.centerY
