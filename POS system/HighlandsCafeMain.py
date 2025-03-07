import sys #this imports the sys module for to change the output of the print()
import HighlandsCafeClass as HCC #this imports the class to make objects
Table1 = HCC.table()#this makes the object called Table1
Table2 = HCC.table()#this makes the object called Table2
Table3 = HCC.table()#this makes the object called Table3
Table4 = HCC.table()#this makes the object called Table4
Table5 = HCC.table()#this makes the object called Table5
Table6 = HCC.table()#this makes the object called Table6
Table1.tablename = "1. Table 1"#this gives Table1 the specific name
Table2.tablename = "2. Table 2"#this gives Table2 the specific name
Table3.tablename = "3. Table 3"#this gives Table3 the specific name
Table4.tablename = "4. Table 4"#this gives Table4 the specific name
Table5.tablename = "5. Table 5"#this gives Table5 the specific name
Table6.tablename = "6. Table 6"#this gives Table6 the specific name
Logins = {} #this is an empty dictionary to save all the usernames and passwords
Avaltables = {Table1:Table1.tablename,Table2:Table2.tablename,Table3:Table3.tablename,Table4:Table4.tablename,Table5:Table5.tablename,Table6:Table6.tablename}#this is the dictionary of avaliable tables.
Usedtabs = {} #this dictionary is for the used tables
OrderItems = [] #list for order items for list
ItemsPrices = [] #list for items total price for list
itemAmounts= []#list for totalamount items for list
DailyTotal = 0 #Total for the day
with open("Login.txt") as logfile: #this opens the file and assigns it an alias
    for entry in logfile: #for loop to add contents of file to list
        uname, upass = entry.split(",")#splits the entry into username and password and assings to the variables.
        Logins[uname] = int(upass) #this assigns the vraibles to the dictionary
Stocklist = {} #dictionay for the stocklist to be written too.
with open("Stock.txt") as Stock:  #this opens the file and assigns it an alias
    for item in Stock: #for loop to add contents of file to list
        items, price = item.split(",") #splits the entry into items and price and assings to the variables.
        Stocklist[items] = int(price) #writes the items and prices to a dictionary.



def InputError(question):#this function test for int input error takes the question as argument to allow for asking the same question over and over.
    while True: #loops until the correct input is inserted
        try: #tests the code to see if it will run without errors
            Uinput = int(input(question)) #this is the code that the try statement will test.
        except: #this code will run if the input is problematic.
            print("Please use numbers only.") #if the code failes then it prints the text.
        else:#if the code runs correctly this will run
            return Uinput #this returns the correct input.
            
    

def login(): #this function asks the user for their username and password
    enterpassword = "Please enter password:" #this assigns the question to the variable
    print("\nUser Login\n") #prints the string
    UName = input("Please enter username:").capitalize()#this gets the username and capitalizes the word entered
    UPass = InputError(enterpassword) #this calls the inputerror function and pass the return to the variable.
    return UName,UPass #returns the user name and password
def AuthCheck(UName,UPass): #this function authorises access or not.
    if UName in Logins.keys():#this test if the username is in the keys of the dictionary
        Userpass = Logins.get(Uname)#this assigns the value of the key to the variable
        if UPass == Userpass:#this compares the varaible to the user inputted password.
            return True #this returns a true value if the two are equal
        else:#this runs if the two are not equal
            print("Incorrect Password. Please login again")#this prints if the two are not equal
    else:#this runs if the username is not in the keys list
        print("Username not found. Please try again.")#this prints if the username is not in the keys list
