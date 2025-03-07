import HighlandsCafeClass as HCC
Table1 = HCC.table()
Table2 = HCC.table()
Table3 = HCC.table()
Table4 = HCC.table()
Table5 = HCC.table()
Table6 = HCC.table()
Logins = {}
Avaltables = ["1. Table 1","2. Table 2","3. Table 3","4. Table 4","5. Table 5","6. Table 6" ]
Usedtabs = []
OrderItems = []
ItemsPrices = []
itemAmounts= []
with open("Login.txt") as logfile:
    for entry in logfile:
        uname, upass = entry.split(",")
        Logins[uname] = int(upass)
Stocklist = {}
with open("Stock.txt") as Stock:
    for item in Stock:
        items, price = item.split(",")
        Stocklist[items] = int(price)


def InputError(question):
    while True:
        try:
            Uinput = int(input(question))
        except:
            print("Please use numbers only.")
        else:
            return Uinput
            
    

def login():
    enterpassword = "Please enter password:"
    print("\nUser Login\n")
    UName = input("Please enter username:").capitalize()
    UPass = InputError(enterpassword)
    return UName,UPass
def AuthCheck(UName,UPass):
    if UName in Logins.keys():
        Userpass = Logins.get(Uname)
        if UPass == Userpass:
            return True
        else:
            print("Incorrect Password. Please login again")
    else:
        print("Username not found. Please try again.")
def Assigntable(num):
    
    Usedtabs.append(str(num) + ". Table " + str(num))
    try:
        Avaltables.remove(str(num) + ". Table "+ str(num))
    except:
        print("This table is not avaliable.")
        return False
    print(f"Table successfully assigned to {Uname} ")
    addcus = input("Would you like to add customers to the table? y/n:")
    if addcus == 'y':
        for tabs in Usedtabs:
            print(tabs)
        tabsel = int(input("Select table to assign customers to or 0 to exit:"))
        return tabsel
    elif addcus == 'n':
        return False

def AddCustotable(tabsel):
    NumCus = "How many customers are seated at the table?"
    while True:
        if tabsel == 1:
            if "1. Table 1" in Usedtabs:               
                    Cusnums = InputError(NumCus)
                    Table1.NumofCus(Cusnums)
                    break
            else:
                print("You are not assigned to this table.")
                break
        elif tabsel == 2:
            if "2. Table 2" in Usedtabs:
                Cusnums = InputError(NumCus)
                Table2.NumofCus(Cusnums)
                break
            else:
                print("You are not assigned to this table.")
                break
        elif tabsel == 3:
            if "3. Table 3" in Usedtabs:
                Cusnums = InputError(NumCus)
                Table3.NumofCus(Cusnums)
                break
            else:
                print("You are not assigned to this table.")
                break
        elif tabsel == 4:
            if "4. Table 4" in Usedtabs:
                Cusnums = InputError(NumCus)
                Table4.NumofCus(Cusnums)
                break
            else:
                print("You are not assigned to this table.")
                break
        elif tabsel == 5:
            if "5. Table 5" in Usedtabs:
                Cusnums = InputError(NumCus)
                Table5.NumofCus(Cusnums)
                break
            else:
                print("You are not assigned to this table.")
                break

        elif tabsel == 6:
            if "6. Table 6" in Usedtabs:
                Cusnums = InputError(NumCus)
                Table6.NumofCus(Cusnums)
                break
            else:
                print("You are not assigned to this table.")
                break
        elif tabsel == False:
            print("")
            break
        else:
            print("Please try again.")
            break


