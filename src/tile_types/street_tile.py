from map_handling import Tile
import constants as cons

class Street_tile(Tile):
    def __init__(self, xPos, yPos, starting_direction, ending_direction, starting_tile=False, ending_tile=False):
        super().__init__(xPos, yPos)

        self.starting_direction = starting_direction
        self.ending_direction = ending_direction
        self.starting_tile = starting_tile
        self.ending_tile = ending_tile

        self.tile_image = ""

    def render(self, surface):
        self.tile_image = self.determine_tile_pygame_image()
        surface.blit(self.tile_image, (self.xPos, self.yPos))
        print("rendered road")

    """
    Returns specified image for the tile_image by looking at starting_direction 
    and ending_direction 
    returns pygame.image.load type
    """
    def determine_tile_pygame_image(self):
        if (self.starting_direction ==  "n"):
            if (self.ending_direction == "e"):
                self.tile_image = cons.CLEAR_ROAD_BEND_UP_RIGHT
                print("I'm a road-section that starts north and ends east")

            elif (self.ending_direction == "s"):
                self.tile_image = cons.CLEAR_ROAD_VERT
                print("I'm a road-section that starts north and ends south")

            elif (self.ending_direction == "w"):
                self.tile_image = cons.CLEAR_ROAD_BEND_UP_LEFT
                print("I'm a road-section that starts north and ends west")

            else:
                print("Exception Error: Given no cardinal direction for self.ending_direction")

        elif (self.starting_direction == "s"):
            if (self.ending_direction == "e"):
                self.tile_image = cons.CLEAR_ROAD_BEND_DOWN_RIGHT
                print("I'm a road-section that starts south and ends east")

            elif (self.ending_direction == "w"):
                self.tile_image = cons.CLEAR_ROAD_BEND_DOWN_LEFT
                print("I'm a road-section that starts south and ends west")

            elif (self.ending_direction == "n"):
                self.tile_image = cons.CLEAR_ROAD_CROSS_VERT
                print("I'm a road-section that starts south and ends north")

            else:
                print("Exception Error: Given no cardinal direction for self.ending_direction")

        elif (self.starting_direction == "e"):
            if (self.ending_direction == "s"):
                return cons.CLEAR_ROAD_BEND_DOWN_RIGHT
                print("I'm a road-section that starts east and ends south")

            elif (self.ending_direction == "w"):
                return cons.CLEAR_ROAD_HORI
                print("I'm a road-section that starts east and ends west")

            elif (self.ending_direction == "n"):
                return cons.CLEAR_ROAD_BEND_UP_RIGHT
                print("I'm a road-section that starts east and ends north")

            else: 
                print("Exception Error: Given no cardinal direction for self.ending_direction")
      
        
        elif (self.starting_direction == "w"):
            if (self.ending_direction == "s"):
                return cons.CLEAR_ROAD_BEND_DOWN_LEFT
                print("I'm a road-section that starts west and ends south")

            elif (self.ending_direction == "e"):
                return cons.CLEAR_ROAD_CROSS_HORZ
                print("I'm a road-section that starts west and ends east")

            elif (self.ending_direction == "n"):
                return cons.CLEAR_ROAD_BEND_DOWN_LEFT
                print("I'm a road-section that starts north and ends west")

            else: 
                print("Exception Error: Given no cardinal direction for self.ending_direction")
            
        else:
            print("Execption Error: Given no cardinal direction for self.starting_direction")
