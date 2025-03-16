import pygame
import datetime 

pygame.init()

width = 1000
length = 850

screen = pygame.display.set_mode((width, length))

pygame.display.set_caption("toha's mickey clock 0_o")

mainclock = pygame.image.load(r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\mainclock.png")
righthand = pygame.image.load(r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\left.png")
lefthand = pygame.image.load(r"C:\Users\evrik\OneDrive\Desktop\uni\4 sem\python\LAB7\right.png")

clockCenter = screen.get_rect().center

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()

    secondAngle = (now.second / 60) * 360
    minuteAngle = (now.minute / 60) * 360

    location = mainclock.get_rect(center = clockCenter)
    screen.blit(mainclock, location)

    newLeft = pygame.transform.rotate(lefthand, -minuteAngle)
    leftLocation = newLeft.get_rect(center = clockCenter)
    screen.blit(newLeft, leftLocation)


    newRigth = pygame.transform.rotate(righthand, -secondAngle)
    rightLocation = newRigth.get_rect(center = clockCenter)
    screen.blit(newRigth, rightLocation)


    pygame.display.flip()