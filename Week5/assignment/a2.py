# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) => NoneType
    
        initialize a Rat with a symbol to show on the maze
        and two int to detect its position
        """
        
        self.symbol =symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ (Rat, int, int) => NoneType

        Set the rat's row and col instance variables to
        the given row and column.
        """
        
        self.row = row
        self.col = col

    def eat_sprout(self):
        """ (Rat) => NoneType

        Add one to the rat's instance variable
        num_sprouts_eaten
        """

        self.num_sprouts_eaten+=1

    def __str__(self):
        """ (Rat) => str

        Return a string representation of the rat,
        in this format:
        symbol at (row, col) ate num_sprouts_eaten sprouts.    
        """

        return '{0} at ({1}, {2}) ate {3} sprouts'.format(
            self.symbol,self.row,self.col,self.num_sprouts_eaten)
    
class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
