import pygame, random, sys

W, H = 400, 600
FPS = 60

ROAD_L, ROAD_R = 80, 320
LANES = [130, 200, 270]

WHITE=(255,255,255)
RED=(200,0,0)
GREEN=(0,200,0)
BLUE=(0,0,200)
YELLOW=(255,215,0)
GRAY=(50,50,50)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40,70), pygame.SRCALPHA)
        pygame.draw.rect(self.image, BLUE, (5,10,30,50), border_radius=6)
        self.rect = self.image.get_rect(center=(LANES[1], H-40))
        self.speed = 6

    def update(self, keys):
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        self.rect.left = max(ROAD_L+5, self.rect.left)
        self.rect.right = min(ROAD_R-5, self.rect.right)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((40,70), pygame.SRCALPHA)
        pygame.draw.rect(self.image, RED, (5,10,30,50), border_radius=6)
        self.rect = self.image.get_rect(center=(random.choice(LANES), -40))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > H: self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((20,20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (10,10), 10)
        self.rect = self.image.get_rect(center=(random.choice(LANES), -20))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > H: self.kill()

class Game:
    def __init__(self):
        pygame.init()
        self.s = pygame.display.set_mode((W,H))
        self.c = pygame.time.Clock()
        self.f = pygame.font.SysFont("arial", 22, True)
        self.reset()

    def reset(self):
        self.player = Player()
        self.all = pygame.sprite.Group(self.player)
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        self.score = 0
        self.coin_count = 0
        self.level = 1
        self.enemy_speed = 5
        self.coin_speed = 4

        self.et = 0
        self.ct = 0
        self.over = False

    def spawn_enemy(self):
        self.et += 1
        if self.et > 60:
            self.et = 0
            e = Enemy(self.enemy_speed)
            self.all.add(e); self.enemies.add(e)

    def spawn_coin(self):
        self.ct += 1
        if self.ct > random.randint(80,150):
            self.ct = 0
            c = Coin(self.coin_speed)
            self.all.add(c); self.coins.add(c)

    def level_up(self):
        lvl = self.score//50 + 1
        if lvl > self.level:
            self.level = lvl
            self.enemy_speed += 0.5
            self.coin_speed += 0.5

    def draw_road(self):
        self.s.fill((34,139,34))
        pygame.draw.rect(self.s, GRAY, (ROAD_L,0,ROAD_R-ROAD_L,H))
        for y in range(0,H,40):
            col = RED if (y//40)%2==0 else WHITE
            pygame.draw.rect(self.s, col, (ROAD_L-10,y,10,40))
            pygame.draw.rect(self.s, col, (ROAD_R,y,10,40))

    def draw_ui(self):
        t = self.f.render(f"{self.score} | lvl {self.level}", True, WHITE)
        self.s.blit(t,(90,10))
        c = self.f.render(f"x {self.coin_count}", True, YELLOW)
        self.s.blit(c,(250,10))

    def run(self):
        while True:
            self.c.tick(FPS)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if e.type == pygame.KEYDOWN and self.over:
                    if e.key == pygame.K_r: self.reset()

            if not self.over:
                keys = pygame.key.get_pressed()
                self.player.update(keys)

                self.spawn_enemy()
                self.spawn_coin()

                self.enemies.update()
                self.coins.update()

                if pygame.sprite.spritecollideany(self.player, self.enemies):
                    self.over = True

                got = pygame.sprite.spritecollide(self.player, self.coins, True)
                for _ in got:
                    self.coin_count += 1
                    self.score += 5

                self.score += 1
                self.level_up()

            self.draw_road()
            self.all.draw(self.s)
            self.draw_ui()

            if self.over:
                t = self.f.render("GAME OVER R", True, RED)
                self.s.blit(t,(120,300))

            pygame.display.flip()

if __name__ == "__main__":
    Game().run()