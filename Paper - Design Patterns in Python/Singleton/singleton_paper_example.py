class Singleton(object):
    __single = None

    def __init__(self):
        if Singleton.__single:
            raise Singleton.__single
        Singleton.__single = self


def handle(x=Singleton):
    try:
        single = x()
    except Singleton as s:
        single = s
    return single


a = handle()
print(a)
b = handle()
print(b)
