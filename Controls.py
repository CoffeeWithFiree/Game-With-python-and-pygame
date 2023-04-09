import pygame as pg
import sys
from ino import Ino
import time

def Update(BgColor, screen, spaceship, stats, sc, inos, bullets, bulletsenemy):
    """Update the screen"""
    screen.blit(BgColor, (0, 0))
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.DrawBullet()
    for bulletsenemy in bulletsenemy.sprites():
        bulletsenemy.DrawBulletEnemies()
    spaceship.Output()
    inos.draw(screen)
    pg.display.flip()

def UpdateBullet(screen,stats, sc, inos, bullets):
    """Update the position of the bullets"""
    bullets.update()
    for Bullet in bullets.copy():
        if Bullet.rect.bottom <= 0 or Bullet.rect.bottom >= 1080 or Bullet.rect.centerx <= 0 or Bullet.rect.centerx >= 1920:
            bullets.remove(Bullet)
    collisions = pg.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        stats.GunsLeft += 1
        sc.image_score()
    if len(inos) == 0:
        bullets.empty()
        CreateArmy(screen, inos)

def UpdateBulletEnemeis(screen, spaceship, bulletsenemy):
    bulletsenemy.update()
    for BulletEnemy in bulletsenemy.copy():
        if BulletEnemy.rect.bottom <= 0 or BulletEnemy.rect.bottom >= 1080 or BulletEnemy.rect.centerx <= 0 or BulletEnemy.rect.centerx >= 1920:
            bulletsenemy.remove(BulletEnemy)

def GunKill(stats, sc, screen, spaceship, inos, bullets, bulletsenemy):
    """Collision of a spaceship and an enemy"""
    stats.EnemyLeft += 1
    sc.image_score()
    bullets.empty()
    bulletsenemy.empty()
    spaceship.CreateGun()
    time.sleep(2)

def UpdateInos(stats, sc, screen, spaceship, inos, bullets, bulletsenemy):
    """Update the position of the ememies"""
    inos.update(spaceship)
    if pg.sprite.spritecollideany(spaceship, inos):
        GunKill(stats, sc, screen, spaceship, inos, bullets, bulletsenemy)
        stats.GunsLeft += 1
        sc.image_score()
    if pg.sprite.spritecollideany(spaceship, bulletsenemy):
        GunKill(stats, sc, screen, spaceship, inos, bullets, bulletsenemy)

def CreateArmy(screen, inos):
    """Create an army of enemies"""
    ino = Ino(screen)
    InoWidth = ino.rect.width
    NumberInoX = 1
    InoHeight = ino.rect.height
    NumberInoY = 2

    for RowNumber in range(NumberInoY):
       for InoNumber in range(NumberInoX):
            ino = Ino(screen)
            ino.x = 1
            ino.y = 2
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + 2 * ino.rect.height * RowNumber
            inos.add(ino)
