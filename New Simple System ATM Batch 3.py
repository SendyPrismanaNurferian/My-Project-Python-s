#After Im add the database account and the accouns is fake or this is not real you can rename the account patch 3
balance = 1000000000  #first your account balance
#Database account the other peoples (example)
accounts = {
    "123456789": {
        "name": "John Doe",
        "balance": 500000000
    },
    "987654321": {
        "name": "Jane Smith",
        "balance": 750000000
    }
}

while True:
    print("    ATM JOMBLO     ") #You can change the name ATM
    print("""
    1)      Balance
    2)      Deposit
    3)      Withdraw
    4)      Transfer
    5)      Quit      
    """)
    try:
        option = int(input("Enter Option: "))
    except Exception as e:
        print("ERROR:", e)
        print("Please enter option 1, 2, 3, 4, or 5 only")
        continue

    if option == 1:
        print("Your Balance in Your Account is Rp", balance)

    elif option == 2:
        print("Your Balance in Your Account is Rp", balance)
        deposit = float(input("Enter Deposit amount Rp"))
        if deposit > 0:
            balance += deposit
            print("Deposit successful")
        else:
            print("No Deposit Made")

    elif option == 3:
        print("Your Balance in Your Account is Rp", balance)
        withdraw = float(input("Enter Withdraw amount Rp"))
        if withdraw > 0:
            if withdraw <= balance:
                balance -= withdraw
                print("Withdraw successful")
            else:
                print("Insufficient funds in your account")
        else:
            print("No Withdraw Made")

    elif option == 4:
        print("Your Balance in Your Account is Rp", balance)
        transfer_amount = float(input("Enter Transfer amount Rp"))
        if transfer_amount > 0:
            transfer_account = input("Enter Account Number to Transfer: ")
            if transfer_account in accounts:
                password = input("Enter Password: ")
                if password == accounts[transfer_account]["password"]:
                    if transfer_amount <= balance:
                        balance -= transfer_amount
                        accounts[transfer_account]["balance"] += transfer_amount
                        print("Transfer successful")
                    else:
                        print("Insufficient funds in your account for transfer")
                else:
                    print("Incorrect password")
            else:
                print("Account not found")
        else:
            print("No Transfer Made")

    elif option == 5:
        exit()

    print("Latest Balance:", balance)
