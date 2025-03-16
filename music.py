import pygame

pygame.init()

screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))

ArianaGrande = [
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\Ariana Grande - 7 rings.mp3",
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\Ariana Grande - break up with your girlfriend, i'm bored.mp3",
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\Ariana Grande - Dangerous Women.mp3",
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\Ariana Grande - Love Me Harder (feat. The Weeknd).mp3",
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\Ariana Grande - side to side (feat nicki minaj).mp3",
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\Ariana Grande - we can't be friends (wait for your love).mp3",
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\Ariana Grande - yes, and.mp3"
]

Backgrounds = [
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\7 rings.JPG",
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\break up with your girlfriend, i'm bored.JPG",
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\Dangerous Women.JPG",
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\Love Me Harder.JPG",
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\side to side.JPG",
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\we can't be friends.JPG",
    r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\yes, and.JPG"
]

currentTrack = 0

pygame.mixer.music.load(ArianaGrande[currentTrack]) 
pygame.mixer.music.play()

def load_background(path):
    image = pygame.image.load(path)
    return pygame.transform.smoothscale(image, (screen_width, screen_height))

background = load_background(Backgrounds[currentTrack])

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                currentTrack = (currentTrack + 1) % len(ArianaGrande)
                pygame.mixer.music.load(ArianaGrande[currentTrack]) 
                pygame.mixer.music.play()
                background = load_background(Backgrounds[currentTrack])
            elif event.key == pygame.K_LEFT:
                currentTrack = (currentTrack - 1) % len(ArianaGrande)
                pygame.mixer.music.load(ArianaGrande[currentTrack])
                pygame.mixer.music.play()
                background = load_background(Backgrounds[currentTrack])

    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
