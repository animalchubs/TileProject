# Help: https://www.thecodingforums.com/threads/ttrpg-movement.973120/
# https://gamedev.stackexchange.com/questions/194414/turn-based-grid-movement-each-click-of-the-clock-you-want-to-move-the-player
import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.speed = MOVEMENT
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.destination = None
        self.x = x
        self.y = y

    def move_toward(self, new_location):
        def do_calculations():
            # Code
            return dx, dy
        new_x, new_y = do_calculations()
        self.move(dx=new_x, dy=new_y)

    # ----
    # you have the current x,y for the player.
    # each click of the clock you want to move the player
    # closer to the end location.
    # get <delta> amount closer to the end corrds. <-- do this each tick of the clock.

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x = dx
            self.y = dy
            self.rect = self.rect.move(dx * TILESIZE, dy * TILESIZE)



    def collide_with_walls(self, dx=0, dy=0, obstacles=None):
        for wall in self.game.walls:
            if wall.x == dx and wall.y == dy:
                return True
        return False



    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Monster(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


