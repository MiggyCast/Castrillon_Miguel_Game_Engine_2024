# This file was created by: Miguel
# import libraries and modules
'''
moving enemies
more maps
more powerups
 
'''
import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
import random

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Pac-Man with Coins")
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'c':
                    Coin(self, col, row)
                if tile == 'p':
                    self.player = Player(self, col, row)

        self.score = 0

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BLUE)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
while True:
    g.new()
    g.run()
