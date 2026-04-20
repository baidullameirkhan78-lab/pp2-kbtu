import pygame
import random

pygame.init()

W, H = 600, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

block = 20

font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 50)

def reset_game():
    snake = [(300, 300)]
    direction = (block, 0)
    food = (random.randrange(0, W, block), random.randrange(0, H, block))
    score = 0
    speed = 8
    return snake, direction, food, score, speed

snake, direction, food, score, speed = reset_game()

game_over = False

restart_button = pygame.Rect(200, 320, 200, 50)

def random_food():
    while True:
        x = random.randrange(0, W, block)
        y = random.randrange(0, H, block)
        if (x, y) not in snake:
            return (x, y)

running = True
while running:
    screen.fill((20, 20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 🔁 Restart click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over and restart_button.collidepoint(event.pos):
                snake, direction, food, score, speed = reset_game()
                game_over = False

        # 🎮 Control
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP:
                direction = (0, -block)
            if event.key == pygame.K_DOWN:
                direction = (0, block)
            if event.key == pygame.K_LEFT:
                direction = (-block, 0)
            if event.key == pygame.K_RIGHT:
                direction = (block, 0)

    if not game_over:
        # 🐍 Move snake
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)

        # ❌ wall collision
        if head[0] < 0 or head[0] >= W or head[1] < 0 or head[1] >= H:
            game_over = True

        # ❌ self collision
        if head in snake[1:]:
            game_over = True

        # 🍎 food
        if head == food:
            score += 1
            food = random_food()
            speed += 0.3
        else:
            snake.pop()

        # 🐍 draw snake (worm style)
        for i, s in enumerate(snake):
            if i == 0:
                pygame.draw.circle(screen, (0, 255, 0), s, block//2)
            else:
                pygame.draw.circle(screen, (0, 200, 0), s, block//2)

        # 🍎 food
        pygame.draw.circle(screen, (255, 0, 0), food, block//2)

        # 📊 score
        text = font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(text, (10, 10))

    else:
        # 💀 GAME OVER SCREEN
        over_text = big_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(over_text, (150, 200))

        sub = font.render("YOU CRASHED 😈", True, (255,255,255))
        screen.blit(sub, (200, 260))

        # 🔁 Restart button
        pygame.draw.rect(screen, (0, 200, 0), restart_button)
        btn_text = font.render("RESTART", True, (0, 0, 0))
        screen.blit(btn_text, (250, 335))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()