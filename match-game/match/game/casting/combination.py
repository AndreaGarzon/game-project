import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Combination(Actor):
    """
    The combination of colors that may be matched.
    
    The responsibility of Combination is to show a random combination of colors between yellow, blue, red and green.

    Attributes:
        _points (int): The points of each color.
    """
    def __init__(self):
        "Constructs a new Combination."
        super().__init__()
        self._points = 0
        self.set_text("@")
        self.set_color(None) 
        self.reset()
        
    def reset(self):
        """Selects a random combination of colors."""
        self._points = random.randint(1, 8)
        color_list = [constants.BLUE, constants.YELLOW, constants.RED, constants.GREEN]
        self._color = random.choice(color_list)
        
    def get_points(self):
        """Gets the points.
        
        Returns:
            points (int): The points of color.
        """
        return self._points

    def get_color(self):
        return self._color