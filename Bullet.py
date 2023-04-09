import pygame as pg
import math

class Bullet(pg.sprite.Sprite):
    def __init__(self, screen, spaceship):
        """Create a bullet at the position of the spaceship"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pg.Rect(0, 0, 5, 5)
        self.color = 148, 0, 211
        self.speed = 10.5
        self.rect.centerx = spaceship.rect.centerx
        self.rect.center = spaceship.rect.center
        self.y = float(self.rect.y)
        mouse_x, mouse_y = pg.mouse.get_pos()
        distance_x = mouse_x - spaceship.rect.centerx
        distance_y = mouse_y - spaceship.rect.centery
        angle = math.atan2(distance_y, distance_x)
        self.speed_x = self.speed * math.cos(angle)
        self.speed_y = self.speed * math.sin(angle)

    def update(self):
        """Move the bullet"""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def DrawBullet(self):
        """Draw a bullet on the screen"""
        pg.draw.rect(self.screen, self.color, self.rect)