import pygame


pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)

# The original
hero_img = pygame.Surface((48, 48), pygame.SRCALPHA)

pygame.draw.circle(hero_img, (30, 90, 170), (24, 24), 20)
# ---Solution 1---
# You could create a copy of the original image and
# then draw the rect onto it.
hero_img_with_border = hero_img.copy()
# Draw the red border. Pass an int as the last argument (width)
# to draw a non-filled rect. For 2 pixel linewidth the rect has
# to be one pixel smaller.

pygame.draw.rect(hero_img_with_border, red, (0, 0, 47, 47), 2)


class Hero(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()
        self.image = hero_img
        self.rect = self.image.get_rect(center=position)
        self.speed = 3

    def draw(self, screen):
        # ---Solution 2---
        # Just draw the non-filled rect here.
        pygame.draw.rect(screen, red, self.rect, 2)

    def right(self):
        self.rect.x += self.speed
    def left(self):
        self.rect.x -= self.speed
    def up(self):
        self.rect.y -= self.speed
    def down(self):
        self.rect.y += self.speed


screen = pygame.display.set_mode((640, 480))

sprites_list = pygame.sprite.Group()
# You can pass the coords and change the rect in the __init__ method.
hero = Hero((200, 300))
sprites_list.add(hero)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
       hero.left()
    if key[pygame.K_RIGHT]:
       hero.right()
    if key[pygame.K_UP]:
       hero.up()
    if key[pygame.K_DOWN]:
       hero.down()

    sprites_list.update()

    screen.fill(white)
    sprites_list.draw(screen)
    
    # If you use solution 1, you don't need the draw method, since
    # sprites_list.draw blits the image already.
    hero.draw(screen)
    screen.blit(hero_img_with_border, (100, 100))

    pygame.display.flip()
    clock.tick(60)