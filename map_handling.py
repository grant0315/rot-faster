import pygame, random
import constants as cons

# 1600 X 960 surface size = 50 cells by 30

class Map:
    """
    Map class: requires a xSize, and ySize. Probably just the dimensions of the x
    and y cells (30 x 50) or 1600 x 950 at 32 pixels per cell.
    """
    def __init__(self, xSize, ySize):
        self.map_dict = [[0] * cons.X_GRID_NUM] * cons.Y_GRID_NUM

        self.xSize = xSize
        self.ySize = ySize

        for i in range(len(self.map_dict)):
            for j in range(len(self.map_dict[0])):
                tile = Tile(i, j)
                self.map_dict[i][j] = tile


    """
    Generates and replaces specific parts of the map_dict to render later as streets
    """
    def road_building_gen(self):
        directions = ['n', 's', 'e', 'w']
        self.starting_node = 0
        self.ending_node = 0
        # Picking a starting cardinal direction to determine where the road starts
        # then remove that direction so that it can't be picked again, and select a new direction at random
        starting_direction = random.choice(directions)
        directions.remove(starting_direction)
        ending_direction = random.choice(directions)
        print("Starting Direction: {}".format(starting_direction))
        print("Ending Direction: {}".format(ending_direction))

        # Assin index of starting_node so that it starts at the choosen direction of the screen
        if (starting_direction == "n"):
            self.starting_node = (random.randint(0, cons.X_GRID_NUM), 0)
        elif (starting_direction == "s"):
            self.starting_node = (random.randint(0, cons.X_GRID_NUM -1), cons.Y_GRID_NUM -1)
        elif (starting_direction == "e"):
            self.starting_node = (cons.X_GRID_NUM -1, random.randint(0, cons.Y_GRID_NUM -1))
        elif (starting_direction == "w"):
            self.starting_node = (0, random.randint(0, cons.Y_GRID_NUM -1))
        
        if (ending_direction == "n"):
            self.ending_node = (random.randint(0, cons.X_GRID_NUM -1), 0)
        elif (ending_direction == "s"):
            self.ending_node = (random.randint(0, cons.X_GRID_NUM -1), cons.Y_GRID_NUM -1)
        elif (ending_direction == "e"):
            self.ending_node = (cons.X_GRID_NUM -1, random.randint(0, cons.Y_GRID_NUM -1))
        elif (ending_direction == "w"):
            self.ending_node = (0, random.randint(0, cons.Y_GRID_NUM))

        print(self.starting_node)
        print(self.ending_node)
        print(len(self.map_dict))
        print(len(self.map_dict[0]))
        
        # Assign specific tile to become a starting and ending node
        target_node = self.map_dict[self.starting_node[0]][self.starting_node[1]]
        print("Targeted starting node...")
        target_node.starting_node = True
        print("Target node is now starting node")

        target_node = self.map_dict[self.ending_node[0]][self.ending_node[1]]
        print("Targeted ending node...")
        target_node.ending_node = True
        print("Target node is now ending node")

        # Now create road going to specific direction

class Tile:
    """
    Each tile has a xPos (x position in grid) and yPos (y position in grid),
    starting_node is if the node is used to start the road at a specific position
    ending_node is if the node is used to end the road at a specific position
    tileType is to differeniate roads, buildings, etc...
    """
    def __init__(self, xPos, yPos, starting_node=False, ending_node=False, tileType=None):
        self.xPos = xPos
        self.yPos = yPos
        self.starting_node = starting_node
        self.ending_node = ending_node
        self.tileType = tileType
