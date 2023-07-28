def Decarator(func):
    def inner(name):
        if name=="Python":
            return f'Good Morning {name}'
        else:
            return func(name)
    return inner

@Decarator
def Name(name):
    return name

print(Name("Python"))
