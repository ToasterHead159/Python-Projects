from ctuClass import ctuStock #this imports the class from the class file.
def Menu1(): #this function prints the first menu.
    print("1. Shop Management\n2. Sales\n3. Returns\n4. Stock\n99. Exit\n") #this is the string for menu
    UserSelMain = int(input("Select an option or 99 to exit: ")) #this asks the user to chose one of the options.
    return UserSelMain #this retyrns the users selection to be used outside the function.

shopOne = ctuStock() #this creates the object based on the class.
shopTwo = ctuStock()  #this creates the object based on the class.
shopThree = ctuStock()  #this creates the object based on the class.
shopFour = ctuStock()  #this creates the object based on the class.


while True: #this while loop allows for continuous use until the loop is broken.
    print("Welcome to CTU Technologies\n") #this prints the opening line of the program.
    UserSelMain = Menu1() #this calls the first menu for the main program and assigns the value of the user selection.

    if UserSelMain == 1: #this compares the user selection to a number.
        while True: #this allows to loop until the loop is broken.
            UserSelSub = ctuStock.Menu2() #this calls the menu2 function and assigns the return to the varaible.
            if UserSelSub == 1: #this compares the user selection to a number.
                print("Change Shop Name\n\n") #this prints the title of the next list.
                while True: #this allows to loop until the loop is broken.
                    print(f"Select Shop\n1. {shopOne.NameofShop}\n2. {shopTwo.NameofShop}\n3. {shopThree.NameofShop}\n4. {shopFour.NameofShop}\n0. Back") #this prints the list.
                    UserSelSub21 = int(input("Select an option: ")) #This asks the user to select an option and assigns the value to the variable.
                    if UserSelSub21 == 1: #this compares the user answer to a number.
                        NewName = input("Type the new Shop name: ") #this asks the user for the new name of the shop.
                        print("") #this prints a new blank line.
                        shopOne.NameofShop = NewName #this assigns the value of new name to the specific objects name of shop attribute.
                        while True: #this loop will continue until its is broken.
                            Test4Blank = ctuStock.TestNameChange(NewName) #this calls the test name function passes the new name to the fucntion and assigns the return to the variable.
                            if Test4Blank == False: #this test the value of the against the boolean value.
                                NewName = input("Type the new Shop name: ") #THis asks the user again for the newest value.
                                shopOne.NameofShop = NewName #this assigns the newest name to the atrribute.
                            elif Test4Blank == True: #this test the value of the against the boolean value.
                                print(f"Shop name was successfully changed to {NewName}\n") #this prints the confirmation message.
                                break #this breaks the while loop to stop checking the name.
                        break #this breaks the loop to go back from the shop selection menu.
                    elif UserSelSub21 == 2: #this compares the user selection to a number.
                        NewName = input("Type the new Shop name: ") # this asks the user for the new name and assigns the value to new name.
                        print("") #this prints a new blank line.
                        shopTwo.NameofShop = NewName #this assigns the value of new name to the specific objects name of shop attribute.
                        while True: #this loop will continue until its is broken.
                            Test4Blank = ctuStock.TestNameChange(NewName) #this calls the test name function passes the new name to the fucntion and assigns the return to the variable.
                            if Test4Blank == False: #this test the value of the against the boolean value.
                                NewName = input("Type the new Shop name: ") # this asks the user for the new name and assigns the value to new name.
                                shopTwo.NameofShop = NewName #this assigns the value of new name to the specific objects name of shop attribute.
                            elif Test4Blank == True: #this test the value of the against the boolean value.
                                print(f"Shop name was successfully changed to {NewName}\n") #this prints the confirmation message.
                                break #this breaks the while loop to stop checking the name.

                        break #this breaks the while loop to stop checking the name.
                    elif UserSelSub21 == 3: #this compares the user selection to a number.
                        NewName = input("Type the new Shop name: ") #This asks the user again for the newest value.
                        print("") #this prints a new blank line.
                        shopThree.NameofShop = NewName #this assigns the value of new name to the specific objects name of shop attribute.
                        while True: #this loop will continue until its is broken.
                            Test4Blank = ctuStock.TestNameChange(NewName) #this calls the test name function passes the new name to the fucntion and assigns the return to the variable.
                            if Test4Blank == False: #this test the value of the against the boolean value.
                                NewName = input("Type the new Shop name: ") # this asks the user for the new name and assigns the value to new name.
                                shopThree.NameofShop = NewName #this assigns the value of new name to the specific objects name of shop attribute.
                            elif Test4Blank == True: #this test the value of the against the boolean value.
                                print(f"Shop name was successfully changed to {NewName}\n") #this prints the confirmation message.
                                break #this breaks the while loop to stop checking the name.
                        break #this breaks the while loop to stop checking the name.
                    elif UserSelSub21 == 4:  #this compares the user selection to a number.
                        NewName = input("Type the new Shop name: ") #this ask the user for the shop name of shop 4.
                        print("") #this prints a new line.
                        shopFour.NameofShop = NewName #this assigns the new name to shop4s atrribute.
                        while True: #this loop will continue until broken.
                            Test4Blank = ctuStock.TestNameChange(NewName) ##this calls the test name function passes the new name to the fucntion and assigns the return to the variable.
                            if Test4Blank == False: #this test the value of the against the boolean value.
                                NewName = input("Type the new Shop name: ") # this asks the user for the new name and assigns the value to new name.
                                shopOne.NameofShop = NewName #this assigns the value of new name to the specific objects name of shop attribute.
                            elif Test4Blank == True: #this test the value of the against the boolean value.
                                print(f"Shop name was successfully changed to {NewName}\n") #this prints the confirmation message.
                                break #this breaks the while loop.
                        break #this breaks the while loop.
                    elif UserSelSub21 == 0: #this compares the user selection to a number.
                        break  #this breaks the loops and takes the user back to the main menu.
                    else: #this runs if the user selects something thats not on the current menu.
                        print("Invalid Selection") #this prints the string to tell the user that the selection they made are invalid.
            elif UserSelSub == 2: #this compares the user selection to a number.
                    while True: #this loop will continue until broken
                        print("Change Shop Location") #this is the title of the next menu.
                        print(f"Select Shop\n1. {shopOne.NameofShop},{shopOne.LocationofShop}\n2. {shopTwo.NameofShop},{shopTwo.LocationofShop}\n\
3. {shopThree.NameofShop},{shopThree.LocationofShop}\n4. {shopFour.NameofShop},{shopFour.LocationofShop}\n0. Back") #this prints the list with shop name and shop location.
                        UserSelSub22 = int(input("Select an option: ")) #this takes the user answer and assigns it to the variable.
                        if UserSelSub22 == 1: #this compares the value of the user input to the number.
                            NewLocal = input('Enter a location Free State, Gauteng, KZN, Limpopo or Default: ') #this asks the user for the location of the shop.
                            print("") #this prints a new line.
                            shopOne.LocationofShop = NewLocal #this assigns the new name to the location atrribute for the first shop.
                            while True: #this loop will run until broken.
                                Test4NewLocal = ctuStock.TestLocalChange(NewLocal) #This test the name agaisnt the critera in the class and assigns the return to the varible.
                                if Test4NewLocal == False: #this compares the variable to the boolean value.
                                    NewLocal = input('Enter a location Free State, Gauteng, KZN, Limpopo or Default: ')  #this asks the user for the location of the shop.
                                    shopOne.LocationofShop = NewLocal #this assigns the new name to the location atrribute for the first shop.
                                    continue #this allows code to continue so the loop doesnt break.
                                elif Test4NewLocal == True: #this compares the variable to the boolean value.
                                    print(f"Shop name was successfully changed to {NewLocal}\n") #this prints the confirmation message.
                                    break #this breaks the loop.
                                break #this breaks the loop.
                        elif UserSelSub22 == 2: #this compares the user selection to a number.
                            NewLocal = input('Enter a location Free State, Gauteng, KZN, Limpopo or Default: ')  #this asks the user for the location of the shop.
                            print("") #prints a new line.
                            shopTwo.LocationofShop = NewLocal #this assigns the new name to the location atrribute for the first shop.
                            while True: #this loop will run until broken.
                                Test4NewLocal = ctuStock.TestLocalChange(NewLocal) #This test the name agaisnt the critera in the class and assigns the return to the varible.
                                if Test4NewLocal == False: #this compares the variable to the boolean value.
                                    NewLocal = input('Enter a location Free State, Gauteng, KZN, Limpopo or Default: ') #this asks the user for the location of the shop.
                                    shopTwo.LocationofShop = NewLocal #this assigns the new name to the location atrribute for the first shop.
                                    continue #this allows code to continue so the loop doesnt break.
                                elif Test4NewLocal == True: #this compares the variable to the boolean value.
                                    print(f"Shop name was successfully changed to {NewLocal}\n") #this prints the confirmation message.
                                    break #this breaks the loop.
                                break #this breaks the loop.
                        elif UserSelSub22 == 3:  #this compares the user selection to a number.
                            NewLocal = input('Enter a location Free State, Gauteng, KZN, Limpopo or Default: ') #this asks the user for the location of the shop.
                            print("") #prints a new line.
                            shopThree.LocationofShop = NewLocal #this assigns the new name to the location atrribute for the first shop.
                            while True: #this loop will run until broken.
                                Test4NewLocal = ctuStock.TestLocalChange(NewLocal) #This test the name agaisnt the critera in the class and assigns the return to the varible.
                                if Test4NewLocal == False: #this compares the variable to the boolean value.
                                    NewLocal = input('Enter a location Free State, Gauteng, KZN, Limpopo or Default: ') #this asks the user for the location of the shop.
                                    shopThree.LocationofShop = NewLocal #this assigns the new name to the location atrribute for the first shop.
                                    continue #this allows code to continue so the loop doesnt break.
                                elif Test4NewLocal == True: #this compares the variable to the boolean value.
                                    print(f"Shop name was successfully changed to {NewLocal}\n") #this prints the confirmation message.
                                    break #this breaks the loop.
                                break #this breaks the loop.
                        elif UserSelSub22 == 4: #this compares the user selection to a number.
                            NewLocal = input('Enter a location Free State, Gauteng, KZN, Limpopo or Default: ') #this asks the user for the location of the shop.
                            print("") #prints a new line.
                            shopFour.LocationofShop = NewLocal #this assigns the new name to the location atrribute for the first shop.
                            while True: #this loop will run until broken.
                                Test4NewLocal = ctuStock.TestLocalChange(NewLocal) #This test the name agaisnt the critera in the class and assigns the return to the varible.
                                if Test4NewLocal == False: #this compares the variable to the boolean value.
                                    NewLocal = input('Enter a location Free State, Gauteng, KZN, Limpopo or Default: ') #this asks the user for the location of the shop.
                                    shopFour.LocationofShop = NewLocal #this assigns the new name to the location atrribute for the first shop.
                                    continue #this allows code to continue so the loop doesnt break.
                                elif Test4NewLocal == True: #this compares the variable to the boolean value.
                                    print(f"Shop name was successfully changed to {NewLocal}\n") #this prints the confirmation message.
                                    break #this breaks the loop.
                                break #this breaks the loop.
                        elif UserSelSub22 == 0: #this compares the user selection to a number and if true it breaks the loop to return the user to the main menu.
                            break #this breaks the loop.
            elif UserSelSub == 3: #this compares the user selection to a number.
                print("Current Shops\n") #this prints the name of the current menu.
                print(f"1. {shopOne.NameofShop},{shopOne.LocationofShop}\n2. {shopTwo.NameofShop},{shopTwo.LocationofShop}\n\
3. {shopThree.NameofShop},{shopThree.LocationofShop}\n4. {shopFour.NameofShop},{shopFour.LocationofShop}\n") #this prints a menu.
            elif UserSelSub == 4: #this compares the user selection to a number.
                for shop in [shopOne,shopTwo,shopThree,shopFour]: #this loop iterstes through the list of shops to print the name and location of the shop.
                    print("----------------") #this prints the dividing lines to separate each shop.
                    print(f"Shop Name: {shop.NameofShop}\nShop Location: {shop.LocationofShop}\nNumber of Customers: {shop.NumCustomers}\n\
Current Sales: {shop.NumSales}\nReturns: {shop.NumReturns}") #this prints the all the specifics shops details.
                    print("----------------\n") #this prints the dividing lines to separate each shop.
            elif UserSelSub == 0: #this compares the user selection to a number and if true it breaks the loop to return the user to the main menu.
                break #this breaks the loop.      
            else: #this is if an invalid selection was made by user.
                print("Invalid Selection") #this prints the string to tell the user that the selection was invalid.
    elif UserSelMain == 2: #this compares the user selection to a number.
      while True: #this loop will continue until broken
        print("Sales\n\nHere is a list of items for sale: ") # this is the title of the next list.
        ctuStock.salesMenu() #this calls the sale menu from the class file.
        UserBuyInput = int(input("\nSelect an option: ")) #this asks the user to select something from the menu and assigns the value to the variable.
        if UserBuyInput == 1: #this compares the user selection to a number.
            QuantityofItem = int(input(f"You have chosen the Laptop for R5000.\nHow many would you like to purchase? ")) #this asks the user how man laptops they would like to purchase.
            print("Please select the shop you would like to purchase from:") #this prints the string
            ShopSelection = int(input(f"1. {shopOne.NameofShop}\n2. {shopTwo.NameofShop}\n3. {shopThree.NameofShop}\n4. {shopFour.NameofShop}\n0. Back\nSelect a shop: ")) #this prints the menu and assigns the userinput to a variable.
            if ShopSelection == 1: #this compares the user selection to a number.
                ShopSelection = shopOne.NameofShop #this assignes the name of shop one to the variable.
                print(f"You have chosen {QuantityofItem} Laptop(s) from {ShopSelection}") #this tells the user how many latops they have bought from which shop.
                shopOne.NumCustomers += 1 #this changes the customers by 1 everytime a purchase is made.
                shopOne.NumSales += QuantityofItem #this increases the number of sales by the amount the user purchases
                ctuStock.StockQuantity[0] -=  QuantityofItem #this changes the stock amount by the number of items bought.
            elif ShopSelection == 2: #this compares the user selection to a number.
                ShopSelection = shopTwo.NameofShop #this assignes the name of  the shop to the variable.
                print(f"You have chosen {QuantityofItem} Laptop(s) from {ShopSelection}") #this tells the user how many latops they have bought from which shop.
                shopTwo.NumCustomers += 1 #this changes the customers by 1 everytime a purchase is made.
                shopTwo.NumSales += QuantityofItem #this increases the number of sales by the amount the user purchases
                ctuStock.StockQuantity[0] -= QuantityofItem  #this changes the stock amount by the number of items bought.
            elif ShopSelection == 3: #this compares the user selection to a number.
                ShopSelection = shopThree.NameofShop #this assignes the name of  the shop to the variable.
                print(f"You have chosen {QuantityofItem} Laptop(s) from {ShopSelection}") #this tells the user how many latops they have bought from which shop.
                shopThree.NumCustomers += 1 #this changes the customers by 1 everytime a purchase is made.
                shopThree.NumSales += QuantityofItem #this increases the number of sales by the amount the user purchases
                ctuStock.StockQuantity[0] -= QuantityofItem  #this changes the stock amount by the number of items bought.
            elif ShopSelection == 4: #this compares the user selection to a number.
                ShopSelection = shopFour.NameofShop #this assignes the name of the shop to the variable.
                print(f"You have chosen {QuantityofItem} Laptop(s) from {ShopSelection}") #this tells the user how many latops they have bought from which shop.
                shopFour.NumCustomers += 1 #this changes the customers by 1 everytime a purchase is made.
                shopFour.NumSales += QuantityofItem #this increases the number of sales by the amount the user purchases
                ctuStock.StockQuantity[0] -= QuantityofItem  #this changes the stock amount by the number of items bought.
            else: #this runs when the user selects an option that isn't one of the options.
                print("Invalid Selection") #this prints the string to tell the user that the selection was invalid.
            break #this breaks the loop.
        
        elif UserBuyInput == 2: #this compares the user selection to a number.
            QuantityofItem = int(input(f"You have chosen the Mouse for R80.\nHow many would you like to purchase? ")) #this asks the user how many mouses they would like to purchase
            print("Please select the shop you would like to purchase from:") #this prints the string
            ShopSelection = int(input(f"1. {shopOne.NameofShop}\n2. {shopTwo.NameofShop}\n3. {shopThree.NameofShop}\n4. {shopFour.NameofShop}\n0. Back\nSelect a shop: ")) #prints the list and asks the user and assigns asnwer to the variable.
            if ShopSelection == 1:#this compares the user selection to a number.
                ShopSelection = shopOne.NameofShop #this assignes the name of the shop to the variable.
                print(f"You have chosen {QuantityofItem} Mouse(s) from {ShopSelection}") #this tells the user how many Mouse(s) they have bought from which shop.
                shopOne.NumCustomers += 1 #this changes the customers by 1 everytime a purchase is made.
                shopOne.NumSales = QuantityofItem #this changes the stock amount by the number of items bought.
                ctuStock.StockQuantity[1] -=  QuantityofItem #this changes the stock amount by the number of items bought.
            elif ShopSelection == 2: #this compares the user selection to a number.
                ShopSelection = shopTwo.NameofShop #this assignes the name of the shop to the variable.
                print(f"You have chosen {QuantityofItem} Mouse(s) from {ShopSelection}") #this tells the user how many Mouse(s) they have bought from which shop.
                shopTwo.NumCustomers += 1 #this changes the customers by 1 everytime a purchase is made.
                shopTwo.NumSales = QuantityofItem  #this changes the stock amount by the number of items bought.
                ctuStock.StockQuantity[1] -=  QuantityofItem #this changes the stock amount by the number of items bought.
            elif ShopSelection == 3: #this compares the user selection to a number.
                ShopSelection = shopThree.NameofShop #this assignes the name of the shop to the variable.
                print(f"You have chosen {QuantityofItem} Mouse(s) from {ShopSelection}") #this tells the user how many Mouse(s) they have bought from which shop.
                shopThree.NumCustomers += 1 #this changes the customers by 1 everytime a purchase is made.
                shopThree.NumSales = QuantityofItem #this changes the stock amount by the number of items bought.
                ctuStock.StockQuantity[1] -=  QuantityofItem #this changes the stock amount by the number of items bought.
            elif ShopSelection == 4: #this compares the user selection to a number.
                ShopSelection = shopFour.NameofShop #this assignes the name of the shop to the variable.
                print(f"You have chosen {QuantityofItem} Mouse(s) from {ShopSelection}") #this tells the user how many Mouse(s) they have bought from which shop.
                shopFour.NumCustomers += 1 #this changes the customers by 1 everytime a purchase is made.
                shopFour.NumSales = QuantityofItem #this changes the stock amount by the number of items bought.
                ctuStock.StockQuantity[1] -=  QuantityofItem #this changes the stock amount by the number of items bought.
            else: #this runs when the user selects an option that isn't one of the options.
                print("Invalid Selection") #this prints the string to tell the user that the selection was invalid.
            break #this breaks the loop.
        elif UserBuyInput == 3: #this compares the user selection to a number.
            QuantityofItem = int(input(f"You have chosen the SSD for R600.\nHow many would you like to purchase? ")) #this asks the user how many SSDs they would like to purchase
            print("Please select the shop you would like to purchase from:") #this prints the string
            ShopSelection = int(input(f"1. {shopOne.NameofShop}\n2. {shopTwo.NameofShop}\n3. {shopThree.NameofShop}\n4. {shopFour.NameofShop}\n0. Back\nSelect a shop: ")) #prints the list and asks the user and assigns asnwer to the variable.
            if ShopSelection == 1: #this compares the user selection to a number.
                ShopSelection = shopOne.NameofShop #this assignes the name of the shop to the variable.
                print(f"You have chosen {QuantityofItem} SSD(s) from {ShopSelection}") #this tells the user how many SSDs they have bought from which shop.
                shopOne.NumCustomers += 1 #this changes the customers by 1 everytime a purchase is made.
                shopOne.NumSales = QuantityofItem #this increases the number of sales by the amount the user purchases
                ctuStock.StockQuantity[2] -=  QuantityofItem  #this changes the stock amount by the number of items bought.
            elif ShopSelection == 2: #this compares the user selection to a number.
                ShopSelection = shopTwo.NameofShop #this assignes the name of the shop to the variable.
                print(f"You have chosen {QuantityofItem} SSD(s) from {ShopSelection}") #this tells the user how many SSDs they have bought from which shop.
                shopTwo.NumCustomers += 1 #this changes the customers by 1 everytime a purchase is made.
                shopTwo.NumSales = QuantityofItem #this increases the number of sales by the amount the user purchases
                ctuStock.StockQuantity[2] -=  QuantityofItem #this changes the stock amount by the number of items bought.
            elif ShopSelection == 3: #this compares the user selection to a number.
                ShopSelection = shopThree.NameofShop #this assignes the name of the shop to the variable.
                print(f"You have chosen {QuantityofItem} SSD(s) from {ShopSelection}") #this tells the user how many SSDs they have bought from which shop.
                shopThree.NumCustomers = + 1 #this changes the customers by 1 everytime a purchase is made.
                shopThree.NumSales = QuantityofItem #this increases the number of sales by the amount the user purchases
                ctuStock.StockQuantity[2] -=  QuantityofItem #this changes the stock amount by the number of items bought.
            elif ShopSelection == 4: #this compares the user selection to a number.
                ShopSelection = shopFour.NameofShop #this assignes the name of the shop to the variable.
                print(f"You have chosen {QuantityofItem} SSD(s) from {ShopSelection}") #this tells the user how many SSDs they have bought from which shop.
                shopFour.NumCustomers = + 1 #this changes the customers by 1 everytime a purchase is made.
                shopFour.NumSales = QuantityofItem #this increases the number of sales by the amount the user purchases
                ctuStock.StockQuantity[2] -=  QuantityofItem #this changes the stock amount by the number of items bought.
            else: #this runs when the user selects an option that isn't one of the options.
                print("Invalid Selection") #this prints the string to tell the user that the selection was invalid.
            break  #this breaks the loop.
        else: #this runs when the user selects an option that isn't one of the options.
            print("Invalid Selection") #this prints the string to tell the user that the selection was invalid.
    elif UserSelMain == 3: #this compares the user selection to a number.
        while True: #this loops until borken.
            print(f"Returns \n\nWhat would you like to return?") #this prints the heading of the menu and the string.
            for ItemName,Price in ctuStock.SalesStockList.items(): #this for loop iterates through the dictionary but prints only the keys.
                print(ItemName) #this prints just the keys.
            UserReturn = int(input("Select an option: ")) #this asks the user to select an option and assigns it to the varaible. 
            ReturnsNum = int(input("How many are you returning? ")) #this asks the user how many they are returning and assigns it to the variable.
            if UserReturn == 1: #this compares the user selection to a number.
                ShopReturn = int(input(f"1. {shopOne.NameofShop}\n2. {shopTwo.NameofShop}\n3. {shopThree.NameofShop}\n4. {shopFour.NameofShop}\n0. Back\nSelect a shop: ")) #prints the list and asks the user and assigns asnwer to the variable.
                if ShopReturn == 1: #this compares the user selection to a number.
                        ShopReturn = shopOne.NameofShop #this assignes the name of the shop to the variable.
                        print(f"You are returning {ReturnsNum} Laptop(s) to {ShopReturn}") #this tells the user how many laptops they are returning to which shop.
                        shopOne.NumReturns += 1 #this increases the number of returns by the amount the user purchases
                        shopOne.NumSales -= ReturnsNum #this changes the sales number by the number of items returned.
                        ctuStock.StockQuantity[0] += ReturnsNum #this changes the stock amount by the number of returns.
                elif ShopReturn == 2: #this compares the user selection to a number.
                        ShopReturn = shopTwo.NameofShop #this assignes the name of the shop to the variable.
                        print(f"You are returning {ReturnsNum} Laptop(s) to {ShopReturn}") #this tells the user how many laptops they are returning to which shop.
                        shopTwo.NumReturns += 1 #this increases the number of returns by the amount the user purchases
                        shopTwo.NumSales -= ReturnsNum #this changes the sales number by the number of items returned.
                        ctuStock.StockQuantity[0] += ReturnsNum #this changes the stock amount by the number of returns.
                elif ShopReturn == 3: #this compares the user selection to a number.
                        ShopReturn = shopThree.NameofShop #this assignes the name of the shop to the variable.
                        print(f"You are returning {ReturnsNum} Laptop(s) to {ShopReturn}") #this tells the user how many laptops they are returning to which shop.
                        shopThree.NumReturns += 1 #this increases the number of returns by the amount the user purchases
                        shopThree.NumSales -= ReturnsNum #this changes the sales number by the number of items returned.
                        ctuStock.StockQuantity[0] += ReturnsNum #this changes the stock amount by the number of returns.
                elif ShopReturn == 4: #this compares the user selection to a number.
                        ShopReturn = shopFour.NameofShop #this assignes the name of the shop to the variable.
                        print(f"You are returning {QuantityofItem} Laptop(s) to {ShopReturn}") #this tells the user how many laptops they are returning to which shop.
                        shopFour.NumReturns += 1 #this increases the number of returns by the amount the user purchases
                        shopFour.NumSales -= ReturnsNum #this changes the sales number by the number of items returned.
                        ctuStock.StockQuantity[0] += ReturnsNum #this changes the stock amount by the number of returns.
                else: #this runs when the user selects an option that isn't one of the options.
                    print("Invalid Selection") #this prints the string to tell the user that the selection was invalid.
                break #this breaks the loop.
            elif UserReturn == 2:  #this compares the user selection to a number.
                 ShopReturn = int(input(f"1. {shopOne.NameofShop}\n2. {shopTwo.NameofShop}\n3. {shopThree.NameofShop}\n4. {shopFour.NameofShop}\n0. Back\nSelect a shop: ")) #prints the list and asks the user and assigns asnwer to the variable.
                 if ShopReturn == 1:  #this compares the user selection to a number.
                        ShopReturn = shopOne.NameofShop #this assignes the name of the shop to the variable.
                        print(f"You are returning {ReturnsNum} Mouse(s) to {ShopReturn}")  #this tells the user how many laptops they are returning to which shop.
                        shopOne.NumReturns += 1 #this increases the number of returns by the amount the user purchases
                        shopOne.NumSales -= ReturnsNum #this changes the sales number by the number of items returned.
                        ctuStock.StockQuantity[1] += ReturnsNum #this changes the stock amount by the number of returns.
                 elif ShopReturn == 2:  #this compares the user selection to a number.
                        ShopReturn = shopTwo.NameofShop #this assignes the name of the shop to the variable.
                        print(f"You are returning {ReturnsNum} Mouse(s) to {ShopReturn}")  #this tells the user how many laptops they are returning to which shop.
                        shopTwo.NumReturns += 1 #this increases the number of returns by the amount the user purchases
                        shopTwo.NumSales -= ReturnsNum #this changes the sales number by the number of items returned.
                        ctuStock.StockQuantity[1] += ReturnsNum #this changes the stock amount by the number of returns.
                 elif ShopReturn == 3:  #this compares the user selection to a number.
                        ShopReturn = shopThree.NameofShop #this assignes the name of the shop to the variable.
                        print(f"You are returning {ReturnsNum} Mouse(s) to {ShopReturn}")  #this tells the user how many laptops they are returning to which shop.
                        shopThree.NumReturns += 1 #this increases the number of returns by the amount the user purchases
                        shopThree.NumSales -= ReturnsNum #this changes the sales number by the number of items returned.
                        ctuStock.StockQuantity[1] += ReturnsNum #this changes the stock amount by the number of returns.
                 elif ShopReturn == 4:  #this compares the user selection to a number.
                        ShopReturn = shopFour.NameofShop #this assignes the name of the shop to the variable.
                        print(f"You are returning {QuantityofItem} Mouse(s) to {ShopReturn}")  #this tells the user how many laptops they are returning to which shop.
                        shopFour.NumReturns += 1 #this increases the number of returns by the amount the user purchases
                        shopFour.NumSales -= ReturnsNum #this changes the sales number by the number of items returned.
                        ctuStock.StockQuantity[1] += ReturnsNum #this changes the stock amount by the number of returns.
                 else: #this runs when the user selects an option that isn't one of the options.
                    print("Invalid Selection") #this prints the string to tell the user that the selection was invalid.
                 break #this breaks the loop.
            elif UserReturn == 3:  #this compares the user selection to a number.
                ShopReturn = int(input(f"1. {shopOne.NameofShop}\n2. {shopTwo.NameofShop}\n3. {shopThree.NameofShop}\n4. {shopFour.NameofShop}\n0. Back\nSelect a shop: ")) #prints the list and asks the user and assigns asnwer to the variable.
                if ShopReturn == 1: #this compares the user selection to a number.
                        ShopReturn = shopOne.NameofShop #this assignes the name of the shop to the variable.
                        print(f"You are returning {ReturnsNum} SSD(s) to {ShopReturn}") #this tells the user how many laptops they are returning to which shop.
                        shopOne.NumReturns += ReturnsNum #this increases the number of returns by the amount the user purchases
                        shopOne.NumSales -= ReturnsNum #this changes the sales number by the number of items returned.
                        ctuStock.StockQuantity[2] += ReturnsNum #this changes the stock amount by the number of returns.
                elif ShopReturn == 2: #this compares the user selection to a number.
                        ShopReturn = shopTwo.NameofShop #this assignes the name of the shop to the variable.
                        print(f"You are returning {ReturnsNum} SSD(s) to {ShopReturn}") #this tells the user how many laptops they are returning to which shop.
                        shopTwo.NumReturns += ReturnsNum #this increases the number of returns by the amount the user purchases
                        shopTwo.NumSales -= ReturnsNum #this changes the sales number by the number of items returned.
                        ctuStock.StockQuantity[2] += ReturnsNum #this changes the stock amount by the number of returns.
                elif ShopReturn == 3: #this compares the user selection to a number.
                        ShopReturn = shopThree.NameofShop #this assignes the name of the shop to the variable.
                        print(f"You are returning {ReturnsNum} SSD(s) to {ShopReturn}") #this tells the user how many laptops they are returning to which shop.
                        shopThree.NumReturns = ReturnsNum #this increases the number of returns by the amount the user purchases
                        shopThree.NumSales -= ReturnsNum #this changes the sales number by the number of items returned.
                        ctuStock.StockQuantity[2] += ReturnsNum #this changes the stock amount by the number of returns.
                elif ShopReturn == 4: #this compares the user selection to a number.
                        ShopReturn = shopFour.NameofShop #this assignes the name of the shop to the variable.
                        print(f"You are returning {QuantityofItem} SSD(s) to {ShopReturn}") #this tells the user how many laptops they are returning to which shop.
                        shopFour.NumReturns += ReturnsNum #this increases the number of returns by the amount the user purchases
                        shopFour.NumSales -= ReturnsNum #this changes the sales number by the number of items returned.
                        ctuStock.StockQuantity[2] += ReturnsNum #this changes the stock amount by the number of returns.
                else: #this runs when the user selects an option that isn't one of the options.
                    print("Invalid Selection") #this prints the string to tell the user that the selection was invalid.
                break #this breaks the loop and returns the user to the main menu.

    elif UserSelMain == 4: #this compares the user selection to a number.
        UserStockSel = int(input("Stock\n\n1. Display Stock\n2. Add stock\n0. Back\n\nSelect an option: ")) #this displays the menu and takes user input and assigns it to the variable.
        while True: #this loop will continue until broken
            if UserStockSel == 1: #this compares the user selection to a number.
                print("This is the current stock including price and quantity on hand.")
                ctuStock.Stocklist(1) #this calls the stocklist funtion from the class and passes an argument to the method.
                print(" ") #this prints a new line.
                break #this breaks the loop
            elif UserStockSel == 2: #this compares the user selection to a number.
                ItemAdd = input("Which item would you like to add: ") #this asks the user for the item they are adding.
                AddPrice = input(f"What is the Price of the {ItemAdd}: ") #this asks the user for the price of the item they are adding.
                AddQuantity = input(f"How many new {ItemAdd}(s) are there?") #This asks the user how many items they are adding.
                ctuStock.AddToStocklist(ItemAdd,AddPrice,AddQuantity) #this calls the add stock method and passes the three arguments to the function.
                break #this will break the loop.
            else: #this runs when the user selects an option that isn't one of the options.
                print("Invalid Selection")  #this prints the string to tell the user that the selection was invalid.
            break #this breaks the loop and returns the user to the main menu.
    elif UserSelMain == 99: #this compares the user selection to a number.
        break  #this breaks the loop

    else: #this runs when the user selects an option that isn't one of the options.
        print("Invalid Selection") #this prints the string to tell the user that the selection was invalid.