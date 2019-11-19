import math
import time
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
        self.player_vessel = Drawable()
        self.player_vessel.pos = (50, 50)
        self.player_vessel.width = 10
        self.player_vessel.height = 20
        self.dynamics = (0, 0)
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

        if event.type is KEYDOWN:
            keyname = pygame.key.name(event.key)
            if keyname in ('up', 'left', 'right', 'down'):
                print('down dynamic')
                x, y = self.dynamics
                x  += {
                    'up': -1,
                    'down': 1
                }.get(keyname, 0)
                y += {
                    'left': -1,
                    'right': 1
                }.get(event.key, 0)
                self.dynamics = (x, y)

        
        if event.type is KEYUP:
            if keyname in ('up', 'left', 'right', 'down'):
                print('up dynamic')
                x, y = self.dynamics
                x -= {
                    'up': -1,
                    'down': 1
                }.get(keyname, 0)
                y -= {
                    'left': -1,
                    'right': 1
                }.get(keyname, 0)
                self.dynamics = (x, y)


    def update(self):
        # Player vessel dynamics
        if sum(self.dynamics) != 0:
            print(self.dynamics)
            self.player_vessel >> self.dynamics

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