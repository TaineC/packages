def logger(func):
    def wrapper():
        print('logging execution')
        func()
        print('log complete')
    return wrapper

@logger
def sample():
    for num in range(0,10):
        print(num)

sample()