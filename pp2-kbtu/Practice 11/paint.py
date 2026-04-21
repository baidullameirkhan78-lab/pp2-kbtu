import pygame
import math

pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# current shape
shape = "square"

# drawing state
start_pos = None
end_pos = None
drawing = False

# saved shapes list
shapes = []

# function to draw shapes
def draw_shape(shape, start, end):
    x1, y1 = start
    x2, y2 = end

    if shape == "square":
        size = min(abs(x2 - x1), abs(y2 - y1))
        rect = pygame.Rect(x1, y1, size, size)
        pygame.draw.rect(screen, (255, 255, 255), rect, 2)

    elif shape == "right_triangle":
        points = [(x1, y2), (x1, y1), (x2, y2)]
        pygame.draw.polygon(screen, (0, 255, 0), points, 2)

    elif shape == "equilateral_triangle":
        height = abs(y2 - y1)
        points = [
            (x1, y2),
            (x2, y2),
            ((x1 + x2) // 2, y2 - height)
        ]
        pygame.draw.polygon(screen, (0, 0, 255), points, 2)

    elif shape == "rhombus":
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2
        points = [
            (mx, y1),
            (x2, my),
            (mx, y2),
            (x1, my)
        ]
        pygame.draw.polygon(screen, (255, 0, 0), points, 2)

running = True

while running:
    screen.fill((0, 0, 0))

    # draw all saved shapes
    for s in shapes:
        draw_shape(s[0], s[1], s[2])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # mouse down
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # mouse up
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            # save shape
            shapes.append((shape, start_pos, end_pos))

        # keyboard to change shape
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                shape = "square"
            if event.key == pygame.K_2:
                shape = "right_triangle"
            if event.key == pygame.K_3:
                shape = "equilateral_triangle"
            if event.key == pygame.K_4:
                shape = "rhombus"

    # preview while drawing
    if drawing and start_pos:
        mouse_pos = pygame.mouse.get_pos()
        draw_shape(shape, start_pos, mouse_pos)

    pygame.display.set_caption(f"Paint Tool - {shape}")
    pygame.display.update()
    clock.tick(60)

pygame.quit()