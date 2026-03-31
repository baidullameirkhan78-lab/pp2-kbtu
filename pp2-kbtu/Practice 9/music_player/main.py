import pygame
import os

# 1. Инициализация
pygame.init()
pygame.mixer.init()

# Экран (жай ғана терезе ашылып тұруы үшін)
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

# 2. Әндерді жүктеу
# Осы файл тұрған папкадағы 'music' папкасына жол сілтеу
music_dir = os.path.join(os.path.dirname(__file__), 'music')
songs = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
current_idx = 0

def play_song():
    if songs:
        pygame.mixer.music.load(os.path.join(music_dir, songs[current_idx]))
        pygame.mixer.music.play()
        print(f"Қазір ойнап тұр: {songs[current_idx]}")

# Бірінші әнді қосу
if songs:
    play_song()
else:
    print("Қате: 'music' папкасына .mp3 файлдарын салыңыз!")

# 3. Басқару циклі
running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: # P - Play/Pause
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            
            if event.key == pygame.K_s: # S - Stop
                pygame.mixer.music.stop()
            
            if event.key == pygame.K_n: # N - Next track
                current_idx = (current_idx + 1) % len(songs)
                play_song()
            
            if event.key == pygame.K_b: # B - Previous track
                current_idx = (current_idx - 1) % len(songs)
                play_song()

    screen.fill((30, 30, 30))
    pygame.display.flip()

pygame.quit()