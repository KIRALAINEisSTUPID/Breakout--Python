import pygame
import random
from pygame import mixer
import os
pygame.init()

screen_width = 1440
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout * Level 2")

icon = pygame.image.load("Files/sprites and photos/icon2.png")
pygame.display.set_icon(icon)

bg = pygame.image.load("Files/sprites and photos/bg2.jpg")
bg = pygame.transform.scale(bg, (screen_width, screen_height))

game_over = False
won = False

ball_speed_x = 1
ball_speed_y = 1

ball_icon = pygame.image.load("Files/sprites and photos/ball2.png")
ball_icon = pygame.transform.scale(ball_icon, (75, 50))
ball_rect = ball_icon.get_rect()
ball_rect.center = (screen_width / 2, screen_height / 2)

score = 0
font = pygame.font.SysFont(None, 50)
font1 = pygame.font.SysFont(None, 150)
player = pygame.image.load("Files/sprites and photos/player2.png")
player = pygame.transform.scale(player, (250, 200))
player_rect = player.get_rect()
player_rect.center = (screen_width / 2, screen_height + 0.1)


class Brick:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.visible = True

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.color, self.rect)

    def hit(self):
        self.visible = False

bricks = []
brick_width = 100
brick_height = 50
for row in range(6):
    for col in range(14):  
        x = col * (brick_width + 5) + 10
        y = row * (brick_height + 5) + 50
        brick = Brick(x, y, brick_width, brick_height, (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
        bricks.append(brick)

def player_movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and player_rect.right < screen_width:
        player_rect.x += 5






















bg_sound = mixer.Sound('Files/audios/asgore.mp3')
game_over_sound = mixer.Sound('Files/audios/detemination.wav')
won_sound = mixer.Sound('Files/audios/misaki-undertale-ost-034-memory.wav')




























running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not game_over and not won:
        bg_sound.play(-1)

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

        for brick in bricks:
            if brick.visible and ball_rect.colliderect(brick.rect):
                ball_speed_y *= -1
                brick.hit()
                score += 10
                if score == 350:
                    won = True
        score_font = font.render("Score: " + str(score), True, (255, 255, 255))

        player_movement()
        screen.blit(bg, (0, 0))
        screen.blit(ball_icon, ball_rect)
        screen.blit(player, player_rect)
        screen.blit(score_font, (10, 10))

        for brick in bricks:
            brick.draw(screen)






    elif game_over:
            retry = pygame.image.load("Files/sprites and photos/image.png")
            retry = pygame.transform.scale(retry, (200, 200))
            retry_rect = retry.get_rect()
            retry_rect.center = (screen_width / 2 , screen_height/2)
            game_over_sound.play(-1)
            screen.fill('Black')
            screen.blit(retry, retry_rect)
            bg_sound.stop()
            game_over_photo = pygame.image.load("Files/sprites and photos/game_over.png")
            game_over_photo = pygame.transform.scale(game_over_photo, (500, 500))
            screen.blit(game_over_photo, (screen_width / 2 - 250, screen_height / 2 - 290))
            if retry_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                score = 0
                game_over_sound.stop()
                bg_sound.play(-1)
                game_over = False
                ball_rect.center = (screen_width / 2, screen_height / 2)
                for brick in bricks:
                    brick.visible = True
            
        
    elif won:
        next_button = pygame.image.load("Files/sprites and photos/next.png")
        next_button = pygame.transform.scale(next_button, (200, 200))
        next_button_rect = next_button.get_rect()
        next_button_rect.center = (screen_width / 2 , screen_height/2  )
        won_sound.play(-1)
        screen.fill('Black')
        screen.blit(next_button, next_button_rect)
        bg_sound.stop()
        won_text = font1.render("You Won", True, (255, 255, 255))
        screen.blit(won_text, (screen_width / 2 - 200, screen_height / 2 - 200))
        if next_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            running = False
            os.system("python boss_fight.py")
    screen.blit(score_font, (10, 10))        
    pygame.display.update()

pygame.quit()
