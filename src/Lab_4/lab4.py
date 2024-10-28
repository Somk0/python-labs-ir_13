
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
        return f"Притер {self.__name} за ціною {self.__price} надрукував {self.__pages} сторінок зі швидкістю {self.__speed} сторінок за хвилину"
    
    def __repr__(self):
        return f"self.__name = {self.__name},\nself.__speed = {self.__speed},\nself.__price = {self.__price}"
    

    def __del__(self):
        print(f"Deleted {self.__name}")
    

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getSpeed(self):
        return self.__speed

    def getPages(self):
        return self.__pages
        

    def setName(self, __name):
        self.__name = __name
        
    def setPrice(self, __price):
        self.__price = __price

    def setSpeed(self, __speed):
        self.__speed = __speed

    def setPages(self, __pages):
        self.__pages = __pages
        
    def getAllInfo(self):

        return [self.getName(), self.getPrice(), self.getSpeed(), self.getPages()]
        

    
    


    




    
        
def main():
        prnt1 = Printer("Neo2000", 42.50, 20, 100)
        prnt2 = Printer("Neo2001", 55, 25, 124)
        prnt3 = Printer("Neo2002", 60, 40, 345)

        # prnt1.getAllInfo()
        # prnt2.getAllInfo()
        # prnt3.getAllInfo()
        # print(Printer)
    
        

prnt1 = Printer("Neo2000", 42.50, 20, 100)
prnt2 = Printer("Neo2001", 55, 25, 124)
prnt3 = Printer("Neo2002", 60, 40, 345)

prnt1.setPages(999)



obj_ls = [prnt1, prnt2, prnt3]


def Printer_with_MinPages(objects):
        
        x = float('inf')
        results = []


        for obj in objects:
            
            if obj.getPages() < x:
                x = obj.getPages()

            
                results = obj

            
        return results
        
        


print(Printer_with_MinPages(obj_ls))