from argparse import Namespace
from typing import Any
import yaml


class AttributeDict:

    def __init__(self, inner: dict = None):
        self.__inner = inner or {}

    def __getattr__(self, key: str):
        return self.__inner.__getitem__(key)

    def __getitem__(self, key: Any):
        return self.__inner.__getitem__(key)

    def __setitem__(self, key: Any, value: Any):
        return self.__inner.__setitem__(key, value)

    def __setattr__(self, key: str, value: Any):
        if key == f'_{self.__class__.__qualname__}__inner':
            self.__dict__[key] = value
            return
        self.__inner.__setitem__(key, value)

    def __call__(self) -> dict:
        return self.__inner

    @classmethod
    def allthewaydown(cls, d: dict):
        
        result = AttributeDict()

        for key, value in d.items():

            if type(value) is dict:
                value = AttributeDict.allthewaydown(value)

            result[key] = value

        return result

    def __str__(self):
        return f'ADict{self.__inner}'

    def __repr__(self):
        return str(self)


if __name__ == "__main__":

    a = AttributeDict()
    a.tell = 3
    print(a)
    print(a())
    
    v = {'a': {'b': 3}}
    print(v)

    x = AttributeDict.allthewaydown(v)
    print(x)

    print(x.a, x.a.b)
    
    
class MiniSettings:

    def __init__(self):
        # default settings
        self.resolution = { 'width' : 800, 'height' : 600 }
        self.window_rect = (
            self.resolution['width'],
            self.resolution['height']
        )
        self.refresh_rate = 60
        self.key_repeat = {'delay' : 400, 'frequency' : 30}
        
    @staticmethod
    def load_from_file(filepath: str) -> dict:
        nn = AttributeDict.allthewaydown(yaml.safe_load(open(filepath)))
        return nn
