import pygame
import datetime
import os

# Pygame-ді іске қосу
pygame.init()

# Терезе өлшемі (Квадрат болуы керек)
W, H = 800, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mickey's Clock")

# Файл жолдарын анықтау
path = os.path.dirname(__file__)
img_path = os.path.join(path, 'images')

# Суреттерді жүктеу
try:
    # Сағат беті
    bg = pygame.image.load(os.path.join(img_path, 'main_clock.png')).convert()
    bg = pygame.transform.scale(bg, (W, H))

    # Қолдың суреті (Мөлдір фон болуы үшін convert_alpha маңызды)
    hand_orig = pygame.image.load(os.path.join(img_path, 'mickey_hand-removebg-preview.png')).convert_alpha()
    # Қолдың өлшемі (сағаттың радиусына лайықтап)
    hand_orig = pygame.transform.scale(hand_orig, (W // 2, H // 4)) 
except Exception as e:
    print(f"Қате: Суреттер табылмады! {e}")
    pygame.quit()
    exit()

def rotate_center(surf, image, angle, center_pos):
    # Суретті центрінен айналдыру
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center_pos)
    surf.blit(rotated_image, new_rect.topleft)

# Ойын циклы
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Уақытты алу
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    # Бұрышты есептеу (Миккидің қолы оңға қарап тұрса -90 қосамыз)
    # 6 градус = 1 секунд/минут
    sec_angle = -(seconds * 6) + 90
    min_angle = -(minutes * 6) + 90

    # Экранды тазалау және фонды салу
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))

    # Сағаттың ортасы
    center = (W // 2, H // 2)

    # Қолдарды салу
    rotate_center(screen, hand_orig, min_angle, center)
    rotate_center(screen, hand_orig, sec_angle, center)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()