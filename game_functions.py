import sys

import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """Respond to key press movements."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                 sys.exit()
        # Checks for keypresses up or down.
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)    
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship) 
        

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:    
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:    
        ship.moving_left = True
    elif event.key == pygame.K_UP:    
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:    
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def check_keyup_events(event, ship):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False    
    elif event.key == pygame.K_LEFT:    
        ship.moving_left = False   
    elif event.key == pygame.K_UP:    
        ship.moving_up = False   
    elif event.key == pygame.K_DOWN:    
        ship.moving_down= False
           
def update_screen(ai_settings, screen, ship, alien, bullets):
    # Redraw the screen during each pass through the loop. 
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ships and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
    #character.blitme() #include characters need to add another parameter
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit is not reached yet."""
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)