def Assigntable(num):#this function assigns the tables to the specific waiters
    if num == 1:# this checks if the user selection is equal to 1
        if Table1 in Avaltables: #this checks if table 1 is avaliable for assignment
            Avaltables.pop(Table1) #if it is avaliable it is removed from the avaliable tables
            Usedtabs[Table1] = Table1.tablename #table1 is assigned to the used table list
            print(f"Table 1 successfully assigned to {Uname}") #this prints to that the user can gets confimation of the change.
            addcus = input("Would you like to add customers to the table? y/n:")#asks the user if they want to add customers to the table.
            if addcus == 'y':#this checks what the user is 
                for tabs in Usedtabs:#this loop loops though the used tables and prints it
                    print(Usedtabs.get(tabs))
                tabsel = int(input("Select table to assign customers to or 0 to exit:"))#this asks the user to chose the table
                return tabsel #this returns the user selection
            elif addcus == 'n':#this checks what the user is 
                return False#this returns false
            else:#this will run if user selects an option
                print("Invalid Option.")#this prints the string
                return False #this returns false
            
        else:
            print("Table Not avaliable")
    elif num == 2:
        if Table2 in Avaltables:
            Avaltables.pop(Table2)
            Usedtabs[Table2] = Table2.tablename
            print(f"Table 2 successfully assigned to {Uname}")
            addcus = input("Would you like to add customers to the table? y/n:")
            if addcus == 'y':
                for tabs in Usedtabs:
                    print(Usedtabs.get(tabs))
                tabsel = int(input("Select table to assign customers to or 0 to exit:"))
                return tabsel
            elif addcus == 'n':
                return False
            else:
                print("Invalid Option.")
                return False
        else:
            print("Table Not avaliable")
    elif num == 3:
        if Table3 in Avaltables:
            Avaltables.pop(Table3)
            Usedtabs[Table3] = Table3.tablename
            print(f"Table 3 successfully assigned to {Uname}")
            addcus = input("Would you like to add customers to the table? y/n:")
            if addcus == 'y':
                for tabs in Usedtabs:
                    print(Usedtabs.get(tabs))
                tabsel = int(input("Select table to assign customers to or 0 to exit:"))
                return tabsel
            elif addcus == 'n':
                return False
            else:
                print("Invalid Option.")
                return False
        else:
            print("Table Not avaliable")
    elif num == 4:
        if Table4 in Avaltables:
            Avaltables.pop(Table4)
            Usedtabs[Table4] = Table4.tablename
            print(f"Table 4 successfully assigned to {Uname}")
            addcus = input("Would you like to add customers to the table? y/n:")
            if addcus == 'y':
                for tabs in Usedtabs:
                    print(Usedtabs.get(tabs))
                tabsel = int(input("Select table to assign customers to or 0 to exit:"))
                return tabsel
            elif addcus == 'n':
                return False
            else:
                print("Invalid Option.")
                return False
        else:
            print("Table Not avaliable")
    elif num == 5:
        if Table5 in Avaltables:
            Avaltables.pop(Table5)
            Usedtabs[Table5] = Table5.tablename
            print(f"Table 5 successfully assigned to {Uname}")
            addcus = input("Would you like to add customers to the table? y/n:")
            if addcus == 'y':
                for tabs in Usedtabs:
                    print(Usedtabs.get(tabs))
                tabsel = int(input("Select table to assign customers to or 0 to exit:"))
                return tabsel
            elif addcus == 'n':
                return False
            else:
                print("Invalid Option.")
                return False
        else:
            print("Table Not avaliable")
    elif num == 6:
        if Table6 in Avaltables:
            Avaltables.pop(Table6)
            Usedtabs[Table6] = Table6.tablename
            print(f"Table 6 successfully assigned to {Uname}")
            addcus = input("Would you like to add customers to the table? y/n:")
            if addcus == 'y':
                for tabs in Usedtabs:
                    print(Usedtabs.get(tabs))
                tabsel = int(input("Select table to assign customers to or 0 to exit:"))
                return tabsel
            elif addcus == 'n':
                return False
            else:
                print("Invalid Option.")
                return False
        else:
            print("Table Not avaliable")
        return num

