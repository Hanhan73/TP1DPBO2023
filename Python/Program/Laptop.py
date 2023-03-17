
# deklarasi class

class Laptop:

    # deklarasi private atribut
    __brand = ""
    __model = ""
    __year = ""
    # constructor dengan parameter

    def __init__(self, brand="", model="", year=""):
        self.__brand = brand
        self.__model = model
        self.__year = year

    # setter dan getter untuk masing masing attribut
    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year
