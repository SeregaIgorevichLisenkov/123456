from pygame import *
from random import randint
init()
# КЛАССЫ
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > win_height/24:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - win_height/4-win_height/24:
            self.rect.y += self.speed
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > win_height/24:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - win_height/4-win_height/24:
            self.rect.y += self.speed
# ФУНКЦИИ
# ПЕРЕМЕННЫЕ
FPS = 60
clock = time.Clock()
img_fon = "fon.jpg"
img_icon = "icon.png"
win_width = display.Info().current_w/1.25
win_height = display.Info().current_h/1.25
speed_x = randint(3, 6)
speed_y = randint(3, 6)
# ОКНО
window = display.set_mode((win_width, win_height)) # , RESIZABLE
background = transform.scale(image.load(img_fon), (win_width, win_height))
display.set_caption(' П И Н Г - П О Н Г ')
gameIcon = image.load(img_icon)
display.set_icon(gameIcon)
font.init()
font = font.Font(None, 50)
lose1 = font.render('ЛЕВЫЙ ПРОПУСТИЛ', True, (255, 200, 0))
lose2 = font.render('ПРАВЫЙ ПРОПУСТИЛ', True, (255, 200, 0))
# ОБЪЕКТЫ
# player_image, player_x, player_y, size_x, size_y, player_speed
racket_R = Player('RIGHT.jpg',  int(win_width-win_height/8),    int(win_height/2-win_height/8),  
int(win_height/16),             int(win_height/4),      15)
racket_L = Player('LEFT.jpg',   int(win_height/16),             int(win_height/2-win_height/8),   
int(win_height/16),             int(win_height/4),      15)
ball = GameSprite('ball.png',   win_width/2-25,                 win_height/2-25,   
int(win_height/8),              int(win_height/8),      5)

# ЦИКЛ
finish = False
run = True
game_over = False
while run:
    speed_x *= 1.001
    speed_y *= 1.001
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0,0))
        racket_L.update_L()
        racket_R.update_R()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket_L, ball) or sprite.collide_rect(racket_R, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (win_width/2-100,win_height/2-50))
            time.delay(1000)
            game_over = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (win_width/2-100,win_height/2-50))
            time.delay(1000)
            game_over = True
        if game_over == True:
            ball = GameSprite('ball.png',win_width/2-25,win_height/2-25,int(win_height/8),int(win_height/8),5)
            game_over = False
            finish = False
            run = True
        racket_L.reset()
        racket_R.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)




# ЦИКЛ
finish = False
run = True
game_over = False
while run:
    speed_x *= 1.001
    speed_y *= 1.001
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0,0))
        racket_L.update_L()
        racket_R.update_R()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket_L, ball) or sprite.collide_rect(racket_R, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            lose_text = font.render('ЛЕВЫЙ ПРОПУСТИЛ', True, (255, 200, 0))
            window.blit(lose_text, (win_width/2-100,win_height/2-50))
            time.delay(1000)
            game_over = True
        if ball.rect.x > win_width:
            finish = True
            lose_text = font.render('ПРАВЫЙ ПРОПУСТИЛ', True, (255, 200, 0))
            window.blit(lose_text, (win_width/2-100,win_height/2-50))
            time.delay(1000)
            game_over = True
        if game_over == True:
            ball = GameSprite('ball.png',win_width/2-25,win_height/2-25,int(win_height/8),int(win_height/8),5)
            game_over = False
            finish = False
            run = True
        racket_L.reset()
        racket_R.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)









