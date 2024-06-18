import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
FRUIT_WIDTH = 30
FRUIT_HEIGHT = 30
SWEET_WIDTH = 30
SWEET_HEIGHT = 30
PLAYER_SPEED = 10
FRUIT_SPEED = 3
SWEET_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

background1 = pygame.image.load('backg.png')
backgroundwin1 = pygame.image.load('backgwin.png')
backgroundlose1 = pygame.image.load('backglose.png')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.transform.scale(background1,(SCREEN_WIDTH, SCREEN_HEIGHT))
backgroundwin = pygame.transform.scale(backgroundwin1,(SCREEN_WIDTH, SCREEN_HEIGHT))
backgroundlose = pygame.transform.scale(backgroundlose1,(SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pepe's Basket")

player_img1 = pygame.image.load('pepebowl1.png')
player_img = pygame.transform.scale(player_img1,(100,100))
fruit_img1 = pygame.image.load('egg.png')
fruit_img = pygame.transform.scale(fruit_img1,(50,50))
sweet_img1 = pygame.image.load('enemy.jpg')
sweet_img =pygame.transform.scale(sweet_img1,(50,50))
heart_img = pygame.image.load('heartfull.png')
heart_img = pygame.transform.scale(heart_img, (60, 60))

font = pygame.font.Font(None, 36)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT // 2)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED
        
# Eggplant class
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = fruit_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - FRUIT_WIDTH)
        self.rect.y = random.randint(-100, -FRUIT_HEIGHT)
    def update(self):
        self.rect.y += FRUIT_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - FRUIT_WIDTH)
            self.rect.y = random.randint(-100, -FRUIT_HEIGHT)
            global lives
            lives -= 1  
            if lives <= 0:
                game_over()

# Enemy class
class Sweet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sweet_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - SWEET_WIDTH)
        self.rect.y = random.randint(-100, -SWEET_HEIGHT)
    def update(self):
        self.rect.y += SWEET_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - SWEET_WIDTH)
            self.rect.y = random.randint(-100, -SWEET_HEIGHT)

# Game over
def game_over():
    while True:
        screen.fill(BLACK)
        screen.blit(backgroundlose,(0,0))
        game_over_text = font.render("Game Over! Your score: " + str(score), True, WHITE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

        retry_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2, 100, 50)
        quit_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 60, 100, 50)

        pygame.draw.rect(screen, WHITE, retry_button)
        pygame.draw.rect(screen, WHITE, quit_button)

        retry_text = font.render("Retry", True, BLACK)
        quit_text = font.render("Quit", True, BLACK)

        screen.blit(retry_text, (retry_button.x + 20, retry_button.y + 10))
        screen.blit(quit_text, (quit_button.x + 20, quit_button.y + 10))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.collidepoint(event.pos):
                    difficulty_screen()
                    return
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()

