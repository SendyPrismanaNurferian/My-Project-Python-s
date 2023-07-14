# THIS IS MY ATM IN PYTHON AND WILL BE UPDATE PATCH
#The programs is simple ATM and will be develop in future versions and this is my batch 1
while True:
    balance =1000000000 #first your account balance
    print ("    ATM JOMBLO     ") #You can change the name ATM
    print ("""
    1)      Balance
    2)      Deposit
    3)      Withdraw
    4)      Quit      
    """)
    try:
        Optiom=int(input("Enter Option: "))
    except Exception as e:
        print("ERROR:",e)
        print("Please enter option 1, 2, 3, or 4 only")
        continue
    if Optiom==1:
        print("Your Balance in Your Account is Rp", balance)
    if Optiom==2:
        print("Your Balance in Your Account is Rp", balance)
        Withdraw=float(input("Enter Withdraw amount Rp"))
        if Withdraw>0:
            forewardbalance=(balance-Withdraw)
            print("Foreward Balance Rp",forewardbalance)
        elif Withdraw>balance:
            print("No funds available for your account")
        else:
            print("None Withdraw Made")
    if Optiom==3:
        print("Your Balance in Your Account is Rp", balance)
        Deposit=float(input("Enter your Deposit Amount Rp"))
        if Deposit>0:
            forewardbalance=(balance + Deposit)
            print("Foreward Balance Rp",forewardbalance)
        else:
            print("No Deposit Made")
    if Optiom==4:
        exit()
