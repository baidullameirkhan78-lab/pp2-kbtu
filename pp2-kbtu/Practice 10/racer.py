import pygame
import random

pygame.init()
pygame.mixer.init()

W, H = 400, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Motorcycle Racer")

clock = pygame.time.Clock()

# 🏍️ Мотоцикл
bike_img = pygame.image.load("motorcycle.png")
bike_img = pygame.transform.scale(bike_img, (50, 70))

font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 50)

def reset_game():
    """Ойынды қайта бастау"""
    bike_rect = bike_img.get_rect()
    bike_rect.center = (200, 500)

    enemy = pygame.Rect(random.randint(0, 360), -100, 40, 60)
    coin = pygame.Rect(random.randint(0, 370), -50, 30, 30)

    return bike_rect, enemy, coin

bike_rect, enemy, coin = reset_game()

coins_collected = 0
speed = 5

particles = []
show_message = False
message_timer = 0

music_played = False

game_over = False

# 🔁 Restart кнопка
restart_button = pygame.Rect(130, 350, 140, 50)

running = True
while running:
    screen.fill((50, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 🔁 Кнопка басу
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over and restart_button.collidepoint(event.pos):
                bike_rect, enemy, coin = reset_game()
                coins_collected = 0
                particles = []
                show_message = False
                music_played = False
                game_over = False

    if not game_over:
        # 🕹️ Управление
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and bike_rect.x > 0:
            bike_rect.x -= 5
        if keys[pygame.K_RIGHT] and bike_rect.x < W - 50:
            bike_rect.x += 5

        # 🚗 Враг
        enemy.y += speed
        if enemy.y > H:
            enemy.y = -100
            enemy.x = random.randint(0, 360)

        # 💰 Монета
        coin.y += speed
        if coin.y > H:
            coin.y = -50
            coin.x = random.randint(0, 370)

        # 💰 Жинау
        if bike_rect.colliderect(coin):
            coins_collected += 1
            coin.y = -50
            coin.x = random.randint(0, 370)

            # 🎉 5 coin
            if coins_collected >= 5:
                show_message = True
                message_timer = pygame.time.get_ticks()

                for _ in range(25):
                    particles.append([
                        bike_rect.centerx,
                        bike_rect.centery,
                        random.randint(-5, 5),
                        random.randint(-5, 5)
                    ])

            # 🎧 10 coin
            if coins_collected >= 10 and not music_played:
                pygame.mixer.music.load("music.mp3")
                pygame.mixer.music.play()
                music_played = True

        # 💥 Соқтығыс
        if bike_rect.colliderect(enemy):
            game_over = True

        # 🎨 Рисуем
        screen.blit(bike_img, bike_rect)
        pygame.draw.rect(screen, (255, 0, 0), enemy)
        pygame.draw.circle(screen, (255, 255, 0), coin.center, 15)

        # 📊 Счёт
        text = font.render(f"Coins: {coins_collected}", True, (255, 255, 255))
        screen.blit(text, (250, 10))

        # 🎉 MOLDETS
        if show_message:
            text2 = font.render("MOLDETS!", True, (0, 255, 0))
            screen.blit(text2, (140, 300))

            if pygame.time.get_ticks() - message_timer > 2000:
                show_message = False

        # 💥 Шарлар
        for p in particles:
            p[0] += p[2]
            p[1] += p[3]
            pygame.draw.circle(
                screen,
                (random.randint(100,255), 0, random.randint(100,255)),
                (int(p[0]), int(p[1])),
                5
            )

        if len(particles) > 100:
            particles = particles[-100:]

    else:
        # ❌ GAME OVER SCREEN
        over_text = big_font.render("YOU LOSE", True, (255, 0, 0))
        screen.blit(over_text, (110, 200))

        sub_text = font.render("SLABAK 😈", True, (255, 255, 255))
        screen.blit(sub_text, (150, 260))

        # 🔁 Кнопка
        pygame.draw.rect(screen, (0, 200, 0), restart_button)
        btn_text = font.render("RESTART", True, (0, 0, 0))
        screen.blit(btn_text, (150, 365))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()