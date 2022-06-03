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
    
        c_typed = []
        c1 = ()
        c2 = ()
        c3 = ()
        c4 = ()