import pygame

class Ship(pygame.sprite.Sprite):

    def __init__(self, speed, color):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.set_colorkey((12,34,56))
        self.image.fill((12,34,56))
        pygame.draw.circle(self.image, color, (5, 5), 3)
        self.rect = self.image.get_rect()

        self.pos = pygame.Vector2(0, 0)
        self.set_target((0, 0))
        self.speed = speed

    def set_target(self, pos):
        self.target = pygame.Vector2(pos)

    def update(self):
        move = self.target - self.pos
        move_length = move.length()

        if move_length < self.speed:
            self.pos = self.target
        elif move_length != 0:
            move.normalize_ip()
            move = move * self.speed
            self.pos += move

        self.rect.topleft = list(int(v) for v in self.pos)

def main():
    pygame.init()
    quit = False
    screen = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()

    group = pygame.sprite.Group(
        Ship(1.5, pygame.Color('white')),
        Ship(3.0, pygame.Color('orange')),
        Ship(4.5, pygame.Color('dodgerblue')))

    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ship in group.sprites():
                    ship.set_target(pygame.mouse.get_pos())

        group.update()
        screen.fill((20, 20, 20))
        group.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()