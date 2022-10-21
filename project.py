account = {
    "1" : ["John", "100", "50", "14"],
    "2" : ["Sarah", "495", "10", "4"],
    "3" : ["Paul", "39", "273", "6"],
    "4" : ["Ryan", "390", "100", "-10"],
    "5" : ["Earl", "357", "209", "1"],
    "6" : ["Sally", "930", "100", "1"],
    "7" : ["Chloe", "25", "490", "-4"],
    "8" : ["Matt", "361", "267", "5"],
    "9" : ["Jane", "494", "123", "0"],
    "10" : ["Arthur", "456", "987", "9"],
    "11" : ["Oliver", "32", "100", "1"],
    "12" : ["Steph", "345", "25", "2"],
    "13" : ["Dave", "566", "134", "5"],
    "14" : ["Olivia", "574", "60", "2"],
    "15" : ["Hilary", "10", "50", "20"],
    "16" : ["Liam", "100", "80", "-30"],
    "17" : ["Steve", "103", "367", "3"],
    "18" : ["Emma", "499", "50", "5"],
    "19" : ["Gabby", "213", "105", "-9"],
    "20" : ["Tim", "492", "234", "7"]
}



for key in account:
    while (True):
       
        accountnumber = (input("What is your account number?\n"))
       
        if accountnumber not in account:
            print("Invalid account number. Please try again.")
       
        if accountnumber in account:
            print(f"Welcome back {account[key][0]}!")
            break
    
    while (True):
       
        service = input("\nWhich service would you like to use today: Account Balance, Savings, Investments or Total balance? \n")
       
        if service == "Account Balance" or service == "account balance" or service == "Account balance":
            print(f"{account[key][0]} your account balance is:\n{account[key][1]}")
        
            anotherservice = input("\nEnter 'Yes' if you would like to exit following this service?\n")
            
            if anotherservice == "No" or anotherservice == "no" or anotherservice == "exit" or anotherservice =="Exit":
                print("\nEnter another service you would like to use below:")

            if anotherservice == "yes" or anotherservice == "Yes":
                print("\nThank you for using our service today! :)")
                break
                   
    
        elif service == "Savings" or service == "savings" or service == "saving" or service == "Saving":
            print(f"{account[key][0]}, your account balance is:\n{account[key][2]}")
            

            anotherservice = input("\nEnter 'Yes' if you would like to exit following this service?\n")
            
            if anotherservice == "No" or anotherservice == "no" or anotherservice == "exit" or anotherservice =="Exit":
                print("\nEnter another service you would like to use below:")

            if anotherservice == "yes" or anotherservice == "Yes":
                print("\nThank you for using our service today! :)")
                break
            
       
        elif service == "investments" or service == "Investments" or service == "investment" or service == "Investment":
            print(f"\n{account[key][0]}, your annual portfolio % change is:\n{account[key][3]}%")
        
            anotherservice = input("\nEnter 'Yes' if you would like to exit following this service?\n")
            
            if anotherservice == "No" or anotherservice == "no" or anotherservice == "exit" or anotherservice =="Exit":
                print("\nEnter another service you would like to use below:")

            if anotherservice == "yes" or anotherservice == "Yes":
                print("\nThank you for using our service today! :)")
                break
            
            
        elif service == "total" or service == "Total" or service == "total balance" or service == "Total balance" or "Total Balance":
            print(f"{account[key][0]}, the total across your balance and savings is: £{account[key][0]}")
            
            anotherservice = input("\nEnter 'Yes' if you would like to exit following this service?\n")
            
            if anotherservice == "No" or anotherservice == "no" or anotherservice == "exit" or anotherservice =="Exit":
                print("\nEnter another service you would like to use below:")

            if anotherservice == "yes" or anotherservice == "Yes":
                print("\nThank you for using our service today! :)")
                break
            

        elif service == "none" or service == "None":
            print("\nThank you for using our service today! :)")
            break
        
    break


