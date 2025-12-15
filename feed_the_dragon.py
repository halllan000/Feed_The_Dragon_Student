import pygame, random

# Initialize pygame
pygame.init()


def make_text(font_object, text, color, background_color):
    return font_object.render(text, True, color, background_color)


def blit(surface, item, rect):
    surface.blit(item, rect)


def fill(surface, color):
    surface.fill(color)


def update_display():
    pygame.display.update()


# Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Dragon")

# Set FPS and clock
FPS = 60
Clock = pygame.time.Clock()

# Set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

# Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set fonts
font = pygame.font.Font("assets/AttackGraffiti.ttf", 32)

# Set text
score_text = make_text(font, f"Score: {score}", GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = make_text(font, "Feed the Dragon", GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.midtop = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 350)

lives_text = make_text(font, f"Lives: {player_lives}", GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

game_over_text = make_text(font, "GAMEOVER", GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = make_text(font, "Press any key to play again", GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 32)

# Set sounds and music
catching_coin = pygame.mixer.Sound("assets/coin_sound.wav")
miss_coin = pygame.mixer.Sound("assets/miss_sound.wav")

# Set images
dragon = pygame.image.load("assets/dragon_right.png")
dragon_rect = dragon.get_rect()
dragon_rect.left = (32, WINDOW_HEIGHT // 2)

coin = pygame.image.load("assets/coin.png")
coin_rect = coin.get_rect()
coin_rect.right = BUFFER_DISTANCE
coin_rect.yposition = random.randrange(64, 350)

# The main game loop
pygame.mixer.music.play()
running = True


def tick():
    Clock.tick(FPS)


def is_still_running():
    global running
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False


def move_player(PLAYER_VELOCITY=None):
    pygame.key.get_pressed()
    if pygame.key.get_pressed()[pygame.K_UP] and WINDOW_HEIGHT > 64:
        PLAYER_VELOCITY += 10
    if pygame.key.get_pressed()[pygame.K_DOWN] and WINDOW_HEIGHT > WINDOW_HEIGHT - 32:
        PLAYER_VELOCITY -= 10


def handle_coin():
    global player_lives
    coin_rect.x -= coin_velocity
    if coin_rect.x < 0:
        player_lives -= 1
        miss_coin.play()
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)


def handle_collisions():
    global score, coin_velocity
    if dragon_rect.colliderect(coin_rect):
        score += 1
        catching_coin.play()
        coin_velocity += COIN_ACCELERATION
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)


def update_hud():
    make_text(score_text, "Score: " + str(score), GREEN, DARKGREEN)
    make_text(lives_text, "Lives: " + str(player_lives), GREEN, DARKGREEN)



def game_over_check():
    # TODO:
    #   - If player_lives reaches 0:
    #       * Draw the game over text and the "press any key to play again" text on the screen.
    #       * Update the display so the player can see the game over screen.
    #       * Stop the background music.
    #       * Create a loop (e.g., is_paused = True) that:
    #           - Waits for events:
    #               + If the player presses any key (KEYDOWN):
    #                   · Reset score to 0
    #                   · Reset player_lives to PLAYER_STARTING_LIVES
    #                   · Reset player position to center vertically
    #                   · Reset coin_velocity to COIN_STARTING_VELOCITY
    #                   · Restart the background music
    #                   · Exit the pause loop (resume game)
    #               + If the player clicks the window close button (QUIT):
    #                   · Set running to False and exit the pause loop so the game can end.
    global score, player_lives, coin_velocity
    if player_lives > 0:
        make_text(game_over_text, "press any key to play again", GREEN, DARKGREEN)
        update_display()
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                score = 0
                player_lives = PLAYER_STARTING_LIVES
                coin_velocity = COIN_STARTING_VELOCITY
                pygame.mixer.music.play()
                is_paused = False



def update_screen():
    # TODO:
    #   - Fill the display_surface with a background color (e.g., BLACK) using your fill(...) helper.
    #   - Draw the HUD elements on the screen:
    #       * score_text, title_text, lives_text at their rect positions using your blit(...) helper.
    #   - Draw a horizontal line across the screen near the top to separate the HUD from the play area.
    #   - Draw the player image and the coin image at their rect positions using your blit(...) helper.
    #   - Finally, call update_display() so that everything appears on the screen.
    display_surface.fill(BLACK)
    score_text.blit(display_surface)
    title_text.blit(display_surface)
    lives_text.blit(display_surface)


    update_display()
    pass


while running:
    is_still_running()
    move_player()
    handle_coin()
    handle_collisions()
    update_hud()
    game_over_check()
    update_screen()
    tick()

# End the game
pygame.quit()
