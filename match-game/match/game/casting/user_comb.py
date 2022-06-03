import constants
from game.casting.actor import Actor
from game.shared.point import Point


class User_comb(Actor):
    """
    The user combination.
    
    The responsibility of user combination is to track the user combination input and compare with the combination given.

    Attributes:
        _points (int): The user's input.
    """
    def __init__(self):
        super().__init__()
        self._user_comb = []
        self._compare()

    def get_user_comb(self):
        return self._user_comb

    def color_next(self):
        # Add the color typed
        for c in self._user_comb:
            c.user_comb() 
        
    def _compare(self):
        c1 = 
        c2 = 
        c3 =
        c4 =

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)