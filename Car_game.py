import pygame
import random
import sys

# ابعاد صفحه
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WIN_WIDTH = 600

# رنگ‌ها
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# ابعاد خودرو
CAR_WIDTH = 50
CAR_HEIGHT = 100

# ابعاد دشمن
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 100

# سرعت بازی
GAME_SPEED = 15

class Car:
    def __init__(self):
        self.image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = WIN_WIDTH // 2 - CAR_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - CAR_HEIGHT - 20
        self.speed = 10

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Enemy:
    def __init__(self):
        self.image = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIN_WIDTH - ENEMY_WIDTH)
        self.rect.y = random.randint(-100, -50)
        self.speed = random.randint(5, 15)

    def move(self):
        self.rect.y += self.speed

    def reset(self):
        self.rect.x = random.randint(0, WIN_WIDTH - ENEMY_WIDTH)
        self.rect.y = random.randint(-100, -50)
        self.speed = random.randint(5, 15)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

def draw_menu(screen):
    font = pygame.font.Font(None, 74)
    text = font.render("Car Game", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 100))

    font = pygame.font.Font(None, 36)
    text = font.render("Press Space to Start", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Car Game")

    clock = pygame.time.Clock()

    car = Car()
    enemies = [Enemy() for _ in range(3)]

    score = 0
    font = pygame.font.Font(None, 36)

    game_active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not game_active:
                    game_active = True
                    score = 0
                    car.rect.x = WIN_WIDTH // 2 - CAR_WIDTH // 2
                    for enemy in enemies:
                        enemy.reset()

        keys = pygame.key.get_pressed()
        if game_active:
            if keys[pygame.K_LEFT]:
                car.move_left()
            if keys[pygame.K_RIGHT]:
                car.move_right()

            # Update logic
            for enemy in enemies:
                enemy.move()
                if car.rect.colliderect(enemy.rect):
                    game_active = False
                    draw_menu(screen)

            for enemy in enemies:
                if enemy.rect.y > SCREEN_HEIGHT:
                    enemy.reset()
                    score += 1

        # Draw everything
        screen.fill((0, 0, 0))
        if game_active:
            car.draw(screen)
            for enemy in enemies:
                enemy.draw(screen)

            score_text = font.render("Score: {}".format(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        else:
            draw_menu(screen)

        pygame.display.flip()
        clock.tick(GAME_SPEED)

if __name__ == "__main__":
    main()
