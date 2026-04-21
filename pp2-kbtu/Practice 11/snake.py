import pygame
import random

pygame.init()

W, H = 600, 400
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

snake = [(100, 100)]
direction = (10, 0)

foods = []  # [x, y, weight, timer]
score = 0

def spawn_food():
    weight = random.choice([1, 2, 3])
    foods.append([random.randint(0, W-10), random.randint(0, H-10), weight, 300])

running = True
spawn_food()

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = (0, -10)
    if keys[pygame.K_DOWN]:
        direction = (0, 10)
    if keys[pygame.K_LEFT]:
        direction = (-10, 0)
    if keys[pygame.K_RIGHT]:
        direction = (10, 0)

    # Move snake
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    snake.insert(0, new_head)

    snake.pop()

    # Draw snake
    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*s, 10, 10))

    # Food logic
    for food in foods[:]:
        food[3] -= 1  # timer

        # remove if time ended
        if food[3] <= 0:
            foods.remove(food)
            continue

        pygame.draw.circle(screen, (255, 0, 0), (food[0], food[1]), 8)

        # collision
        if abs(new_head[0] - food[0]) < 10 and abs(new_head[1] - food[1]) < 10:
            score += food[2]
            foods.remove(food)
            snake.append(snake[-1])  # grow snake

    # spawn new food
    if random.randint(1, 80) == 1:
        spawn_food()

    pygame.display.set_caption(f"Score: {score}")
    pygame.display.update()
    clock.tick(10)

pygame.quit()