def AddCustotable(tabsel):#this adds customers to specific tables.
    NumCus = "How many customers are seated at the table?"#this assigns the question to the variable for errorinput
    while True: #this loops until false
        if tabsel == 1: #if the table select is equal to 1
            if Table1 in Usedtabs: #this check if the table is in the used tables           
                    Cusnums = InputError(NumCus)#this calls the function and passes the num of customers
                    Table1.NumofCus(Cusnums)#assigns the value of the customers to the object attributes
                    break#this breaks the loop.
            else:#this uns if the first if fails
                print("You are not assigned to this table.")#this prints the string
                break
        elif tabsel == 2:#if the table select is equal to 2           
            if Table2 in Usedtabs:#this check if the table is in the used tables
                Cusnums = InputError(NumCus) #this calls the function and passes the num of customers
                Table2.NumofCus(Cusnums) #assigns the value of the customers to the object attributes
                break
            else:
                print("You are not assigned to this table.")#this prints the string
                break
        elif tabsel == 3: #if the table select is equal to 3
            if Table3 in Usedtabs:#this check if the table is in the used tables
                Cusnums = InputError(NumCus)#this calls the function and passes the num of customers
                Table3.NumofCus(Cusnums)#assigns the value of the customers to the object attributes
                break
            else:
                print("You are not assigned to this table.")#this prints the string
                break
        elif tabsel == 4:#if the table select is equal to 4
            if Table4 in Usedtabs:#this check if the table is in the used tables
                Cusnums = InputError(NumCus)#this calls the function and passes the num of customers
                Table4.NumofCus(Cusnums)#assigns the value of the customers to the object attributes
                break
            else:
                print("You are not assigned to this table.")#this prints the string
                break
        elif tabsel == 5:#if the table select is equal to 5
            if Table5 in Usedtabs:#this check if the table is in the used tables
                Cusnums = InputError(NumCus)#this calls the function and passes the num of customers
                Table5.NumofCus(Cusnums)#assigns the value of the customers to the object attributes
                break
            else:
                print("You are not assigned to this table.")#this prints the string
                break

        elif tabsel == 6:#if the table select is equal to 6
            if Table6 in Usedtabs:#this check if the table is in the used tables
                Cusnums = InputError(NumCus)#this calls the function and passes the num of customers
                Table6.NumofCus(Cusnums)#assigns the value of the customers to the object attributes
                break
            else:
                print("You are not assigned to this table.")#this prints the string
                break
        elif tabsel == False:#if the table select is equal to False
            print("") #this prints the string
            break
        else:#this runs if the user selects a wrong option.
            print("Please try again.") #this prints the string
            break


