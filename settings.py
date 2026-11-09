class Settings():
    """A class to store all settings in Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1600 
        self.screen_height = 900
        self.bg_color = (230, 230, 230) 
        
        # Ship Settings.
        self.ship_speed_factor = 1.5
        self.ship_limit = 2

        # Bullet settings. 
        self.bullet_speed_factor = 3 # per pixel
        self.bullet_width = 3 # per pixel
        self.bullet_height = 15 # per pixel
        self.bullet_color = 60, 60, 60 # RBG gray scale
        self.bullets_allowed = 3
        
        # Alien settings.
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        # Fleet_direction of 1 represents right: -1 represents left.
        self.fleet_direction = 1
        
        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialized settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # Scoring
        self.alien_points = 50
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increased speed settings and alien value points."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        
