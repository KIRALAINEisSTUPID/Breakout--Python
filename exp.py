# import pygame
# import sys

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Полоска здоровья")

# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = 'yellow'

# max_hp = 100
# current_hp = max_hp
# hp_bar_length = 250
# hp_bar_height = 25
# hp_bar_x = (WIDTH - hp_bar_length) // 2
# hp_bar_y = HEIGHT // 2 - hp_bar_height // 2

# hp_decrease_amount = 10

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 current_hp = max(0, current_hp - hp_decrease_amount)

#     screen.fill(WHITE)

#     pygame.draw.rect(screen, RED, (hp_bar_x, hp_bar_y, hp_bar_length, hp_bar_height))
#     pygame.draw.rect(screen, GREEN, (hp_bar_x, hp_bar_y, current_hp / max_hp * hp_bar_length, hp_bar_height))

#     pygame.display.update()

import time
current =time.time()
while True:
    print(current)