import sys
import pygame
import random
#try on

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        screen.fill("light green")
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        for i in range(20):
            pygame.draw.line(screen, (0, 0, 0), (i * 32, 0), (i * 32, 512))
        for i in range(16):
            pygame.draw.line(screen, (0, 0, 0), (0, i * 32), (640, i * 32))
        clock = pygame.time.Clock()
        mole_pos = (1,1)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    print(event.pos[0] // 32)
                    print(mole_pos[0] // 32)
                    if event.pos[0] // 32 == mole_pos[0] // 32:
                        if event.pos[1] // 32 == mole_pos[1] // 32:
                            new_pos_x = random.randrange(0, 20)
                            new_pos_y = random.randrange(0, 16)
                            screen.fill("light green")
                            for i in range(20):
                                pygame.draw.line(screen, (0, 0, 0), (i * 32, 0), (i * 32, 512))
                            for i in range(16):
                                pygame.draw.line(screen, (0, 0, 0), (0, i * 32), (640, i * 32))
                            screen.blit(mole_image, mole_image.get_rect(topleft=(new_pos_x * 32, new_pos_y * 32)))
                            mole_pos = (new_pos_x * 32, new_pos_y * 32)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
