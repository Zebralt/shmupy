from functools import wraps
from typing import Tuple, List
import time


def sacrilege(f):
    @wraps(f)
    def wrapper(self, other, default=None):
        if type(other) is tuple or default is not None:
            other = default is not None and (other, default) or other
            return self.move(other)
        return f(self, other)
    return wrapper


class Fixable:

    def __init__(self):
        self.pos = (0, 0)
        self.origin = (0, 0)
        self.forces: List[Tuple[int, int]] = [
            {
                'force': (0, 10),
                'since': time.time(),
                'for': 2000  # ms
            }
        ]

    @sacrilege
    def __ilshift__(self, other: int):
        """Move left."""
        x, y = self.pos
        x -= other
        self.pos = (x, y)
        return self

    @sacrilege
    def __irshift__(self, other: int):
        """Move right."""
        x, y = self.pos
        x += other
        self.pos = (x, y)
        return self

    @sacrilege
    def __ixor__(self, other: int):
        """Move up."""
        x, y = self.pos
        y -= other
        self.pos = (x, y)
        return self

    @sacrilege
    def __ior__(self, other: int):
        """Move down."""
        x, y = self.pos
        y += other
        self.pos = (x, y)
        return self

    def move(self, other: Tuple[int, int]):
        x, y = self.pos
        a, b = other
        x += a
        y += b
        self.pos = (x, y)
        return self

    def __lshift__(self, other):
        a = self
        a <<= other
        return a

    def __rshift__(self, other):
        a = self
        a >>= other
        return a

    def __xor__(self, other):
        a = self
        a ^= other
        return a

    def __or__(self, other):
        a = self
        a |= other
        return a

    def __matmul__(self, other):
        if type(other) is not tuple:
            other = other.pos
        other = other or (0, 0)
        x, y = self.pos
        a, b = other
        return (
            x - a,
            y - b
        )

    def update(self):
        pass

    



import pygame
class Drawable(Fixable):

    def __init__(self):
        super().__init__()
        self.hitbox = (0, 0)
        self.width, self.height = 5, 5

    def draw(self, screen):
        pygame.draw.rect(screen, (0xff, 0, 0xff), (*self.pos, self.width, self.height))


if __name__ == "__main__":
    
    a = Fixable()

    print(a.pos)
    a <<= 3
    print(a.pos)
    a >>= 24
    print(a.pos)
    a ^= 30
    print(a.pos)
    a |= 35
    print(a.pos)
    a >>= (5, 5)
    print(a.pos)
    a >>= 5, 5
    print(a.pos)
    print(a.pos)

    b = Drawable()