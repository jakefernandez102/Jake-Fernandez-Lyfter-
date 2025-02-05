import inspect

def print_params_return(func):
    def wrapper(*args, **kwargs):
        function_return = func(*args,**kwargs)
        signature = inspect.signature(func)
        params_names = list(signature.parameters.keys())

        params={}
        for key,value in zip(params_names,args):
            params[key]=value

        print(params)    
        print(f' Here is the return of the function you are decorating: {function_return}\n')
    return wrapper

@print_params_return
def greet(name,day_time):
    greeting_output = f'Hello {name}, I wish you have a great {day_time}'
    return greeting_output

greet('Jake','day')
greet('Jake','night')
