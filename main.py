import pygame
from random import randint
pygame.init()
WIDTH, HEIGHT = 600, 300
SNAKE_STEP = 50
FPS = 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
class Snake:
    head = [100, 50]
    body = []
    direc = [0, 50]
    color = (255, 255, 0)
    head_color = (255, 204, 0)
    def addBody(self):
        x, y = 0, 0
        if len(self.body) == 0:
            x = self.head[0] - self.direc[0]
            y = self.head[1] - self.direc[1]
        elif len(self.body) == 1:
            x = self.body[0][0] - (self.head[0] - self.body[0][0])
            y = self.body[0][1] - (self.head[1] - self.body[0][1])
        else:
            x = self.body[-1][0] - (self.body[-2][0] - self.body[-1][0])
            y = self.body[-1][1] - (self.body[-2][1] - self.body[-1][1])
        self.body.append([x, y])
    def draw(self):
        for i in self.body:
            pygame.draw.rect(screen, self.color, [i, [SNAKE_STEP, SNAKE_STEP]])
        pygame.draw.rect(screen, self.head_color, [self.head, [SNAKE_STEP, SNAKE_STEP]])
    def move(self):
        for i in range(len(self.body) - 1, -1, -1):
            if i != 0:
                self.body[i] = self.body[i - 1].copy()
            else:
                self.body[i] = self.head.copy()
        self.head = [(self.head[0] + self.direc[0]) % WIDTH, (self.head[1] + self.direc[1]) % HEIGHT]
    def changeDirec(self, direc):
        if self.direc[0] != direc[0] and self.direc[1] != direc[1]:
            self.direc = direc.copy()
    def checkHead(self, apple):
        if self.head in self.body:
            return False
        if apple.pos == self.head:
            self.addBody()
            apple.spawn()
        return True
snake = Snake()
class Apple:
    pos = [0 , 0]
    color = (255, 0, 0)
    def spawn(self):
        print("a")
        while self.pos in snake.body or self.pos == snake.head:
            self.pos = [randint(0, WIDTH // SNAKE_STEP - 1) * SNAKE_STEP, randint(0, HEIGHT // SNAKE_STEP - 1) * SNAKE_STEP]
            print(self.pos)
        print("b")
    def draw(self):
        pygame.draw.rect(screen, self.color, [self.pos, [SNAKE_STEP, SNAKE_STEP]])
apple = Apple()
running = True
while running and snake.checkHead(apple):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.changeDirec([-50, 0])
            elif event.key == pygame.K_RIGHT:
                snake.changeDirec([50, 0])
            elif event.key == pygame.K_UP:
                snake.changeDirec([0, -50])
            elif event.key == pygame.K_DOWN:
                snake.changeDirec([ 0, 50])
    screen.fill('green')
    snake.move()
    apple.draw()
    snake.draw()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()