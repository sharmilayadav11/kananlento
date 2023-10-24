import pygame

def main():
    pygame.init()

    screen-pygame.display.set mode((800, 600))
    clock - pygame.time.clock()

    running-True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((200,150,200))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

        if __name__ == "__main__":
            main()