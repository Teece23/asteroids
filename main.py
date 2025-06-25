from constants import *
import pygame
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player= Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        dt =clock.tick(60)/1000
        updatable.update(dt)
        for a in asteroid:
                for s in shots:
                    if a.collision(s):
                        a.split()
                        s.kill()
        
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
            
        for a in asteroid:
            if player.collision(a):
                print ("Game Over!")
                sys.exit()

if __name__ == "__main__":
    main()

