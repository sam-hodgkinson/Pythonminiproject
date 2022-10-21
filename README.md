Program allows 20 account holders to access their specific account balance, savings, investment and total balance
The first step presents an input for the customer to enter their unique account number (key) allowing access to their details. If the account does not exist, they customer is prompted to try again.
The following steps presents an input to determine the service they require. Again if an invalid response is given the customer is prompted to try again.
When selecting the desired service they information is presented before an option to exit the program is given.
If the customer does not select 'Yes' to exit, they return to the input for service selection. However, if they select 'Yes' a small message is presented and they leave
The code employs various conditional operators and if/elif statements are used for the while loops to ensure the conditions are true to examine 20 accounts and 4 variables with
To further develop this, password protection could be employed to ensure better security of each account when accessing through account numbers. An additional prompt following the account number to authenticate the user. A limit could be set on the attempts, through the use of iterations, so 5 attempts before leaving the program
e.g.
password = "password1"
attempt = ''
count = 0
while counter < 5
    counter += 1
    attempt = input("Please enter your password")
    if attempt == password:
        print(Correct!)
        break
else:
    print("Password incorrect. Try again.")