import pygame


def run():
    pygame.init()

    screen_wth = 700
    screen_ht = 700
    screen = pygame.display.set_mode((screen_wth, screen_ht))
    pygame.display.set_caption("Jump-jump-up-up")

    fon = pygame.image.load("need/fon.png")

    block_size = 35

    # фунуция для разделения экрана игры на полосы
    # def draw_line():
    #     for line in range(0, 20):
    #         pygame.draw.line(screen, (255, 255, 255), (0, line * block_size), (screen_wth, line * block_size))
    #         pygame.draw.line(screen, (255, 255, 255), (line * block_size, 0), (line * block_size, screen_ht))

    class Player():
        def __init__(self, x, y):
            girl_im = pygame.image.load("need/girl1.png")
            self.girl_im = pygame.transform.scale(girl_im, (block_size, block_size * 2))
            self.rect = self.girl_im.get_rect()
            self.rect.x = x
            self.rect.y = y

        def update(self):
            count_x = 0
            count_y = 0

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                count_x -= 10
            if key[pygame.K_RIGHT]:
                count_x += 10
            self.rect.x += count_x
            self.rect.y += count_y

            screen.blit(self.girl_im, self.rect)

    class World_lvl1():
        def __init__(self, my_list):
            self.block_list = []
            dirt_im = pygame.image.load("need/dirty.png")
            green_im = pygame.image.load("need/green.png")
            row_count = 0
            for row in world_map_lvl_one:
                count_col = 0
                for block in row:
                    if block == 1:
                        img = pygame.transform.scale(dirt_im, (block_size, block_size))
                        img_rect = img.get_rect()
                        img_rect.x = count_col * block_size
                        img_rect.y = row_count * block_size
                        get_block = (img, img_rect)
                        self.block_list.append(get_block)
                    if block == 2:
                        img = pygame.transform.scale(green_im, (block_size, block_size))
                        img_rect = img.get_rect()
                        img_rect.x = count_col * block_size
                        img_rect.y = row_count * block_size
                        get_block = (img, img_rect)
                        self.block_list.append(get_block)
                    count_col += 1
                row_count += 1

        def draw(self):
            for block in self.block_list:
                screen.blit(block[0], block[1])

    world_map_lvl_one = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    player = Player(70, screen_ht - 105)
    world = World_lvl1(world_map_lvl_one)
    while pygame.event.wait().type != pygame.QUIT:
        screen.blit(fon, (0, 0))

        world.draw()

        player.update()

        pygame.display.update()

    pygame.quit()
