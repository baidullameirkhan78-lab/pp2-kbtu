import pygame

# 1. Инициализация
pygame.init()

# 2. Экран параметрлері (50x50 доп сыю үшін жеткілікті)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Түстер
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 3. Доптың сипаттамасы (Талап бойынша)
# Радиусы 25 (диаметрі 50), ортада орналасады
x, y = WIDTH // 2, HEIGHT // 2
radius = 25
step = 20  # Әр басқанда 20 пиксельге қозғалады

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)  # Ақ фон
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Клавиштерді тексеру
        if event.type == pygame.KEYDOWN:
            # Шекарадан шықпауды тексеру (Boundary checking)
            if event.key == pygame.K_UP and y - step >= radius:
                y -= step
            if event.key == pygame.K_DOWN and y + step <= HEIGHT - radius:
                y += step
            if event.key == pygame.K_LEFT and x - step >= radius:
                x -= step
            if event.key == pygame.K_RIGHT and x + step <= WIDTH - radius:
                x += step

    # 4. Допты салу
    pygame.draw.circle(screen, RED, (x, y), radius)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()