import pygame
from board import Board

white = (222, 195, 164)
black = (31, 13, 3)

pygame.init()

window_size = (800,600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Chess")

running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # draw background
    screen.fill((255,255,255))

    # draw board
    pygame.draw.rect(screen, (46, 21,3), (0, 0, 420, 420))
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, white, (i * 50 + 10, j * 50 + 10, 50, 50))
            else : 
                pygame.draw.rect(screen, black, (i * 50 + 10, j * 50 + 10, 50, 50))

    # draw pieces
    pygame.draw.circle(screen, (255, 0, 0), (35, 35), 20)
    for i in range(8):
        for j in range(8):
            pygame.draw.circle(screen, (255, 0, 0), (i * 50 + 35, j * 50 + 35), 20)


    pygame.display.flip()

pygame.quit()