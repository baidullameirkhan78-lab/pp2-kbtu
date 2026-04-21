import pygame
import random

pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)
BLUE = (0, 0, 255)

# Player car
player = pygame.Rect(400, 500, 50, 80)

# Enemy car
enemy = pygame.Rect(random.randint(0, 750), -100, 50, 80)
enemy_speed = 5

# Coins list (x, y, weight)
coins = []
coin_timer = 0

score = 0

running = True
while running:
    screen.fill((30, 30, 30))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < 750:
        player.x += 5

    # Enemy movement
    enemy.y += enemy_speed
    if enemy.y > H:
        enemy.y = -100
        enemy.x = random.randint(0, 750)

    # Coin generation
    coin_timer += 1
    if coin_timer > 60:
        coin_timer = 0
        weight = random.choice([1, 2, 3])  # different weights
        coins.append([random.randint(0, 780), -20, weight])

    # Move coins
    for coin in coins:
        coin[1] += 4
        pygame.draw.circle(screen, YELLOW, (coin[0], coin[1]), 10)

        # Collision with player
        if player.collidepoint(coin[0], coin[1]):
            score += coin[2]
            coins.remove(coin)

            # Increase enemy speed every 10 coins
            if score % 10 == 0:
                enemy_speed += 1

    # Draw player and enemy
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)

    # Collision with enemy
    if player.colliderect(enemy):
        print("Game Over! Score:", score)
        running = False

    pygame.display.set_caption(f"Score: {score}")
    pygame.display.update()
    clock.tick(60)

pygame.quit()