from dataclasses import dataclass #this imports the dataclass module from the dataclasses libary
class table(): #this is the class for each table.
    def __init__(self): #this makes the class private.
        self.__tablename = ' '#this attribute is the name of the table.
        self.__assinged = str #this attribute is for future use.
        self.__NumofCus = int #this is for the number of customers
        self.__orderitems= [] #this is the list for orderitems for each table.
        self.__prices = [] #this is the list for prices for each table.
        self.__quantities = [] #this is the list for quantities for each table.


    @property
    def NumofCus(self): #this is the getter for the number of customers.
        return self.__NumofCus #this returns the value of attribute.
    
    @NumofCus.setter #this is the setter for the attribute.
    def NumofCus(self, CusNum): #this takes the argument for number of customers.
        self.__NumofCus = CusNum
    
    @property
    def orderitems(self):#this is the getter for the number of customers.
        return self.__orderitems #this returns the value of attribute.
    
    @orderitems.setter #this is the setter for the attribute.
    def orderitems(self, item):
        self.__orderitems = item

    @property
    def tablename(self):#this is the getter for the number of customers.
        return self.__tablename #this returns the value of attribute.
    
    @tablename.setter #this is the setter for the attribute.
    def tablename(self, name):
        self.__tablename = name

    @property
    def prices(self):#this is the getter for the number of customers.
        return self.__prices #this returns the value of attribute.
    
    @prices.setter #this is the setter for the attribute.
    def prices(self, prices):
        self.__prices = prices

    @property
    def quantities(self):#this is the getter for the number of customers.
        return self.__quantities #this returns the value of attribute.
    
    @quantities.setter #this is the setter for the attribute.
    def quantities(self, quant):
        self.__quantities =quant

@dataclass #this is to make the data class
class daysincome: #this names the data class
    totalsfortheday = int #this is the attribute for the total amount of money for the day.

    