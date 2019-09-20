import importlib


def Reload(some_func):
    want_reload = some_func()
    want_reload_module = importlib.import_module(want_reload)
    importlib.reload(want_reload_module)
    