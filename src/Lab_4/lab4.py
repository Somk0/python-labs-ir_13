
class Printer:



    __price : float
    __name : str 
    __speed : int
    __pages : int

    def __init__(self, __name, __price , __speed, __pages):
        self.__name = __name
        self.__price = __price
        self.__speed = __speed 
        self.__pages = __pages

    

    def __str__(self):
        return f"Принтер {self.__name} за ціною {self.__price} надрукував {self.__pages} сторінок зі швидкістю {self.__speed} сторінок за хвилину"
    
    def __repr__(self):
        return f"self.__name = {self.__name},\nself.__speed = {self.__speed},\nself.__price = {self.__price}"
    

    def __del__(self):
        print(f"Deleted {self.__name}")
    

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_speed(self):
        return self.__speed

    def get_pages(self):
        return self.__pages
        

    def set_name(self, __name):
        self.__name = __name
        
    def set_price(self, __price):
        self.__price = __price

    def set_speed(self, __speed):
        self.__speed = __speed

    def set_pages(self, __pages):
        self.__pages = __pages
        
    def get_all_info(self):

        return [self.get_name(), self.get_price(), self.get_speed(), self.get_pages()]
        

def main():
        prnt1 = Printer("Neo2000", 42.50, 20, 100)
        prnt2 = Printer("Neo2001", 55, 25, 124)
        prnt3 = Printer("Neo2002", 60, 40, 345)


prnt1 = Printer("Neo2000", 42.50, 20, 100)
prnt2 = Printer("Neo2001", 55, 25, 124)
prnt3 = Printer("Neo2002", 60, 40, 345)

prnt1.set_pages(999)



obj_ls = [prnt1, prnt2, prnt3]


def get_printer_with_min_pages(objects):
        
        x = float('inf')
        results = []


        for obj in objects:
            
            if obj.get_speed() < x:
                x = obj.get_speed()

            
                results = obj

        return results

print(Printer_with_MinPages(obj_ls))
