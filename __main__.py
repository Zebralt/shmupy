import math
import time
now = time.time
ever = '€'

import mini
from drawable import Drawable

import pygame.locals


class Classy(mini.MiniApplication):

    def before(self):
        t = Drawable()
        t.pos = (50, 50)
        self.drawables = [t]

    def draw(self):
        for x in self.drawables:
            x.draw(self.window)

    def handle_event(self, event):
        if event.type == pygame.locals.MOUSEMOTION:
            self.drawables[0].pos = self.settings.mousepos

        if event.type == pygame.locals.MOUSEBUTTONDOWN:
            self.boom()

    def update(self):
        self.drawables[0] >> 1

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