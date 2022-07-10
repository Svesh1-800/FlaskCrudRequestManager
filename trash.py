import functools
import time

def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return _wrapper

@timer
def complex_calculation():
    """Some complex calculation."""
    time.sleep(0.5)
    return 42

def add_calc(target):

    def calc(self):
        return 42

    target.calc = calc
    return target

@add_calc
class MyClass:
    def __init__():
        print("MyClass __init__")

def simple_logger(func):
    def decorated(*args, **kwargs):
        print(f"You're about to call {func}")
        result = func(*args, **kwargs)
        print(f"You just called {func}")
        return result

    return decorated

@simple_logger
def hello_world():
    print("Hello, World!")