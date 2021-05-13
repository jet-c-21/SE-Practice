class Proxy:
    def __init__(self, subject):
        self.__subject = subject  # instance

    def __getattr__(self, name):
        print('get data via __getattr__ : ', end='')
        return getattr(self.__subject, name)


class RGB:
    def __init__(self, red, green, blue):
        self.__red = red
        self.__green = green
        self.__blue = blue

    def red(self):
        return self.__red

    def green(self):
        return self.__green

    def blue(self):
        return self.__blue


class NoBlueProxy(Proxy):
    def blue(self):
        return 0


rgb = RGB(100, 192, 240)
print(rgb.red())  # 100

proxy = Proxy(rgb)
print(proxy.green())  # 192

no_blue = NoBlueProxy(rgb)
print(no_blue.green())  # 192

print(no_blue.blue())  # 0
