import pygame

pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Paint Pro Smooth")

clock = pygame.time.Clock()

# 🖼️ WHITE CANVAS
canvas = pygame.Surface((W, H))
canvas.fill((255, 255, 255))

# 🎨 colors
colors = [
    (0, 0, 0),       # black
    (255, 0, 0),     # red
    (0, 255, 0),     # green
    (0, 0, 255),     # blue
    (255, 0, 255)    # pink
]

current_color = (0, 0, 0)

# 🖌️ brush sizes
brushes = {
    "pencil": 2,
    "pen": 5,
    "marker": 12,
    "eraser": 20
}

mode = "pen"
brush_size = brushes[mode]

drawing = False
last_pos = None   # ⭐ IMPORTANT FOR SMOOTH LINE

font = pygame.font.SysFont(None, 25)

# 🎨 color buttons
color_buttons = []
for i, c in enumerate(colors):
    rect = pygame.Rect(10 + i * 40, 10, 30, 30)
    color_buttons.append((rect, c))

# 🖌️ tool buttons
tool_buttons = {
    "pencil": pygame.Rect(10, 60, 80, 30),
    "pen": pygame.Rect(100, 60, 80, 30),
    "marker": pygame.Rect(190, 60, 80, 30),
    "eraser": pygame.Rect(280, 60, 80, 30)
}

running = True
while running:
    screen.fill((220, 220, 220))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 🖱️ mouse down
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True

            # 🎨 colors
            for rect, c in color_buttons:
                if rect.collidepoint(event.pos):
                    current_color = c
                    mode = "pen"

            # 🖌️ tools
            for name, rect in tool_buttons.items():
                if rect.collidepoint(event.pos):
                    mode = name
                    brush_size = brushes[name]

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None   # reset line

    # ✏️ SMOOTH DRAWING (FIX HERE 🔥)
    if drawing:
        pos = pygame.mouse.get_pos()

        if last_pos is not None:
            if mode == "eraser":
                pygame.draw.line(canvas, (255, 255, 255), last_pos, pos, brush_size)
            else:
                pygame.draw.line(canvas, current_color, last_pos, pos, brush_size)

        last_pos = pos

    # 🖼️ show canvas
    screen.blit(canvas, (0, 0))

    # 🎨 palette
    for rect, c in color_buttons:
        pygame.draw.rect(screen, c, rect)

    # 🖌️ tools UI
    for name, rect in tool_buttons.items():
        pygame.draw.rect(screen, (100, 100, 100), rect)
        text = font.render(name, True, (255, 255, 255))
        screen.blit(text, (rect.x + 5, rect.y + 5))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()