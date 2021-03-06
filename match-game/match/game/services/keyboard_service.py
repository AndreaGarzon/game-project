import pyray
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        self._keys['y'] = pyray.KEY_Y
        self._keys['b'] = pyray.KEY_B
        self._keys['r'] = pyray.KEY_R
        self._keys['g'] = pyray.KEY_G

    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (y, b, r, g)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (y, b, r, g)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)