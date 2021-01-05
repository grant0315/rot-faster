import pygame
from constants import *
from player import Player
from map_handling import Map

pygame.init()
rootSurface = pygame.display.set_mode(SIZE)
pygame.display.set_caption("RoT FaStEr")

isRunning = True
clock = pygame.time.Clock()

# MAP GENERATION STUFFS
opening_map = Map(X_GRID_NUM, Y_GRID_NUM)
opening_map.road_building_gen()

# init sprites object list
all_sprites_list = pygame.sprite.Group()

# Init player object
player = Player(WHITE, CELL_SIZE, CELL_SIZE)
player.rect.x = 200
player.rect.y = 300

# Add the player sprite to the list of objects
all_sprites_list.add(player)

# Main game loop
while isRunning:

    """
    ALL KEYHANDLING
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print("Player Movement: left")
                player.control(-CELL_SIZE, 0)

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print("Player Movement: right")
                player.control(CELL_SIZE, 0)

            if event.key == pygame.K_UP or event.key == ord('w'):
                print("Player Movement: up")
                player.control(0, -CELL_SIZE)

            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print("Player Movement: down")
                player.control(0, CELL_SIZE)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print("Player Movement: left stop")
                player.control(CELL_SIZE, 0)

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print("Player Movement: right stop")
                player.control(-CELL_SIZE, 0)

            if event.key == pygame.K_UP or event.key == ord('w'):
                print("Player Movement: up stop")
                player.control(0, CELL_SIZE)

            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print("Player Movement: down stop")
                player.control(0, -CELL_SIZE)

    # Game Logic
    all_sprites_list.update()

    # Drawing on screen
    rootSurface.fill(BLACK)

    # Now let;s draw all the the sprites in one go.
    all_sprites_list.draw(rootSurface)

    # Update the screen with what is drawn
    pygame.display.flip()

    # Limit to 2 frames per second
    clock.tick(10)

pygame.quit()   