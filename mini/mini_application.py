from typing import *
from random import randint

import pygame
from pygame.locals import (
    QUIT,
    MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEBUTTONUP,
    KEYDOWN, KEYUP
)

from .mini_settings import MiniSettings
from .mini_locals import *

# This is the bare class. To implement a game, you need to modify this class into your application. You also inherit
# to benefit from the init and close functions.

class MiniApplication:

    # Base class fields; don't override !
    name: Optional[str]
    settings: dict
    state: int
    inited: bool
    window: pygame

    def __init__(self,
        name: Optional[str] = None,
        settings: Optional[Union[str, dict]] = None
    ):
        
        self.state = State.RUNNING

        if settings:
            if type(settings) is str:
                settings = MiniSettings.load_from_file(settings)
            self.settings = settings

        self.name = name

        self.init()
        pass

    def before(self):
        ...

    # Operations at application start.
    def init(self):

        self.inited = True
        
        pygame.init()

        pygame.key.set_repeat(
            self.settings.key_repeat.delay,
            self.settings.key_repeat.frequency
        )
        
        self.window = pygame.display.set_mode(
            (self.settings.resolution.width, self.settings.resolution.height)
        )

        if self.name is not None:
            pygame.display.set_caption(self.name)
        
        pygame.display.flip()

        self.before()

    # Operations at application exit.
    def on_close(self):
        pass

    def set_settings(self, settings):
        self.settings = settings

    # This method must update the application (data structures, etc.)
    def update(self):
        ...

    # This method will draw content on the screen.
    def draw(self):
        ...


    def base_handle_event(self, event):

        if event.type == KEYDOWN:
            print('keydown', event.key, '(%s)' % pygame.key.name(event.key))
            if pygame.key.name(event.key) == 'q':
                self.state = 0
                return

        if 'pos' in event.__dict__:
            self.settings.mousepos = event.pos

        if event.type == QUIT:
            self.state = 0

    # Here you will handle events.
    def handle_event(self, event):

        print(event.dict)

        if event.type == MOUSEBUTTONDOWN:
            
            if event.button == MouseButton.LEFT:
                print('mouse down left')
        
        if event.type == MOUSEBUTTONUP:
            if event.button == MouseButton.LEFT:
                print('mouse up left')
        
        if event.type == MOUSEMOTION:
            self.settings.mousepos = event.pos

        if event.type == KEYDOWN:
            print('keydown', event.key, '(%s)' % pygame.key.name(event.key))
            if pygame.key.name(event.key) == 'q':
                self.state = 0
                return

        if event.type == KEYUP:
            print('keyup', event.key, '(%s)' % pygame.key.name(event.key))
            if pygame.key.name(event.key) == 'q':
                self.state = 0
                return

    def run(self):

        # main loop
        while (self.state & ApplicationState.RUNNING):

            pygame.time.Clock().tick(self.settings.refresh_rate)

            for event in pygame.event.get():
                self.base_handle_event(event)
                self.handle_event(event)

            self.update()
            
            self.window.fill(Color.black)
            self.draw()
            
            pygame.display.flip()

        self.on_close()
        return self.state

if __name__ == '__main__':
    MiniApplication().run()
