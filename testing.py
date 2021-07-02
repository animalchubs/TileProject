import pygame as pg
from pygame.math import Vector2
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

class Entity(pg.sprite.Sprite):

    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pg.Surface((30, 30))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)

    def update(self):
        # Get a vector that points from the position to the target.
        heading = pg.mouse.get_pos() - self.pos
        self.pos += heading * 0.1  # Scale the vector to the desired length.
        self.rect.center = self.pos


def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    entity = Entity((100, 300), all_sprites)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.MOUSEBUTTONDOWN:
                all_sprites.update()


        screen.fill((30, 30, 30))
        all_sprites.draw(screen)

        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()