#this file was created by Miguel Castrillon

import pygame as pg
from settings import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP]:
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN]:
            self.vel.y = PLAYER_SPEED

    def collide_with_coins(self):
        hits = pg.sprite.spritecollide(self, self.game.coins, True)
        for hit in hits:
            self.game.score += 1

    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.topleft = self.pos
        self.collide_with_coins()


class Coin(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.coins
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILESIZE
        self.rect.topleft = self.pos


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILESIZE
        self.rect.topleft = self.pos