while True:#thisloops unitl broken
    while True:#thisloops unitl broken
        print("Welcome to Highlands Cafe\n\n1.Login\n2.Exit")#this prints the login menu
        try:#this function test for int input error 
            LChoice = int(input())#this is the code to test
        except:#this will run if the code fails
            print("Please use a number to select.")
        else:
            break
    if LChoice == 1:#this checks if the user is logining in or not
            Uname,Upass = login()#calls the login function and assigns the returns
            Usercheck= AuthCheck(Uname,Upass)#this calls the function to check if the user is allowed.
            if Usercheck == True:#this checks if the user is allowed or not.
                while True:#thisloops unitl broken
                    while True:#thisloops unitl broken
                        try:#this will test for error input for integer values.
                            Mainsel = int(input(f"\nWelcome {Uname}\nWhat would you like to do today?\n\n1.Assign Table\n2.Change Customers\n3.Add to Order\n4.Prepare Bill\n5.Complete Sale\n6.Cash up\n0.Log Out\n"))
                        except:
                            print("Please use a number to select.")
                        else:
                            break

                    if Mainsel == 1:#this is if user wants to assign a table.
                        while True:
                            print("\nPlease select one of the avaliable tables or press 0 to exit\n\n")
                            for tabname in Avaltables: #this loops to print the tables avaliable for the user.
                                print(Avaltables.get(tabname))
                                
                            while True:#tests for input error
                                try:
                                    Tabopt = int(input())
                                except:
                                    print("Please use a number to select.")
                                else:
                                    break
                            if Tabopt == 1:#this checks for possible table assignment
                                tabsel = Assigntable(Tabopt)#this assigns the return to the variable
                                if tabsel == False:#if the variable is false or not
                                    break
                                else:
                                    AddCustotable(tabsel)#this allows the user to enter the customer numbers.
                                    break
                                
                            elif Tabopt == 2:#this checks for possible table assignment
                                tabsel = Assigntable(Tabopt)#this assigns the return to the variable
                                if tabsel == False:#if the variable is false or not
                                    break
                                else:
                                    AddCustotable(tabsel)#this allows the user to enter the customer numbers.
                                    break

                            elif Tabopt == 3:#this checks for possible table assignment
                                tabsel = Assigntable(Tabopt)#this assigns the return to the variable
                                if tabsel == False:#if the variable is false or not
                                    break
                                else:
                                    AddCustotable(tabsel)#this allows the user to enter the customer numbers.
                                    break
                            elif Tabopt == 4:#this checks for possible table assignment
                                tabsel = Assigntable(Tabopt)#this assigns the return to the variable
                                if tabsel == False:#if the variable is false or not
                                    break
                                else:
                                    AddCustotable(tabsel)#this allows the user to enter the customer numbers.
                                    break
                            elif Tabopt == 5:#this checks for possible table assignment
                                tabsel = Assigntable(Tabopt)#this assigns the return to the variable
                                if tabsel == False:#if the variable is false or not
                                    break
                                else:
                                    AddCustotable(tabsel)#this allows the user to enter the customer numbers.
                                    break
                            elif Tabopt == 6:#this checks for possible table assignment
                                tabsel = Assigntable(Tabopt)#this assigns the return to the variable
                                if tabsel == False:#if the variable is false or not
                                    break
                                else:
                                    AddCustotable(tabsel)#this allows the user to enter the customer numbers.
                                    break
                            elif Tabopt == 0:#this is to break out of the list
                                break
                            else:
                                print("Invalid selection.")#this is for an input error

                    elif Mainsel == 2:#this is for adding customers for the tables
                        while True:                           
                            if Usedtabs == {}:#this tests if the list is empty or not.
                                print("No tables assigned. Please assign tables first.")#this tells the user that no tables are avaliable.
                                break
                            else:
                                for tabname in Usedtabs:#loops to print the avaliable tables
                                    print(Usedtabs.get(tabname))
                                print("Please select one of the avaliable tables or press 0 to exit")#asks user to select an option
                                
                                while True:
                                    try:#test for inputerror
                                        tabsel = int(input())
                                    except:
                                        print("Please use a number to select.")
                                    else:
                                        break
                                if tabsel == 1:#user selection comparision
                                    AddCustotable(tabsel)#calls the addcustomer function and passes the variable to it.
                                    break                              
                                elif tabsel == 2:#user selection comparision
                                    AddCustotable(tabsel)#calls the addcustomer function and passes the variable to it.
                                    break
                                elif tabsel == 3:#user selection comparision
                                    AddCustotable(tabsel)#calls the addcustomer function and passes the variable to it.
                                    break
                                elif tabsel == 4:#user selection comparision
                                    AddCustotable(tabsel)#calls the addcustomer function and passes the variable to it.
                                    break
                                elif tabsel == 5:#user selection comparision
                                    AddCustotable(tabsel)#calls the addcustomer function and passes the variable to it.
                                    break
                                elif tabsel == 6:#user selection comparision
                                    AddCustotable(tabsel)#calls the addcustomer function and passes the variable to it.
                                    break                
                                elif Tabopt == 0:#user selection comparision
                                    break
                    elif Mainsel == 3:#this is for adding order items to the tables
                        billtot = []#list for all the bills totals
                        Billcomplete = False#tells that the bil
                        tabselQ = "Please select one of the avaliable tables or press 0 to exit "#adds question to variale for input error checking.
                        itemselQ = "Select an item from the list to add to order: "#adds question to variale for input error checking.
                        itemamount = 'How many item do you want to add? '#adds question to variale for input error checking.
                        
                        while True:
                            if Usedtabs == {}:#this checks if tables have been assigned or not.
                                    print("No tables assigned. Please assign tables first.")
                                    break
                            else:
                                    for tabname in Usedtabs:#this loop prints all the avalaible tables.
                                        print(Usedtabs.get(tabname))
                            tabopt = InputError(tabselQ)#this calls function and passes the question to it and assigns the output to the variable.
                            if tabopt == 1:#if the user selection is 1 then assigns table1 to table choice.
                                if Table1 in Usedtabs:#checks if the table is avaliable to that waiter
                                    tablechoice = Table1
                                else:
                                    print("You are not assigned to this table.")#prints if the table is not assigned to them.
                                    break
                            elif tabopt == 2:#if the user selection is 1 then assigns table1 to table choice.
                                if Table2 in Usedtabs:#checks if the table is avaliable to that waiter
                                    tablechoice = Table2
                                else:
                                    print("You are not assigned to this table.")#prints if the table is not assigned to them.
                                    break
                            elif tabopt == 3:#if the user selection is 1 then assigns table1 to table choice.
                                if Table3 in Usedtabs:#checks if the table is avaliable to that waiter
                                    tablechoice = Table3
                                else:
                                    print("You are not assigned to this table.")#prints if the table is not assigned to them.
                                    break
                            elif tabopt == 4:#if the user selection is 1 then assigns table1 to table choice.
                                if Table4 in Usedtabs:#checks if the table is avaliable to that waiter
                                    tablechoice = Table4
                                else:
                                    print("You are not assigned to this table.")#prints if the table is not assigned to them.
                                    break
                            elif tabopt == 5:#if the user selection is 1 then assigns table1 to table choice.
                                if Table5 in Usedtabs:#checks if the table is avaliable to that waiter
                                    tablechoice = Table5
                                else:
                                    print("You are not assigned to this table.")#prints if the table is not assigned to them.
                                    break
                            elif tabopt == 6:#if the user selection is 1 then assigns table1 to table choice.
                                if Table6 in Usedtabs:#checks if the table is avaliable to that waiter
                                    tablechoice = Table6
                                else:
                                    print("You are not assigned to this table.")#prints if the table is not assigned to them.
                                    break
                            else:
                                print("Invalid Selection")#prints of the user makes an invalid selection.
                                break    
                            itemnum = 1#this allows itemnum to be used in the loop for itteration purposes.
                            for Item,Price in Stocklist.items():#this loop prints the stock items from the stock dictionary.
                                print(f"{itemnum}. {Item} R {Price}")
                                itemnum += 1 #this adds one to the total of itemnum is increased for itteration purposes.
                            itemsel = InputError(itemselQ)#calls the fucntion and passes the question to it.
                            if itemsel == 1:
                                itemcoke = list(Stocklist.keys())[0]#this calls the key from the dictionary and assigns it to the variable.
                                tablechoice.orderitems.append(itemcoke)#this appends the item to the attribute of the chosen table.
                                amoitem = InputError(itemamount)#calls inputerror and assigns return to varaible.
                                tablechoice.quantities.append(amoitem)#appends the returned value to the attribute list.
                                itemprice = list(Stocklist.values())[0]#this calls the dictionary value and assigns to varaible
                                totprice = itemprice * amoitem#this multiplies amount items by item price assings value to variable
                                tablechoice.prices.append(totprice)#assigns total price to list
                                billtot.append(totprice)#assigns total price to list.



                            elif itemsel == 2:#this does the same as if statment just for each different item in stock list
                                itemfanta = list(Stocklist.keys())[1]
                                tablechoice.orderitems.append(itemfanta)
                                amoitem = InputError(itemamount)
                                tablechoice.quantities.append(amoitem)
                                itemprice = list(Stocklist.values())[1]
                                totprice = itemprice * amoitem
                                tablechoice.prices.append(totprice)
                                billtot.append(totprice)

                            elif itemsel == 3:#this does the same as if statment just for each different item in stock list
                                itemSprite = list(Stocklist.keys())[2]
                                tablechoice.orderitems.append(itemSprite)
                                amoitem = InputError(itemamount)
                                tablechoice.quantities.append(amoitem)
                                itemprice = list(Stocklist.values())[2]
                                totprice = itemprice * amoitem
                                tablechoice.prices.append(totprice)
                                billtot.append(totprice)

                            elif itemsel == 4:#this does the same as if statment just for each different item in stock list
                                itemGsn = list(Stocklist.keys())[3]
                                tablechoice.orderitems.append(itemGsn)
                                amoitem = InputError(itemamount)
                                tablechoice.quantities.append(amoitem)
                                itemprice = list(Stocklist.values())[3]
                                totprice = itemprice * amoitem
                                tablechoice.prices.append(totprice)
                                billtot.append(totprice)

                            elif itemsel == 5:#this does the same as if statment just for each different item in stock list
                                itemCala = list(Stocklist.keys())[4]
                                tablechoice.orderitems.append(itemCala)
                                amoitem = InputError(itemamount)
                                tablechoice.quantities.append(amoitem)
                                itemprice = list(Stocklist.values())[4]
                                totprice = itemprice * amoitem
                                tablechoice.prices.append(totprice)
                                billtot.append(totprice)

                            elif itemsel == 6:#this does the same as if statment just for each different item in stock list
                                itemWing = list(Stocklist.keys())[5]
                                tablechoice.orderitems.append(itemWing)
                                amoitem = InputError(itemamount)
                                tablechoice.quantities.append(amoitem)
                                itemprice = list(Stocklist.values())[5]
                                totprice = itemprice * amoitem
                                tablechoice.prices.append(totprice)
                                billtot.append(totprice)

                            elif itemsel == 7:#this does the same as if statment just for each different item in stock list
                                itemSteak = list(Stocklist.keys())[6]
                                tablechoice.orderitems.append(itemSteak)
                                amoitem = InputError(itemamount)
                                tablechoice.quantities.append(amoitem)
                                itemprice = list(Stocklist.values())[6]
                                totprice = itemprice * amoitem
                                tablechoice.prices.append(totprice)
                                billtot.append(totprice)

                            elif itemsel == 8:#this does the same as if statment just for each different item in stock list
                                itemChic = list(Stocklist.keys())[7]
                                tablechoice.orderitems.append(itemChic)
                                amoitem = InputError(itemamount)
                                tablechoice.quantities.append(amoitem)
                                itemprice = list(Stocklist.values())[7]
                                totprice = itemprice * amoitem
                                tablechoice.prices.append(totprice)
                                billtot.append(totprice)

                            elif itemsel == 9:#this does the same as if statment just for each different item in stock list
                                itemPork = list(Stocklist.keys())[8]
                                tablechoice.orderitems.append(itemPork)
                                amoitem = InputError(itemamount)
                                tablechoice.quantities.append(amoitem)
                                itemprice = list(Stocklist.values())[8]
                                totprice = itemprice * amoitem
                                tablechoice.prices.append(totprice)
                                billtot.append(totprice)

                            elif itemsel == 10:#this does the same as if statment just for each different item in stock list
                                itemIce = list(Stocklist.keys())[9]
                                tablechoice.orderitems.append(itemIce)
                                amoitem = InputError(itemamount)
                                tablechoice.quantities.append(amoitem)
                                itemprice = list(Stocklist.values())[9]
                                totprice = itemprice * amoitem
                                tablechoice.prices.append(totprice)
                                billtot.append(totprice)
                            elif itemsel == 11:#this does the same as if statment just for each different item in stock list
                                itemWaf = list(Stocklist.keys())[10]
                                tablechoice.orderitems.append(itemWaf)
                                amoitem = InputError(itemamount)
                                tablechoice.quantities.append(amoitem)
                                itemprice = list(Stocklist.values())[10]
                                totprice = itemprice * amoitem
                                tablechoice.prices.append(totprice)
                                billtot.append(totprice)

                            elif itemsel == 12:#this does the same as if statment just for each different item in stock list
                                itemCake = list(Stocklist.keys())[11]
                                tablechoice.orderitems.append(itemCake)
                                amoitem = InputError(itemamount)
                                tablechoice.quantities.append(amoitem)
                                itemprice = list(Stocklist.values())[1]
                                totprice = itemprice * amoitem
                                tablechoice.prices.append(totprice)
                                billtot.append(totprice)
                            else:#Error handling for wrong item selection
                                print("Invalid selection.")
                                break
                            Addagain = input("Add another item? y/n: ")#asks user to add another item.
                            if Addagain == 'y':
                                itemsel = 0 #this resets item selection so that you can select the number again.
                                pass
                            elif Addagain == 'n':#this breaks the loop if the user does not want to add more items to the order.
                                break

                    elif Mainsel == 4: #this is to prepare the bill for printing
                        Pitem = "Item"#adds the string to the varaible for printing
                        Pquant = "Quantity" #adds the string to the varaible for printing
                        Pprice = "Price"#adds the string to the varaible for printing
                        while True:
                            if Usedtabs == {}:#this checks if tables have been assigned
                                    print("No tables assigned. Please assign tables first.")
                                    break
                            else:
                                    print("Select a table:")
                                    for tabname in Usedtabs:#prints the list of assigned the tables to this user
                                        print(Usedtabs.get(tabname))
                            tabopt = InputError(tabselQ)#calls the errorinput check and assigns the return
                            if tabopt == 1:
                                if Table1 in Usedtabs:#this checks if table one is in the assigned tables dictionary.
                                    tablechoice = Table1#this assigns table one to table choice for later use.
                                else:
                                    print("You are not assigned to this table.")#this prints if the table is not assigned to the user.
                                    break
                            elif tabopt == 2:#this does the same as the first if but assigns the different tables.
                                if Table2 in Usedtabs:
                                    tablechoice = Table2
                                else:
                                    print("You are not assigned to this table.")
                                    break
                            elif tabopt == 3: #this does the same as the first if but assigns the different tables.
                                if Table3 in Usedtabs:
                                    tablechoice = Table3
                                else:
                                    print("You are not assigned to this table.")
                                    break
                            elif tabopt == 4:#this does the same as the first if but assigns the different tables.
                                if Table4 in Usedtabs:
                                    tablechoice = Table4
                                else:
                                    print("You are not assigned to this table.")
                                    break
                            elif tabopt == 5:#this does the same as the first if but assigns the different tables.
                                if Table5 in Usedtabs:
                                    tablechoice = Table5
                                else:
                                    print("You are not assigned to this table.")
                                    break
                            elif tabopt == 6:#this does the same as the first if but assigns the different tables.
                                if Table6 in Usedtabs:
                                    tablechoice = Table6
                                else:
                                    print("You are not assigned to this table.")
                                    break
                            elif tabopt == 0:#this breaks the loop if user selects 0
                                break        
                                
                            else:#will run if user selects an invalid option.
                                print("Invalid Selection")
                                break
                            Gtot = 0#this is for the grandtotal for the day.
                            for item in tablechoice.prices:#this loops through the prices list to total for the day.
                                Gtot += item #adds the items to the total for the day.

                            print(f"------------------------------------------------------------\n\
The bill for {tablechoice.tablename}\n{Pitem:>20}{Pquant:^20}{Pprice:>10}") #this prints the column titles and the start of the bill.
                            for item,quant,price in zip(tablechoice.orderitems,tablechoice.quantities,tablechoice.prices):
                                print(f"{item:>20}{quant:^20}R{price:>9}")#this prints from all the list to print the bill.
                            print(f"The total for your order is: R{Gtot} \n\nYou were helped by {Uname}\n----------------------------------------------------------\n")#this prints the end of the bill
                            Billcomplete = True #this is so that it can be tested to see if the bill has been completed.
                            input("Bill has been printed. \nPress Enter to Continue")
                            break

                    elif Mainsel == 5:#this is to complete avaliable sales.
                        if Billcomplete == False:#this checks if the bill has been processed yet.
                            print("Bill has not been prepared. Please prepare bill first.")
                        else:#this runs if the bill has been prepared already
                            print("Select a table:")
                            for tabname in Usedtabs:#this prints the avaliable tables list.
                                    print(Usedtabs.get(tabname))
                            tabopt = InputError(tabselQ)
                            if tabopt == 1:#this is to assign the table choice to the variable tablechoice
                                if Table1 in Usedtabs:
                                    tablechoice = Table1
                                else:
                                    print("You are not assigned to this table.")
                                    break
                            elif tabopt == 2:#this does the same as the first if just assigns the specific table
                                if Table2 in Usedtabs:
                                    tablechoice = Table2
                                else:
                                    print("You are not assigned to this table.")
                                    break
                            elif tabopt == 3:#this does the same as the first if just assigns the specific table
                                if Table3 in Usedtabs:
                                    tablechoice = Table3
                                else:
                                    print("You are not assigned to this table.")
                                    break
                            elif tabopt == 4:#this does the same as the first if just assigns the specific table
                                if Table4 in Usedtabs:
                                    tablechoice = Table4
                                else:
                                    print("You are not assigned to this table.")
                                    break
                            elif tabopt == 5:#this does the same as the first if just assigns the specific table
                                if Table5 in Usedtabs:
                                    tablechoice = Table5
                                else:
                                    print("You are not assigned to this table.")
                                    break
                            elif tabopt == 6:#this does the same as the first if just assigns the specific table
                                if Table6 in Usedtabs:
                                    tablechoice = Table6
                                else:
                                    print("You are not assigned to this table.")
                                    break
                            elif tabopt == 0:#this will break the loop if the user selects 0
                                break        
                                
                            else:#this is for error handling of incorrect user input
                                print("Invalid Selection")
                                break
                            original_output = sys.stdout #assigns the standard out to the variable
                            NewFilename = input("Please provide a name for this bill: ") #assigns the userinput to the variable
                            NewFilename += ".txt" #this adds the file extention to the users input
                            with open(NewFilename,"+w") as B: #this opens or creates the file and assigns an alias
                                sys.stdout = B #this sets the print functions output to the file name
                                print(f"------------------------------------------------------------\n\
The bill for {tablechoice.tablename}\n{Pitem:>20}{Pquant:^20}{Pprice:>10}") #this prints the bill to the list.
                                for item,quant,price in zip(tablechoice.orderitems,tablechoice.quantities,tablechoice.prices):
                                    print(f"{item:>20}{quant:^20}R{price:>9}")
                                print(f"The total for your order is: R{Gtot} \n\nYou were helped by {Uname}\n--------------------------------------------------------------\n")
                            sys.stdout = original_output #this changes the output back to the original.
                            DailyTotal += Gtot #this adds the bill totals to the daily totals
                            tablechoice.orderitems.clear #this clears the order items list.
                            tablechoice.quantities.clear #this clears the quantities list.
                            tablechoice.prices.clear #this clears the prices list.
                            UnTable = list(Usedtabs.keys()) #this changes the keys of the dictionary to the list.
                            UnName = list(Usedtabs.values()) #this changes the values of the dictionary to the list.
                            for tabspec, tabname in zip(UnTable, UnName): #this loop puts the assigned tables back into the avaliable
                                Avaltables[tabspec] = tabname
                            Usedtabs.clear()#this clears the usedtables dictionary.


                    elif Mainsel == 6:
                        print(f"Today we made R{DailyTotal}.") #this tells the user how much they made on the day.
                        truncday = input("Would you like to clear todays total? y/n: ") #this is to clear the days totals.
                        if truncday == 'y':
                            DailyTotal = 0 #this sets the dailytotal back to 0
                    elif Mainsel == 0:#this breaks the loop if the user selects 0
                        break
                    else:#this will print if the user selection is invalid.
                        print("Invalid Selection. Please try again.")

    elif LChoice == 2:#this closes the program 
        break
    else:#this is for error handling.
        print("Invalid selection! Please try again.")
