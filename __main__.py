import math
import time
from typing import Union, Any
now = time.time
ever = '€'

import mini
from drawable import Drawable

from pygame.locals import *
import pygame


class Classy(mini.MiniApplication):

    player_vessel: Drawable
    dynamics: int

    def before(self):

        self.key_register = {}

        self.player_vessel = Drawable()
        self.player_vessel.pos = (50, 50)
        self.player_vessel.width = 10
        self.player_vessel.height = 20
        self.player_vessel_speed = 5
        self.player_vessel_focus_speed = 2
        
        self.drawables = []
        self.drawables.append(self.player_vessel)

    def draw(self):
        for x in self.drawables:
            x.draw(self.window)

    def handle_event(self, event):

        if event.type == MOUSEMOTION:
            self.drawables[0].pos = self.settings.mousepos

        if event.type == MOUSEBUTTONDOWN:
            self.boom()

        if event.type in (
            KEYUP, KEYDOWN
        ):
            self.key_handler(event)

    def key_handler(self, event):
        keyname = pygame.key.name(event.key)
        self.key_register[keyname] = self.key_register[event.key] = event.type == KEYDOWN
        print(self.key_register)

    def keypressed(self, codename: Union[int, str], default: Any = 0) -> int:
        return self.key_register.get(codename, default)

    def update(self):
        
        # Compute player vessel dynamics
        player_vessel_dynamics = (
            self.keypressed('right', 0) - self.keypressed('left', 0),
            self.keypressed('down', 0) - self.keypressed('up', 0),
        )

        player_vessel_speed = self.player_vessel_speed

        if self.keypressed('left shift'):
            player_vessel_speed = self.player_vessel_focus_speed

        player_vessel_dynamics = tuple(
            v * player_vessel_speed for v in player_vessel_dynamics
        )

        self.player_vessel >> player_vessel_dynamics

    def boom(self):
        # Create X projectiles
        # Give them motion
        for angle in range(0, 360, 30):

            t = Drawable()
            t.pos = self.settings.mousepos
            
            t.forces.append(
                {
                    'force': force,
                    'since': now(),
                    'for': ever
                }
            )


if __name__ == "__main__":
    
    app = Classy(
        name='shmupy',
        settings='settings.yaml'
    )
    app.run()