import pygame

# Surface constants (16:9 aspect ratio)
HEIGHT = 1600
WIDTH = 960
SIZE = (HEIGHT, WIDTH)

# Cell size constants
CELL_SIZE = 32
TILE_SIZE_FACTOR = 4

# DONT CHANGE ME
X_GRID_NUM = HEIGHT // CELL_SIZE
Y_GRID_NUM = WIDTH // CELL_SIZE


# Color Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

"""
IMAGE CONSTRANTS
"""
# CLEAR ROAD IMAGES
PLAYER_IMG = pygame.image.load('assets/player_male.png')
CLEAR_ROAD_VERT = pygame.image.load('assets/tile042.png')
CLEAR_ROAD_HORZ = pygame.image.load('assets/tile042.png')
CLEAR_ROAD_CROSS_VERT = pygame.image.load('assets/tile044.png')
CLEAR_ROAD_CROSS_HORZ = pygame.image.load('assets/tile045.png')
CLEAR_ROAD_END_DOWN = pygame.image.load('assets/tile046.png')
CLEAR_ROAD_END_UP = pygame.image.load('assets/tile047.png')
CLEAR_ROAD_END_RIGHT = pygame.image.load('assets/tile048.png')
CLEAR_ROAD_END_LEFT = pygame.image.load('assets/tile049.png')
CLEAR_ROAD_INTER_UP = pygame.image.load('assets/tile050.png')
CLEAR_ROAD_INTER_DOWN = pygame.image.load('assets/tile051.png')
CLEAR_ROAD_INTER_LEFT = pygame.image.load('assets/tile052.png')
CLEAR_ROAD_INTER_RIGHT = pygame.image.load('assets/tile053.png')
CLEAR_ROAD_INTER_ALL = pygame.image.load('assets/tile054.png')
CLEAR_ROAD_BEND_DOWN_RIGHT = pygame.image.load('assets/tile055.png')
CLEAR_ROAD_BEND_DOWN_LEFT = pygame.image.load('assets/tile056.png')
CLEAR_ROAD_BEND_UP_RIGHT = pygame.image.load('assets/tile057.png')
CLEAR_ROAD_BEND_UP_LEFT = pygame.image.load('assets/tile055.png')


