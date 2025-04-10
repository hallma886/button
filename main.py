# Draw Lines in Pygame / No Functions

# Pygame game template

import pygame
import sys
import config  # Import the config module

def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events(button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event

def main():

    screen = init_game()  # Initialize the game and get the screen
    clock = pygame.time.Clock() # Initialize the clock objecct
    
    font = pygame.font.SysFont('Georgia', 40, bold=True)
    surf = font.render('Quit', True, config.GREEN)

    button_length = 200
    button_width = 60
    button_x = 300
    button_y = 125
    button = pygame.Rect(button_x, button_y, button_length, button_width)

    surf_rect = surf.get_rect()
    surf_rect.center = button.center
 
    # Main game loop
    running = True
    while running:
        running = handle_events(button)  # Handle events and check if we should continue running

        # Fill the screen with a background color 
        screen.fill(config.BLACK) 

        mouse_x, mouse_y = pygame.mouse.get_pos() 

        if button.collidepoint(mouse_x, mouse_y):
            button_color = config.PURPLE
        else:
            button_color = config.ORANGE

            pygame.draw.rect(screen, button_color, button)

            screen.blit(surf, surf_rect) # surf is the text for the button, and surf_rect is the surface (area on the screen) where the button text will be drawn

        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































