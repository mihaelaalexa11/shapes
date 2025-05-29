import pygame 

pygame.init()


shapes=[]
Window_width=Window_height=0

with open('shapes.txt','r') as f:

    linia1=f.readline().strip().split(',')

    if linia1[0]=='Window':
        w=int(linia1[1])
        h=int(linia1[2])
        Window_width = w
        Window_height = h
        screen = pygame.display.set_mode((Window_width, Window_height))

clock = pygame.time.Clock()
FPS = 60
BG = (205, 150, 190)

class Rectangle:

    def __init__(self, px, py, w, h, vx, vy, color):
        
        self.rect= pygame.Rect(px, py, w, h)
        self.vx=vx
        self.vy=vy
        self.color=color

    def update(self):

        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.x <= 0 or self.rect.x >= Window_width:
            self.vx= -self.vx
        if self.rect.y <= 0 or self.rect.y >= Window_height:
            self.vy= -self.vy
        if self.rect.top < 0 or self.rect.bottom > Window_height:
            self.vy= -self.vy
        if self.rect.right < 0 or self.rect.right > Window_width:
            self.vx= -self.vx

    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Circle: 

    def __init__(self, px, py, r, vx, vy, color):
        self.x=px
        self.y=py
        self.r=r
        self.vx=vx
        self.vy=vy
        self.color=color
    
    def update(self):
        self.x += self.vx
        self.y += self.vy

        if self.x-self.r < 0 or self.x+self.r > Window_width:
            self.vx= -self.vx
        if self.y-self.r < 0 or self.y+self.r > Window_height:
            self.vy= -self.vy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)




def citire(shapes):
    with open('shapes.txt','r') as f:
        for line in f:
            parts=line.strip().split(',')
            forma=parts[0]

            if forma=='Rectangle':
                px=int(parts[1])
                py=int(parts[2])
                w=int(parts[3])
                h=int(parts[4])
                vx=int(parts[5])
                vy=int(parts[6])
                color=(int(parts[7]), int(parts[8]), int(parts[9]))
                shapes.append(Rectangle(px, py, w, h, vx, vy, color))

            elif forma=='Circle':
                px=int(parts[1])
                py=int(parts[2])
                r=int(parts[3])
                vx=int(parts[4])
                vy=int(parts[5])
                color=( int(parts[6]), int(parts[7]), int(parts[8]))
                shapes.append(Circle(px, py, r, vx, vy, color))

citire(shapes)

run=True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(BG)

    for shape in shapes:
        shape.update()
        shape.draw(screen)

    pygame.display.update()

pygame.quit()



        