import pygame
import sys
import time

pygame.init()
screen_width = 1440
screen_height = 800
boss_fight_song = pygame.mixer.Sound('Files/audios/muffet.mp3')
icon = pygame.image.load("Files/sprites and photos/icon.png")
pygame.display.set_icon(icon)
bg = pygame.image.load("Files/sprites and photos/boss_arena.jpg")
bg = pygame.transform.scale(bg, (screen_width, screen_height))
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout")
running = True
won = False
game_over = False
ball_speed_x = 5
ball_speed_y = 5
font = pygame.font.SysFont(None, 50)
font1 = pygame.font.SysFont(None, 100)

ball_icon = pygame.image.load("Files/sprites and photos/ball2.png")
ball_icon = pygame.transform.scale(ball_icon, (75, 50))
ball_rect = ball_icon.get_rect()
ball_rect.center = (screen_width / 2, screen_height / 2)

player = pygame.image.load("Files/sprites and photos/player2.png")
player = pygame.transform.scale(player, (250, 200))
player_rect = player.get_rect()
player_rect.center = (screen_width / 2, screen_height - 50)

def player_movement():
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_rect.left > 0:
        player_rect.x -= 9
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_rect.right < screen_width:
        player_rect.x += 9

class Projectile():
    def __init__(self, x, y):
        self.image = pygame.image.load("Files/sprites and photos/boss.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7

    def move(self):
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

class BOSS():
    def __init__(self):
        self.RED = (255, 0, 0)
        self.GREEN = '#beff74'
        
        self.max_hp = 400
        self.current_hp = self.max_hp
        self.hp_bar_length = 1000
        self.alive = True
        self.hp_bar_height = 25
        self.hp_bar_x = screen_width // 2 - self.hp_bar_length // 2
        self.hp_bar_y = 100
        self.hp_decrease_amount = 5
        self.image = pygame.image.load("Files/sprites and photos/boss.png")
        self.image = pygame.transform.scale(self.image, (500, 300))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2-100)
        self.speed = 5
        self.last_hit_time = 0
        self.hit_cooldown = 5  
        self.last_attack_time = time.time()
        self.attack_interval =3
        self.projectiles = []

    def draw(self):
        global ball_speed_x, ball_speed_y, game_over,won
        if self.alive:
            pygame.draw.rect(screen, self.RED, (self.hp_bar_x, self.hp_bar_y, self.hp_bar_length, self.hp_bar_height))
            pygame.draw.rect(screen, self.GREEN, (self.hp_bar_x, self.hp_bar_y, self.current_hp / self.max_hp * self.hp_bar_length, self.hp_bar_height))
            
            current_time = time.time()
            if self.rect.colliderect(ball_rect) and current_time - self.last_hit_time > self.hit_cooldown:
                self.current_hp = max(0, self.current_hp - self.hp_decrease_amount)
                self.last_hit_time = current_time
                ball_speed_y *= -1
                ball_speed_x *= -1

            self.move()
            screen.blit(self.image, self.rect)
            self.name = font1.render("Brickmaster - Galactic Overlord", True, '#beff74')
            screen.blit(self.name, (screen_width // 2 - self.name.get_width() // 2, 10))
            if self.current_hp <= 0:
                self.alive = False
                won = True

            if current_time - self.last_attack_time > self.attack_interval:
                self.attack()
                self.last_attack_time = current_time

            for projectile in self.projectiles:
                projectile.move()
                projectile.draw()
                if projectile.rect.colliderect(player_rect):
                    game_over = True
                if projectile.rect.y > screen_height:
                    self.projectiles.remove(projectile)

    def move(self):
        self.rect.x += self.speed 
        if self.rect.right >= screen_width or self.rect.left <= 0:
            self.speed *= -1

    def attack(self):
        projectile = Projectile(self.rect.centerx, self.rect.bottom)
        self.projectiles.append(projectile)

boss = BOSS()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not won and not game_over:
        screen.blit(bg, (0, 0))
        
        boss_fight_song.play(-1)
        ball_rect.y += ball_speed_y
        ball_rect.x += ball_speed_x

        if ball_rect.y > screen_height:
            game_over = True
        if ball_rect.y < 0:
            ball_speed_y *= -1
        if ball_rect.x > screen_width or ball_rect.x < 0:
            ball_speed_x *= -1
        if ball_rect.colliderect(player_rect):
            ball_speed_y *= -1
            ball_speed_x *= -1
        
        boss.draw()
        player_movement()
        screen.blit(player, player_rect)
        screen.blit(ball_icon, ball_rect)
    elif game_over:
            retry = pygame.image.load("Files/sprites and photos/image.png")
            retry = pygame.transform.scale(retry, (200, 200))
            retry_rect = retry.get_rect()
            retry_rect.center = (screen_width / 2 , screen_height/2)
            screen.fill('Black')
            screen.blit(retry, retry_rect)
            game_over_photo = pygame.image.load("Files/sprites and photos/game_over.png")
            game_over_photo = pygame.transform.scale(game_over_photo, (500, 500))
            screen.blit(game_over_photo, (screen_width / 2 - 250, screen_height / 2 - 290))
            if retry_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                score = 0
                game_over = False
                ball_rect.center = (screen_width / 2, screen_height / 2)
                boss.current_hp = boss.max_hp
    elif won:
            screen.blit(bg, (0, 0))

            boss_fight_song.stop()
            text = font.render("YOU WON", True, (255, 255, 255))
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
            

    pygame.display.update()

pygame.quit()
