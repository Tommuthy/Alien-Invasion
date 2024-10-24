import sys

import pygame

def check_events(ship):
    """Respond to key press movements."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                 sys.exit()
        
        # Moving ship to the right.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:    
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:    
                ship.moving_left = True            
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:    
                ship.moving_left = False   
        
def update_screen(ai_settings, screen, ship):
    # Redraw the screen during each pass through the loop. 
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #character.blitme() #include characters need to add another parameter
    # Make the most recently drawn screen visible.
    pygame.display.flip()