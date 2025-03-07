class ctuStock(): #This makes a class called ctuStock.
    def __init__(self): #This makes the initializer with a 'self' argurment.
        self.__NameofShop = 'Default' #This is the attribute of the class for the name of the specific shop.
        self.__LocationofShop = 'Default' #This attribute of the class is for the location of the specific shop.
        self.__NumCustomers = 0 #This attribute of the class for the number of customers of the specific shop.
        self.__NumSales = 0 #This attribute of the class for the number of sale of the specific shop.
        self.__NumReturns = 0 #This attribute of the class for the number of returns of the specific shop.

    @property #this tells python that to follow is a getter.
    def NameofShop(self): #this is the name of the function/method for getting the name of the shop.
        return self.__NameofShop #this returns the value of the name of the shop.
    
    @NameofShop.setter #This is the setter to change the value of the Shops Name
    def NameofShop(self,NewName): #this is the name of the function to change the name of the shop and takes a second argument.
        self.__NameofShop = NewName #this changes the value of the attribute name of the shop.

    @property #this tells python that to follow is a getter.
    def LocationofShop(self):#this defines the function/method for getting the location of the shop.
        return self.__LocationofShop #this returns the value of the attribute of the location of the shop.
    
    @LocationofShop.setter #This is the setter to change the value of the Shops Location
    def LocationofShop(self,NewLocal): #this defines the function/method for getting the location of the shop and takes a second argument.
        self.__LocationofShop = NewLocal #This changes the location of the shop to the value of the second argument provided.

    @property #this tells python that to follow is a getter.
    def NumCustomers(self): #this method is used to retrieve the default value of the number of customers.
        return self.__NumCustomers #this returns the default value of the attribute of the number of customers.
    
    @NumCustomers.setter #This is the setter to change the value of the Shops Number of Customer.
    def NumCustomers(self,NewCusNum): #this makes the method to allow the number of customers to be changed.
        self.__NumCustomers = NewCusNum #this changes the value of the number of customers to the second argument.

    @property #this tells python that to follow is a getter for an attribute.
    def NumSales(self): #makes a function to get the number of sales for the specific shop.
        return self.__NumSales #this gives the current value of the Number of Sales.
    
    @NumSales.setter #This is the setter to change the value of the Shops Name
    def NumSales(self,NewSaleNum): #this makes the method to allow the number of sales to be changed.
        self.__NumSales = NewSaleNum #this allows the number of sales to be changed from the second argument.

    @property #this tells python that to follow is a getter.
    def NumReturns(self): #this function/method to retrieve the number of returns.
        return self.__NumReturns #this returns the current value of the attribute Number returns.
    
    @NumReturns.setter #This is the setter to change the value of the Shops Name
    def NumReturns(self,NewRetNum): #This funtion/methods allows to change the value of the number of returns.
        self.__NumReturns = NewRetNum #This sets the value of the Number of Returns to the value of the second arguements.

    SalesStockList = {"1.Laptop  ":"R5000","2.Mouse   ":"R80  ", "3.SSD     ": "R600 "} #This is the dictionary for the items and prcies
    StockQuantity = [35,40,50] #this is the list for the quantites for each item.

    def Menu2(): #this method is used to display the menu for the first option in the main menu.
        print("Shop Management\n1. Change Shop Name\n2. Change shop Location\n3. Display current shops\n4. Display all shops information\n0. Back\n") #displays second list
        UserSelSub = int(input("Select an option: ")) #this asks the user to select one of the options. 
        return UserSelSub #this returns the users selection. 
    
    def TestNameChange (NewName): #this method test the new name is not blank and requires an argument.
                if NewName == " ": #this compares the value of user name to the blank 
                    print ("Please do not leave this blank.\n") #this string will print if the string is blank
                    return False #this returns the value of false to be used out side the function.
                elif NewName == "": #this compares the value the user input to just an enter. 
                    print ("Please do not leave this blank.\n") #this will print if the string is blank
                    return False #this returns the value of false to be used out side the function. 
                else: #if none of the if statments are true then this will run.
                    return True #this returns the value of true to be used out side the function. 
                       
    def TestLocalChange (NewLocal): #this tests the location change if its one ofthe specific options and requires an argument.
        if NewLocal == "Free State": #This compares the user input with the string value
            return True #this returns the value of true to be used out side the function. 
        elif NewLocal == "Gauteng": #This compares the user input with the string value
            return True #this returns the value of true to be used out side the function. 
        elif NewLocal == "KZN": #This compares the user input with the string value
            return True #this returns the value of true to be used out side the function. 
        elif NewLocal == "Limpopo": #This compares the user input with the string value
            return True #this returns the value of true to be used out side the function. 
        elif NewLocal == "Default": #This compares the user input with the string value
            return True #this returns the value of true to be used out side the function. 
        else: #if none of the if statments are true then this will run.
            print ("Please select one of the options provided.\n") #this will print the string in the brackets
            return False #this returns the value of true to be used out side the function.
        
    def salesMenu(): #this function prints the menu for items for sale from the dictionary at the beginning.
            SalesList = ctuStock.SalesStockList #this assigns the stocklist at the start of the class to the variable.
            for key1,value1 in SalesList.items(): #loop iterates through the dictionary
                print(f"{key1}{value1}") #this prints both the key and the value.

    
    def Stocklist(MenuSelect): #this function prints the complete stocklist with all items and details and requires an argument.
            if MenuSelect == 1: #this compares the arugment with a number.
                Stocklist = ctuStock.SalesStockList #this assigns the dictionary at the top the variable stocklist
                StockNum = ctuStock.StockQuantity #this assigns the list at the top the variable stockNum
                StockAmount = 0 #this sets the variable stockamount to zero
                for key1,value1 in Stocklist.items(): #this loop is used to iterate through the dictionary.
                    print(f"Item:{key1} Price:{value1} Quantity:{StockNum[StockAmount]}") #this prints the key and value and the quantity from the list
                    StockAmount +=1 #this changes the value of stockamount to add 1 everytime the loop runs.
            elif MenuSelect == 2: #this compares the arugment to a number.
                StockNum = ctuStock.StockQuantity #this assigns the stockQuantity list to the variable StockNum
                return StockNum #this allows the value of StockNum to be used outside the function.
            
    def AddToStocklist(Item,Price,Quantity): #this function takes 4 arguments and allows the user to add to the stock list.
            NewItemlist = ctuStock.Stocklist(2) #this line calls the stocklist function and assigns it to NewItemlist.
            ctuStock.SalesStockList.update({'4.' + Item + ' \t':'R' + Price + '\t'}) #this updates the dictionary with the new values from the user
            NewItemlist.append(Quantity) #this adds the new quantity to the list.
            print ("Changes have been successfully made.") #once the code has run this will print to confirm that the changes have been made.
