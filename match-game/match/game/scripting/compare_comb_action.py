from itertools import combinations
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class CompareCombAction(Action):
    """
    An update action that compare interactions between the actors.
    
    The responsibility of CompareCombAction is to compare the combination given with the typer by the user
    and determinates if match so earn points or if doesn't the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new CompareCombAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the compare combination action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._dont_match(cast)
            
    def _dont_match(self, cast):
        """Updates the score.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        combination = cast.get_first_actor("combinations")
        user_comb = cast.get_first_actor("user_combs")
        c_typed = [self.c1, self.c2, self.c3, self.c4] 

        if c_typed[self.c1, self.c2, self.c3, self.c4].equals(combination()):
            points = combination.get_points()
            score.add_points(points)
            combination.reset()
    
        else: self._is_game_over = True