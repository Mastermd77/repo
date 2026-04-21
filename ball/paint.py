import pygame, sys, math

W, H = 900, 650
TOP = 60
PANEL = 160
RIGHT = W - PANEL

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (180,180,180)
DARK = (80,80,80)
LIGHT = (220,220,220)
BLUE = (100,180,255)

PALETTE = [
(0,0,0),(255,255,255),(200,0,0),(255,100,0),
(255,215,0),(0,180,0),(0,120,200),(100,0,200),
(255,0,180),(0,200,200),(139,69,19),(150,150,150),
(255,165,80),(80,200,120),(100,149,237),(220,160,220)
]

TOOLS = ["pen","line","rect","circle","eraser","fill"]
SIZES = [2,5,10,20]

def fill(surface, pos, color):
    target = surface.get_at(pos)[:3]
    if target == color: return
    stack = [pos]
    w,h = surface.get_size()
    used = set()
    while stack:
        x,y = stack.pop()
        if (x,y) in used: continue
        if x<0 or y<0 or x>=w or y>=h: continue
        if surface.get_at((x,y))[:3] != target: continue
        surface.set_at((x,y), color)
        used.add((x,y))
        stack += [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

class Btn:
    def __init__(self, r, t):
        self.r = pygame.Rect(r)
        self.t = t
        self.f = pygame.font.SysFont("Arial",14,True)

    def draw(self, s, a=False):
        pygame.draw.rect(s, BLUE if a else DARK, self.r, border_radius=5)
        pygame.draw.rect(s, LIGHT, self.r, 1, border_radius=5)
        txt = self.f.render(self.t,1,WHITE)
        s.blit(txt, txt.get_rect(center=self.r.center))

    def hit(self,p): return self.r.collidepoint(p)

class App:
    def __init__(self):
        pygame.init()
        self.s = pygame.display.set_mode((W,H))
        self.c = pygame.time.Clock()

        self.canvas = pygame.Surface((RIGHT, H-TOP))
        self.canvas.fill(WHITE)
        self.prev = pygame.Surface(self.canvas.get_size(), pygame.SRCALPHA)

        self.tool = "pen"
        self.color = BLACK
        self.size = 5
        self.draw = False
        self.start = None
        self.last = None

        self.tools = {}
        x = 10
        for t in TOOLS:
            self.tools[t] = Btn((x, 12, 95, 32), t)
            x += 105   

        self.clear = Btn((RIGHT-100,12,90,32),"clear")

        self.colors = []
        x = RIGHT+10
        y = 80
        for i,c in enumerate(PALETTE):
            cx = x + (i%4)*36
            cy = y + (i//4)*36
            self.colors.append((pygame.Rect(cx,cy,30,30),c))

        self.sizes = []
        y += (len(PALETTE)//4)*36 + 20
        for s in SIZES:
            b = Btn((x,y,140,28), str(s))
            self.sizes.append((b,s))
            y += 34

    def cp(self,p): return (p[0], p[1]-TOP)

    def inside(self,p):
        return 0<=p[0]<RIGHT and TOP<=p[1]<H

    def preview(self,p):
        self.prev.fill((0,0,0,0))
        if not self.start: return
        sx,sy = self.start
        ex,ey = self.cp(p)

        if self.tool=="line":
            pygame.draw.line(self.prev, (*self.color,200),(sx,sy),(ex,ey),self.size)
        elif self.tool=="rect":
            r = pygame.Rect(min(sx,ex),min(sy,ey),abs(ex-sx),abs(ey-sy))
            pygame.draw.rect(self.prev, (*self.color,200),r,self.size)
        elif self.tool=="circle":
            r = int(math.hypot(ex-sx, ey-sy))
            if r>0:
                pygame.draw.circle(self.prev, (*self.color,200),(sx,sy),r,self.size)

    def commit(self,p):
        if not self.start: return
        sx,sy = self.start
        ex,ey = self.cp(p)

        if self.tool=="line":
            pygame.draw.line(self.canvas,self.color,(sx,sy),(ex,ey),self.size)
        elif self.tool=="rect":
            r = pygame.Rect(min(sx,ex),min(sy,ey),abs(ex-sx),abs(ey-sy))
            pygame.draw.rect(self.canvas,self.color,r,self.size)
        elif self.tool=="circle":
            r = int(math.hypot(ex-sx, ey-sy))
            if r>0:
                pygame.draw.circle(self.canvas,self.color,(sx,sy),r,self.size)

        self.prev.fill((0,0,0,0))
        self.start=None

    def ui(self):
        pygame.draw.rect(self.s,(40,40,50),(0,0,W,TOP))
        pygame.draw.rect(self.s,(50,50,60),(RIGHT,0,PANEL,H))

        for t,b in self.tools.items():
            b.draw(self.s, t==self.tool)

        self.clear.draw(self.s)

        for r,c in self.colors:
            pygame.draw.rect(self.s,c,r)
            pygame.draw.rect(self.s, BLUE if c==self.color else DARK, r,2)

        for b,s in self.sizes:
            b.draw(self.s, s==self.size)

    def run(self):
        while True:
            self.c.tick(60)

            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit(); sys.exit()

                if e.type==pygame.MOUSEBUTTONDOWN:
                    p = e.pos

                    for t,b in self.tools.items():
                        if b.hit(p): self.tool=t

                    if self.clear.hit(p):
                        self.canvas.fill(WHITE)

                    for r,c in self.colors:
                        if r.collidepoint(p): self.color=c

                    for b,s in self.sizes:
                        if b.hit(p): self.size=s

                    if self.inside(p):
                        self.draw=True
                        self.start=self.cp(p)
                        self.last=self.start
                        if self.tool=="fill":
                            fill(self.canvas,self.start,self.color)
                            self.draw=False

                if e.type==pygame.MOUSEBUTTONUP:
                    if self.draw:
                        if self.tool in ["line","rect","circle"]:
                            self.commit(e.pos)
                        self.draw=False
                        self.last=None

                if e.type==pygame.MOUSEMOTION:
                    if self.draw and self.inside(e.pos):
                        p = self.cp(e.pos)

                        if self.tool=="pen":
                            if self.last:
                                pygame.draw.line(self.canvas,self.color,self.last,p,self.size)
                            self.last=p

                        elif self.tool=="eraser":
                            pygame.draw.circle(self.canvas,WHITE,p,self.size*2)

                        elif self.tool in ["line","rect","circle"]:
                            self.preview(e.pos)

            self.s.blit(self.canvas,(0,TOP))
            self.s.blit(self.prev,(0,TOP))
            self.ui()

            if self.tool=="eraser":
                mx,my = pygame.mouse.get_pos()
                if self.inside((mx,my)):
                    pygame.draw.circle(self.s,DARK,(mx,my),self.size*2,2)

            pygame.display.flip()

if __name__=="__main__":
    App().run()