# Starting screen 
def start_screen():
    while True:
        screen.fill(WHITE)
        screen.blit(background,(0,0))
        title_text = font.render("Catch Eggplants and Avoid Enemies", True, BLACK)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

        start_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2, 100, 50)
        info_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 60, 100, 50)

        pygame.draw.rect(screen, BLACK, start_button)
        pygame.draw.rect(screen, BLACK, info_button)

        start_text = font.render("Start", True, WHITE)
        info_text = font.render("Info", True, WHITE)

        screen.blit(start_text, (start_button.x + 20, start_button.y + 10))
        screen.blit(info_text, (info_button.x + 20, info_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    difficulty_screen()
                    return
                if info_button.collidepoint(event.pos):
                    info_screen()

# Difficulty screen
def difficulty_screen():
    while True:
        screen.fill(WHITE)
        screen.blit(background,(0,0))
        difficulty_text = font.render("Select Difficulty", True, BLACK)
        screen.blit(difficulty_text, (SCREEN_WIDTH // 2 - difficulty_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

        easy_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2, 100, 50)
        medium_button = pygame.Rect(SCREEN_WIDTH // 2 - 65, SCREEN_HEIGHT // 2 + 60, 130, 50)
        hard_button = pygame.Rect(SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 + 120, 140, 50)

        pygame.draw.rect(screen, BLACK, easy_button)
        pygame.draw.rect(screen, BLACK, medium_button)
        pygame.draw.rect(screen, BLACK, hard_button)

        easy_text = font.render("Easy", True, WHITE)
        medium_text = font.render("Medium", True, WHITE)
        hard_text = font.render("Dank God", True, WHITE)

        screen.blit(easy_text, (easy_button.x + 20, easy_button.y + 10))
        screen.blit(medium_text, (medium_button.x + 20, medium_button.y + 10))
        screen.blit(hard_text, (hard_button.x + 10, hard_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    main(10)
                    return
                if medium_button.collidepoint(event.pos):
                    main(30)
                    return
                if hard_button.collidepoint(event.pos):
                    main(-1)
                    return

# Info screen 
def info_screen():
    while True:
        screen.fill(WHITE)
        screen.blit(background,(0,0))
        info_text = font.render("Author: Ann", True, BLACK)
        back_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 60, 100, 50)
        screen.blit(info_text, (SCREEN_WIDTH // 2 - info_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        pygame.draw.rect(screen, BLACK, back_button)
        back_text = font.render("Back", True, WHITE)
        screen.blit(back_text, (back_button.x + 20, back_button.y + 10))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    start_screen()
                    return

# Main 
def main(target_score):
    global score, lives, FRUIT_SPEED, SWEET_SPEED
    # Reset speeds
    FRUIT_SPEED = 3
    SWEET_SPEED = 5

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    fruits = pygame.sprite.Group()
    sweets = pygame.sprite.Group()

    # Create player
    player = Player()
    all_sprites.add(player)

    # Create fewer fruits and sweets
    for _ in range(2):
        fruit = Fruit()
        sweet = Sweet()
        all_sprites.add(fruit, sweet)
        fruits.add(fruit)
        sweets.add(sweet)

    # Score and lives
    score = 0
    lives = 3 

    # Run the game loop
    running = True
    clock = pygame.time.Clock()
    paused=False

    pause_button = pygame.Rect(SCREEN_WIDTH - 110, 10, 50, 30)
    exit_button = pygame.Rect(SCREEN_WIDTH - 60, 10, 50, 30)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button.collidepoint(event.pos):
                    paused = not paused
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()
                
        if not paused:
            # Update sprites
            all_sprites.update()

            # Check for collisions with enemies
            hitssw = pygame.sprite.spritecollide(player, sweets, True)
            for hitsw in hitssw: 
                lives -= 1
                sweet = Sweet()
                all_sprites.add(sweet)
                sweets.add(sweet)
                if lives <= 0:
                    game_over()
                    
            # Check for collisions with eggplants
            hits = pygame.sprite.spritecollide(player, fruits, True)
            for hit in hits:
                score += 1
                fruit = Fruit()
                all_sprites.add(fruit)
                fruits.add(fruit)
                # Increase speed every 15 points
                if score % 10 == 0:
                    FRUIT_SPEED += 1
                    SWEET_SPEED += 1

            # Draw everything
            screen.fill(WHITE)
            screen.blit(background,(0,0))
            all_sprites.draw(screen)

            # Draw the score
            score_text = font.render("Score: " + str(score), True, BLACK)
            screen.blit(score_text, (10, 10))

            # Draw lives as hearts
            for i in range(lives):
                screen.blit(heart_img, (SCREEN_WIDTH - (i + 10) * 40, 5,))

            # Draw pause button
            pygame.draw.rect(screen, BLACK, pause_button)
            pause_text = font.render("| |", True, WHITE)
            screen.blit(pause_text, (pause_button.x + 15, pause_button.y + 2))

            # Draw exit button
            pygame.draw.rect(screen, RED, exit_button)
            exit_text = font.render("X", True, WHITE)
            screen.blit(exit_text, (exit_button.x + 15, exit_button.y + 2,))

        else:
            pause_text = font.render("Paused", True, BLACK)
            screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
            
        pygame.display.flip()

        # Check if target score is reached
        if target_score != -1 and score >= target_score:
            game_won(target_score)

        # Frame rate
        clock.tick(60)

    pygame.quit()

# Game won
def game_won(target_score):
    while True:
        screen.fill(WHITE)
        screen.blit(backgroundwin,(0,0))
        win_text = font.render("Congratulations! You won!", True, BLACK)
        screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))

        retry_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2, 100, 50)
        quit_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 60, 100, 50)

        pygame.draw.rect(screen, BLACK, retry_button)
        pygame.draw.rect(screen, BLACK, quit_button)

        retry_text = font.render("Retry", True, WHITE)
        quit_text = font.render("Quit", True, WHITE)

        screen.blit(retry_text, (retry_button.x + 20, retry_button.y + 10))
        screen.blit(quit_text, (quit_button.x + 20, quit_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.collidepoint(event.pos):
                    difficulty_screen()
                    return
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()

if __name__ == "__main__":
    start_screen()