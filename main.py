from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import pygame
import sys

def main():

    # Initializes pygame and sets a clock as well as delta time 
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    # Creates two groups to hold multiple game objects, in this case, updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Create an asteroid group
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Assign the two groups as containers for all future player objects. All player objects will be updatable and drawable
    Player.containers = (updatable, drawable)
    # Assign groups for Asteroid objects and AsteroidField
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    # Creates a screen based on SCREEN_WIDTH and SCREEN_HEIGHT that was set in constants.py
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:

        # Quits the game if the window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Sets the screen to black, can be RGB or string "black"
        #screen.fill((0, 0, 0))
        screen.fill("black")
        

        # Updates all objects within the updatable group
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()
        # Loops through each object in the drawable group and draws them
        for objects in drawable:
            objects.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
