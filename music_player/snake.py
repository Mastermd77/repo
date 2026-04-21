import pygame, random, sys

CELL = 20
COLS, ROWS = 30, 28
W, H = CELL * COLS, CELL * ROWS

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (50,200,50)
DARK_GREEN = (30,140,30)
RED = (220,40,40)
YELLOW = (255,215,0)

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

class Game:
    def __init__(self):
        pygame.init()
        self.s = pygame.display.set_mode((W,H))
        self.c = pygame.time.Clock()
        self.f = pygame.font.SysFont("consolas", 22, True)
        self.reset()

    def reset(self):
        self.snake = [(COLS//2, ROWS//2),(COLS//2-1, ROWS//2)]
        self.dir = RIGHT
        self.next = RIGHT
        self.food = self.spawn()
        self.score = 0
        self.level = 1
        self.eaten = 0
        self.fps = 8
        self.over = False
        self.pause = False

    def spawn(self):
        while True:
            p = (random.randint(1,COLS-2), random.randint(1,ROWS-2))
            if p not in self.snake:
                return p

    def update(self):
        self.dir = self.next
        x,y = self.snake[0]
        dx,dy = self.dir
        head = (x+dx,y+dy)

        if head in self.snake or x+dx<=0 or x+dx>=COLS-1 or y+dy<=0 or y+dy>=ROWS-1:
            self.over = True
            return

        self.snake.insert(0, head)

        if head == self.food:
            self.score += 10 + (self.level-1)*5
            self.eaten += 1
            self.food = self.spawn()
            if self.eaten == 3:
                self.level += 1
                self.eaten = 0
                self.fps += 2
        else:
            self.snake.pop()

    def draw(self):
        self.s.fill((20,20,20))

        for i,(x,y) in enumerate(self.snake):
            col = DARK_GREEN if i==0 else GREEN
            pygame.draw.rect(self.s, col, (x*CELL,y*CELL,CELL,CELL))

        fx,fy = self.food
        pygame.draw.circle(self.s, RED, (fx*CELL+10,fy*CELL+10),8)

        txt = self.f.render(f"{self.score} | lvl {self.level}", True, WHITE)
        self.s.blit(txt,(10,5))

        if self.pause:
            t = self.f.render("PAUSE", True, YELLOW)
            self.s.blit(t,(W//2-40,H//2))

        if self.over:
            t = self.f.render("GAME OVER R", True, RED)
            self.s.blit(t,(W//2-100,H//2))

    def run(self):
        while True:
            self.c.tick(self.fps)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); sys.exit()

                if e.type == pygame.KEYDOWN:
                    if self.over:
                        if e.key == pygame.K_r: self.reset()
                    else:
                        if e.key == pygame.K_UP and self.dir!=DOWN: self.next=UP
                        if e.key == pygame.K_DOWN and self.dir!=UP: self.next=DOWN
                        if e.key == pygame.K_LEFT and self.dir!=RIGHT: self.next=LEFT
                        if e.key == pygame.K_RIGHT and self.dir!=LEFT: self.next=RIGHT
                        if e.key == pygame.K_p: self.pause = not self.pause

            if not self.over and not self.pause:
                self.update()

            self.draw()
            pygame.display.flip()

if __name__ == "__main__":
    Game().run()