while True:
    while True:
        print("Welcome to Highlands Cafe\n\n1.Login\n2.Exit")
        try:
            LChoice = int(input())
        except:
            print("Please use a number to select.")
        else:
            break
    if LChoice == 1:
            Uname,Upass = login()
            Usercheck= AuthCheck(Uname,Upass)
            if Usercheck == True:
                while True:
                    while True:
                        try:
                            Mainsel = int(input(f"\nWelcome {Uname}\nWhat would you like to do today?\n\n1.Assign Table\n2.Change Customers\n3.Add to Order\n4.Prepare Bill\n5.Complete Sale\n6.Cash up\n0.Log Out\n"))
                        except:
                            print("Please use a number to select.")
                        else:
                            break

                    if Mainsel == 1:
                        while True:
                            print("\nPlease select one of the avaliable tables or press 0 to exit\n\n")
                            for tabname in Avaltables:
                                print(tabname)
                                
                            while True:
                                try:
                                    Tabopt = int(input())
                                except:
                                    print("Please use a number to select.")
                                else:
                                    break
                            if Tabopt == 1:
                                tabsel = Assigntable(Tabopt)
                                if tabsel == False:
                                    break
                                else:
                                    AddCustotable(tabsel)
                                    break
                                
                            elif Tabopt == 2:
                                tabsel = Assigntable(Tabopt)
                                if tabsel == False:
                                    break
                                else:
                                    AddCustotable(tabsel)
                                    break

                            elif Tabopt == 3:
                                tabsel = Assigntable(Tabopt)
                                if tabsel == False:
                                    break
                                else:
                                    AddCustotable(tabsel)
                                    break
                            elif Tabopt == 4:
                                tabsel = Assigntable(Tabopt)
                                if tabsel == False:
                                    break
                                else:
                                    AddCustotable(tabsel)
                                    break
                            elif Tabopt == 5:
                                tabsel = Assigntable(Tabopt)
                                if tabsel == False:
                                    break
                                else:
                                    AddCustotable(tabsel)
                                    break
                            elif Tabopt == 6:
                                tabsel = Assigntable(Tabopt)
                                if tabsel == False:
                                    break
                                else:
                                    AddCustotable(tabsel)
                                    break
                            elif Tabopt == 0:
                                break
                            else:
                                print("Invalid selection.")

                    elif Mainsel == 2:
                        while True:                           
                            if Usedtabs == []:
                                print("No tables assigned. Please assign tables first.")
                                break
                            else:
                                for tabname in Usedtabs:
                                    print(tabname)
                                print("Please select one of the avaliable tables or press 0 to exit")
                                
                                while True:
                                    try:
                                        tabsel = int(input())
                                    except:
                                        print("Please use a number to select.")
                                    else:
                                        break
                                if tabsel == 1:
                                    AddCustotable(tabsel)
                                    break                              
                                elif tabsel == 2:
                                    AddCustotable(tabsel)
                                    break
                                elif tabsel == 3:
                                    AddCustotable(tabsel)
                                    break
                                elif tabsel == 4:
                                    AddCustotable(tabsel)
                                    break
                                elif tabsel == 5:
                                    AddCustotable(tabsel)
                                    break
                                elif tabsel == 6:
                                    AddCustotable(tabsel)
                                    break                
                                elif Tabopt == 0:
                                    break
                    elif Mainsel == 3:
                         
                         tabselQ = "Please select one of the avaliable tables or press 0 to exit "
                         itemselQ = "Select an item from the list to add to order: "
                         itemamount = 'How many item do you want to add? '
                         
                         while True:
                            if Usedtabs == []:
                                    print("No tables assigned. Please assign tables first.")
                                    break
                            else:
                                    for tabname in Usedtabs:
                                        print(tabname)
                            tabopt = InputError(tabselQ)
                            itemnum = 1
                            for Item,Price in Stocklist.items():
                                print(f"{itemnum}. {Item} R {Price}")
                                itemnum += 1
                            itemsel = InputError(itemselQ)
                            if itemsel == 1:
                                itemcoke = list(Stocklist.keys())[0]
                                Table1.orderitems.append(itemcoke)
                                itemprice = list(Stocklist.values())[0]
                                ItemsPrices.append(itemprice)
                                amoitem = InputError(itemamount)
                                itemAmounts.append(amoitem)
                            elif itemsel == 2:
                                itemfanta = list(Stocklist.keys())[1]
                                OrderItems.append(itemfanta)
                                itemprice = list(Stocklist.values())[1]
                                ItemsPrices.append(itemprice)
                                amoitem = InputError(itemamount)
                                itemAmounts.append(amoitem)
                            elif itemsel == 3:
                                itemSprite = list(Stocklist.keys())[2]
                                OrderItems.append(itemSprite)
                                itemprice = list(Stocklist.values())[2]
                                ItemsPrices.append(itemprice)
                                amoitem = InputError(itemamount)
                                itemAmounts.append(amoitem)
                            elif itemsel == 4:
                                itemGarS = list(Stocklist.keys())[3]
                                OrderItems.append(itemGarS)
                                itemprice = list(Stocklist.values())[3]
                                ItemsPrices.append(itemprice)
                                amoitem = InputError(itemamount)
                                itemAmounts.append(amoitem)
                            elif itemsel == 5:
                                itemcal = list(Stocklist.keys())[4]
                                OrderItems.append(itemcal)
                                itemprice = list(Stocklist.values())[4]
                                ItemsPrices.append(itemprice)
                                amoitem = InputError(itemamount)
                                itemAmounts.append(amoitem)
                            elif itemsel == 6:
                                itemwings = list(Stocklist.keys())[5]
                                OrderItems.append(itemwings)
                                itemprice = list(Stocklist.values())[5]
                                ItemsPrices.append(itemprice)
                                amoitem = InputError(itemamount)
                                itemAmounts.append(amoitem)
                            elif itemsel == 7:
                                itemsteak = list(Stocklist.keys())[6]
                                OrderItems.append(itemsteak)
                                itemprice = list(Stocklist.values())[6]
                                ItemsPrices.append(itemprice)
                                amoitem = InputError(itemamount)
                                itemAmounts.append(amoitem)
                            elif itemsel == 8:
                                itemchic = list(Stocklist.keys())[7]
                                OrderItems.append(itemchic)
                                itemprice = list(Stocklist.values())[7]
                                ItemsPrices.append(itemprice)
                                amoitem = InputError(itemamount)
                                itemAmounts.append(amoitem)
                            elif itemsel == 9:
                                itempork = list(Stocklist.keys())[8]
                                OrderItems.append(itempork)
                                itemprice = list(Stocklist.values())[8]
                                ItemsPrices.append(itemprice)
                                amoitem = InputError(itemamount)
                                itemAmounts.append(amoitem)
                            elif itemsel == 10:
                                itemice = list(Stocklist.keys())[9]
                                OrderItems.append(itemice)
                                itemprice = list(Stocklist.values())[9]
                                ItemsPrices.append(itemprice)
                                amoitem = InputError(itemamount)
                                itemAmounts.append(amoitem)
                            elif itemsel == 11:
                                itemwaf = list(Stocklist.keys())[10]
                                OrderItems.append(itemwaf)
                                itemprice = list(Stocklist.values())[10]
                                ItemsPrices.append(itemprice)
                                amoitem = InputError(itemamount)
                                itemAmounts.append(amoitem)
                            elif itemsel == 12:
                                itemcake = list(Stocklist.keys())[11]
                                OrderItems.append(itemcake)
                                itemprice = list(Stocklist.values())[11]
                                ItemsPrices.append(itemprice)
                                amoitem = InputError(itemamount)
                                itemAmounts.append(amoitem)
                            else:
                                print("invalid selection.")
                                break
                            Addagain = input("Add another item? y/n: ")
                            if Addagain == 'y':
                                itemsel = 0
                                pass
                            elif Addagain == 'n':
                                break

                    elif Mainsel == 4:
                        print(f"{OrderItems},\n{ItemsPrices},\n{itemAmounts}")
                    elif Mainsel == 5:
                        pass
                    elif Mainsel == 6:
                        pass
                    elif Mainsel == 0:
                        break
                    else:
                        print("Invalid Selection. Please try again.")

    elif LChoice == 2:
        break
    else:
        print("Invalid selection! Please try again.")
