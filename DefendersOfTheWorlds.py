import pygame as pg
from SpaceShip import SpaceShip
import Controls
from pygame.sprite import Group
from ino import Ino
from Stats import Stats
import sys
from Scores import Scores
import time

def run():
    pg.init()
    screen = pg.display.set_mode((1920, 1080))
    pg.display.set_caption("Defenders of the worlds")
    BgColor = pg.image.load("images\BG.png")
    spaceship = SpaceShip(screen)
    bullets = Group()
    bulletsenemy = Group()
    ino = Ino(screen)
    inos = Group()
    Controls.CreateArmy(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    start_ticks = pg.time.get_ticks()

    while True:
        seconds = (pg.time.get_ticks() - start_ticks) / 1000
        if seconds > 99:
            time.sleep(10)
            sys.exit()
        spaceship.UpdateSpaceShip()
        spaceship.Controls(screen, spaceship, bullets, ino, inos, bulletsenemy)
        Controls.Update(BgColor, screen, spaceship,stats, sc, inos, bullets, bulletsenemy)
        Controls.UpdateBullet(screen,stats, sc, inos, bullets)
        Controls.UpdateBulletEnemeis(screen, spaceship, bulletsenemy)
        Controls.UpdateInos(stats, sc, screen, spaceship, inos, bullets, bulletsenemy)


run()