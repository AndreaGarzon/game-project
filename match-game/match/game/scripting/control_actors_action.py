from ast import Constant
from turtle import color
import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the user_comb.
    
    The responsibility of ControlActorsAction is to get the user combination typed.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # yellow
        if self._keyboard_service.is_key_down('y'):
            c_typed = color(Constant.YELLOW)
        
        # blue
        if self._keyboard_service.is_key_down('b'):
             c_typed = color(Constant.BLUE)
        
        # red
        if self._keyboard_service.is_key_down('r'):
             c_typed = color(Constant.RED)
        
        # green
        if self._keyboard_service.is_key_down('g'):
             c_typed = color(Constant.GREEN)
        
        user_comb = cast.get_first_actor("user_comb")
       # snake.turn_head(self._direction)