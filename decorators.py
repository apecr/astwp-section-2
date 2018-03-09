import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print('In the decorator!')
        func()
        print('After the decorator')
    return function_that_runs_func

@my_decorator
def a_function():
    print('I am the function')

a_function()