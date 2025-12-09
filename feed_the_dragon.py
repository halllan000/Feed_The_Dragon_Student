import pygame, random
from pygame.examples.go_over_there import event

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
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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
title_rect.midtop()

lives_text = make_text(font, f"Lives: {player_lives}", GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

# Set sounds and music
catching_coin = "assets/coin_sound.wav"
miss_coin = "assets/miss_sound.wav"
pygame.mixer.music.load("sounds/ftd_background.wav")

# Set images
dragon = pygame.image.load("assets/dragon.png")
dragon_rect = dragon.get_rect()
dragon_rect.leftcenter = (WINDOW_HEIGHT/2, 32)

coin = pygame.image.load("assets/coin.png")
coin_rect = coin.get_rect()
coin_rect.right = BUFFER_DISTANCE
coin_rect.yposition = random.randrange(64, 350)


# The main game loop
pygame.mixer.music.play("sounds/ftd_background_music.wav")
running = True

def tick():
    Clock.tick(FPS)


def is_still_running():
    global running
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False



def move_player(PLAYER_VELOCITY = None):
    pygame.key.get_pressed()
    if pygame.key.get_pressed()[pygame.K_UP]:
        PLAYER_VELOCITY += 10
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        PLAYER_VELOCITY -= 10


def handle_coin():
    global coin_velocity, player_lives, miss_coin
    # TODO:
    #   - Move the coin to the left each frame by subtracting coin_velocity from coin_rect.x.
    #   - If the coin passes off the left side of the screen (coin_rect.x < 0):
    #       * Subtract 1 from player_lives.
    #       * Play the miss sound.
    #       * Reset the coin's position:
    #           - x: WINDOW_WIDTH + BUFFER_DISTANCE
    #           - y: a random integer between a top margin (e.g., 64) and near the bottom edge.
    coin_velocity -= coin_rect.x
    if coin_rect.x < 0:
        player_lives -= 1
        miss_coin.play()

    pass # TODO: remove this when finished


def handle_collisions():
    # TODO:
    #   - Check if the player_rect and coin_rect are colliding using colliderect(...)
    #   - If they collide:
    #       * Increase score by 1
    #       * Play the coin sound
    #       * Increase coin_velocity by COIN_ACCELERATION
    #       * Reset the coin's position:
    #           - x: WINDOW_WIDTH + BUFFER_DISTANCE
    #           - y: random integer between the same top and bottom margins
    pass # TODO: remove this when finished


def update_hud():
    # TODO:
    #   - Re-create score_text and lives_text each frame using make_text(...),
    #     so they show the updated score and lives values.
    #   - Remember to use the same font and colors (GREEN and DARKGREEN).
    pass # TODO: remove this when finished


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
    pass # TODO: remove this when finished


def update_screen():
    # TODO:
    #   - Fill the display_surface with a background color (e.g., BLACK) using your fill(...) helper.
    #   - Draw the HUD elements on the screen:
    #       * score_text, title_text, lives_text at their rect positions using your blit(...) helper.
    #   - Draw a horizontal line across the screen near the top to separate the HUD from the play area.
    #   - Draw the player image and the coin image at their rect positions using your blit(...) helper.
    #   - Finally, call update_display() so that everything appears on the screen.
    pass


while running:
    # Main game loop steps:
    #   1. Handle quit events.
    #   2. Move the player based on keyboard input.
    #   3. Move the coin and handle misses.
    #   4. Check for collisions between player and coin.
    #   5. Update the HUD text to match the current score and lives.
    #   6. Check if the game is over and either reset or quit.
    #   7. Draw everything on the screen.
    #   8. Tick the clock to control the frame rate.

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
