import pygame
import math

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
PLAYER_RADIUS = 10
PLAYER_SPEED = 5
PLAYER_COLOR = (255, 255, 255)  # White
BACKGROUND_COLOR = (0, 0, 0)  # Black

class Player:
    def __init__(self):
        self.position = [int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2)]  # Starting position at center of screen
        self.rect = pygame.Rect(self.position[0], self.position[1], PLAYER_RADIUS * 2, PLAYER_RADIUS * 2)

    def draw(self, window):
        pygame.draw.circle(window, PLAYER_COLOR, self.position, PLAYER_RADIUS)

    def update(self, keys, walls):
        new_position = self.position.copy()

        if keys[pygame.K_LEFT]:
            new_position[0] -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            new_position[0] += PLAYER_SPEED
        if keys[pygame.K_UP]:
            new_position[1] -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            new_position[1] += PLAYER_SPEED

        # Update the rect for collision detection
        new_rect = pygame.Rect(new_position[0], new_position[1], PLAYER_RADIUS * 2, PLAYER_RADIUS * 2)

        for wall in walls:
            if wall.rect.colliderect(new_rect):
                break
        else:
            self.position = new_position
            self.rect = new_rect


class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, window):
        pygame.draw.rect(window, PLAYER_COLOR, self.rect)


class Door:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, window):
        pygame.draw.rect(window, PLAYER_COLOR, self.rect)


def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    player = Player()
    walls = [Wall(WINDOW_WIDTH // 3, 0, 10, WINDOW_HEIGHT // 2),
             Wall(2 * WINDOW_WIDTH // 3, WINDOW_HEIGHT // 2, 10, WINDOW_HEIGHT // 2)]
    door = Door(WINDOW_WIDTH - 20, int(WINDOW_HEIGHT * math.pi) % WINDOW_HEIGHT, 10, 40)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        player.update(keys, walls)

        window.fill(BACKGROUND_COLOR)
        player.draw(window)

        for wall in walls:
            wall.draw(window)

        door.draw(window)

        if player.rect.colliderect(door.rect):
            print("Transition to next level!")
            break

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
