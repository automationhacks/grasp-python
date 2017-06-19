import importlib
import os


def get_module():
    prefix_path = 'xfiles.' + 'dummy'
    mod = importlib.import_module(prefix_path)
    print(mod)
    print(getattr(mod, 'DummyController'))
    print(getattr(mod, 'dummyController'))



get_module()
