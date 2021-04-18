budgetDict = [{
    "category": "Food",
    "amount": 0,
}, {
    "category": "Clothing",
    "amount": 0,
}, {
    "category": "Entertainment",
    "amount": 0,
}]


class Budget:

    def __init__(self):
        pass

    def deposit(self):
        print("Budget Options")
        print("1. Food")
        print("2. Clothing")
        print("3. Entertainment")
        print("4. Exit")
        selectedbudget = int(input("Select your budget \n"))

        if selectedbudget == 1:
            print("FOOD BALANCE: ", budgetDict[0]["amount"])
            dq = int(input("Do you want to deposit to Food balance? 1(Yes) 2(No) \n"))
            if dq == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budgetDict[0]["amount"] + deposit
                budgetDict[0]["amount"] = budgetDict[0]["amount"] + deposit
                print("NEW BALANCE: ", budgetDict[0]["amount"])
                wq = int(input("Do you want to  1(Transfer) 2(Withdraw) 3(Quit)\n"))
                if wq == 2:
                    self.withdrawfromBudget()

                elif wq == 1:
                    self.transfer()

                elif wq == 3:
                    exit()
                else:
                    print("Have a Nice Day!!")

            else:
                print("invalid Selection\nSELECT A VALID OPTION")
                self.deposit()




        elif selectedbudget == 2:
            print("CLOTHING BALANCE: ", budgetDict[1]["amount"])
            dq = int(input("Do you want to Deposit to Clothing balance? 1(Yes) 2(No) \n"))
            if dq == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budgetDict[1]["amount"] + deposit
                budgetDict[1]["amount"] = budgetDict[1]["amount"] + deposit
                print("NEW BALANCE: ", budgetDict[1]["amount"])
                wq = int(input("Do you want to  1(Transfer) 2(Withdraw) 3(Quit)\n"))
                if wq == 2:
                    self.withdrawfromBudget()

                elif wq == 1:
                    self.transfer()

                elif wq == 3:
                    exit()
                else:
                    print("Have a Nice Day!!")


            else:
                print("Invalid Selection\nSELECT A VALID OPTION")
                self.deposit()



        elif selectedbudget == 3:
            print("ENTERTAINMENT BALANCE: ", budgetDict[2]["amount"])
            dq = int(input("Do you want to deposit to Entertainment balance? 1(Yes) 2(No) \n"))
            if dq == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budgetDict[2]["amount"] + deposit
                budgetDict[2]["amount"] = budgetDict[1]["amount"] + deposit
                print("NEW BALANCE: ", budgetDict[2]["amount"])
                wq = int(input("Do you want to  1(Transfer) 2(Withdraw) 3(quit)\n"))
                if wq == 2:
                    self.withdrawfromBudget()

                elif wq == 1:
                    self.transfer()

                elif wq == 3:
                    exit()
                else:
                    print("Have a Nice Day!!")


            else:
                print("Invalid Selection\nSELECT A VALID OPTION")
                self.deposit()

        elif selectedbudget == 4:
            print("Have a nice day!!!")
            exit()


        else:
            print("Have a Nice Day")

    def withdrawfromBudget(self):
        print(budgetDict)
        print("Withdrawal Options")
        print("1. Food")
        print("2. Clothing")
        print("3. Entertainment")
        print("4. Exit")
        selectedbudgetOption = int(input("Select withdraw Options \n"))

        if selectedbudgetOption == 1:
            print("FOOD BALANCE: ", budgetDict[0]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budgetDict[0]["amount"]:
                print("Insufficient Funds")
                wq = int(input("Would you like to return home 1(Yes), 2(No)"))
                if wq == 1:
                    self.deposit()
                else:
                    print("Have a nice day")
                    exit()

            else:
                withdraw1 = budgetDict[0]["amount"] - withdraw
                budgetDict[0]["amount"] = budgetDict[0]["amount"] - withdraw
                print("Withdrawal Successful")
                print("FOOD NEW BALANCE: ", budgetDict[0]["amount"])
                wq = int(input("Would you like to return home 1(Yes), 2(No)"))
                if wq == 1:
                    self.deposit()
                else:
                    print("Have a nice day")
                    exit()

        elif selectedbudgetOption == 2:
            print("CLOTHING BALANCE: ", budgetDict[1]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budgetDict[1]["amount"]:
                print("Insufficient Funds")
                wq = int(input("Would you like to return home 1(Yes), 2(No)"))
                if wq == 1:
                    self.deposit()
                else:
                    print("Have a nice day!!")
                    exit()

            else:
                withdraw1 = budgetDict[1]["amount"] - withdraw
                budgetDict[1]["amount"] = budgetDict[1]["amount"] - withdraw
                print("Withdrawal Successful")
                print("CLOTHING NEW BALANCE: ", budgetDict[1]["amount"])
                wq = int(input("Would you like to return home 1(Yes), 2(No)"))
                if wq == 1:
                    self.deposit()
                else:
                    print("Have a nice day")
                    exit()

        elif selectedbudgetOption == 3:
            print("ENTERTAINMENT BALANCE: ", budgetDict[2]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budgetDict[2]["amount"]:
                print("Insufficient Funds")
                wq = int(input("Would you like to return home 1(Yes), 2(No)"))
                if wq == 1:
                    self.deposit()
                else:
                    print("Have a nice day")
                    exit()

            else:
                withdraw1 = budgetDict[2]["amount"] - withdraw
                budgetDict[2]["amount"] = budgetDict[2]["amount"] - withdraw
                print("Withdrawal Successful")
                print("ENTERTAINMENT NEW BALANCE: ", budgetDict[2]["amount"])
                wq = int(input("Would you like to return home 1(Yes), 2(No)"))
                if wq == 1:
                    self.deposit()
                else:
                    print("Have a nice day")
                    exit()

        elif selectedbudgetOption == 4:
            print("Have a nice day!!!")
            exit()

        else:
            print("Invalid Selection\nSELECT A VALID OPTION")
            self.deposit()

    def transfer(self):
        print(budgetDict)
        print("Transfer Options")
        print("1.From  Food")
        print("2.From Clothing")
        print("3.From Entertainment")
        print("4. Exit")

        if selectTFoption == 1:
            print("FOOD BALANCE: ", budgetDict[0]["amount"])
            tf = int(input("1.(To Clothing)\n 2.(To Entertainment)\n"))
            if tf == 1:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budgetDict[0]["amount"]:
                    tfamount1 = budgetDict[0]["amount"] - tfamount
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] - tfamount
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] + tfamount
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW FOOD BALANCE: ", budgetDict[0]["amount"])
                    print("NEW CLOTHING BALANCE: ", budgetDict[1]["amount"])
                    aq = int(input("Do you want to transfer again? 1(Yes) 2(No)\n"))
                    if aq == 1:
                        self.transfer()
                    else:
                        print("Have a nice day!!")
                        exit()
                else:
                    print("Insufficient funds")
                    print("FOOD BALANCE: ", budgetDict[0]["amount"])
                    self.deposit()

            elif tf == 2:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budgetDict[0]["amount"]:
                    tfamount1 = budgetDict[0]["amount"] - tfamount
                    tfamount2 = budgetDict[2]["amount"] + tfamount
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] - tfamount
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] + tfamount
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW FOOD BALANCE: ", budgetDict[0]["amount"])
                    print("NEW ENTERTAINMENT BALANCE: ", budgetDict[2]["amount"])
                    aq = int(input("Do you want to transfer again? 1(Yes) 2(No)\n"))
                    if aq == 1:
                        self.transfer()
                    else:
                        print("Have a nice day!!")
                        exit()

                else:
                    print("Insufficient funds")
                    print("FOOD BALANCE: ", budgetDict[0]["amount"])
                    self.deposit()

        elif selectTFoption == 2:
            print("CLOTHING BALANCE: ", budgetDict[1]["amount"])
            tf = int(input("1.(To Entertainment), 2.(To Food)\n"))
            if tf == 1:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budgetDict[1]["amount"]:
                    tfamount1 = budgetDict[1]["amount"] - tfamount
                    tfamount2 = budgetDict[2]["amount"] + tfamount
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] - tfamount
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] + tfamount
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW CLOTHING BALANCE: ", budgetDict[1]["amount"])
                    print("NEW ENTERTAINMENT BALANCE: ", budgetDict[2]["amount"])
                    aq = int(input("Do you want to transfer again? 1(Yes) 2(No)\n"))
                    if aq == 1:
                        self.transfer()

                    else:
                        print("Have a nice day!!")
                        exit()
                else:
                    print("Insufficient funds")
                    print("FOOD BALANCE: ", budgetDict[0]["amount"])
                    self.deposit()

            elif tf == 2:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budgetDict[1]["amount"]:
                    tfamount1 = budgetDict[1]["amount"] - tfamount
                    tfamount2 = budgetDict[0]["amount"] + tfamount
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] - tfamount
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] + tfamount
                    tfamount2 = budgetDict[0]["amount"] + tfamount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW CLOTHING BALANCE: ", budgetDict[1]["amount"])
                    print("NEW FOOD BALANCE: ", budgetDict[0]["amount"])
                    aq = int(input("Do you wan to transfer again? 1(Yes) 2(No)\n"))
                    if aq == 1:
                        self.transfer()
                    else:
                        print("Have a nice day!!")
                        exit()

                else:
                    print("Insufficient funds")
                    print("CLOTHING BALANCE: ", budgetDict[1]["amount"])
                    self.deposit()

        elif selectTFoption == 3:
            print("ENTERTAINMENT BALANCE: ", budgetDict[2]["amount"])
            tf = int(input("1.(To clothing), 2.(To Food)\n"))
            if tf == 1:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budgetDict[2]["amount"]:
                    tfamount1 = budgetDict[2]["amount"] - tfamount
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] - tfamount
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] + tfamount
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW ENTERTAINMENT BALANCE: ", budgetDict[2]["amount"])
                    print("NEW CLOTHING BALANCE: ", budgetDict[1]["amount"])
                    aq = int(input("Do you want to transfer again? 1(Yes) 2(No)\n"))
                    if aq == 1:
                        self.transfer()
                    else:
                        print("Have a nice day!!")
                        exit()

                else:
                    print("Insufficient funds")
                    print("FOOD BALANCE: ", budgetDict[0]["amount"])
                    self.deposit()

            elif tf == 2:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budgetDict[2]["amount"]:
                    tfamount1 = budgetDict[2]["amount"] - tfamount
                    tfamount2 = budgetDict[0]["amount"] + tfamount
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] - tfamount
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] + tfamount
                    tfamount2 = budgetDict[0]["amount"] + tfamount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW ENTERTAINMENT BALANCE: ", budgetDict[2]["amount"])
                    print("NEW FOOD BALANCE: ", budgetDict[0]["amount"])
                    aq = int(input("Do you want to transfer again? 1(Yes) 2(No)\n"))
                    if aq == 1:
                        self.transfer()
                    else:
                        print("Have a nice day!!")
                        exit()

                else:
                    print("Insufficient funds")
                    print("CLOTHING BALANCE: ", budgetDict[1]["amount"])
                    self.deposit()

        elif selectTFoption == 4:
            print("Have a nice day!!!")
            exit()

        else:
            print("Have a nice day!!!")


transaction = Budget()
transaction.deposit()
