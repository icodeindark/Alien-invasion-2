class Settings():
    """A class to store all settings for Alien invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color =  (230,230,230)

        #ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 50

        #Alien settings
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 1
        #fleet direction of 1 represnets right; -1 represents left.
        self.fleet_direction =1