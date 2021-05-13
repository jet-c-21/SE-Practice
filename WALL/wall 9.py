class Drink:
    company = 'jet drinks'  # class var

    def __init__(self, price, volume):
        self.price = price
        self.volume = volume

    def get_rate(self):
        return self.price / self.volume

    @staticmethod
    def change_company(s):
        Drink.company = s
        # self.__class__.company = s


class Vodka(Drink):

    def __init__(self, price, volume, alcohol_content):
        super().__init__(price, volume)
        self.alcohol_content = alcohol_content

    def get_rate2(self):
        return self.volume / self.price

    # def change_company_name(self, s):
    #     # self.__class__.company = s
    #     Drink.company = s
    #     # super.__class__.company = s


v1 = Vodka(100, 500, 40)
# v1.change_company('abc')
Drink.company = 'abc'

print(v1.company)

d1 = Drink(100, 500)
print(d1.company)
