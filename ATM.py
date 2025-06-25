'''ask for pin
allow users to check their balance, deposit money, withdraw money
exit when the user selects exit option'''
'''ask user for pin
check balance
deposit money
withdraw money
let user exit'''
'''set balance as 10000
then ask user for options to enter: check balance, deposit money, withdraw money, or exit
if user picks exit:
break the code.


'''


def ATM():
    balance = 10000
    pin = "1234"
    userinput = input("Please enter your PIN:\n")

    if userinput == pin:
        print("Welcome to your account")

        while True:
            print("\nOptions:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            option = input("Please select an option (1,2,3,4): ")

            if option == "1":
                print(f"Your balance is: {balance}")
            elif option == "2":
                deposit = float(input("How much money would you like to deposit? "))
                balance += deposit
                print(f"Deposited. New balance is: {balance}")
            elif option == "3":
                withdraw = float(input("How much money would you like to withdraw? "))
                if withdraw > balance:
                    print("Insufficient funds. Please enter a valid amount.")
                else:
                    balance -= withdraw
                    print(f"Withdrawn. New balance is: {balance}")
            elif option == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Incorrect PIN. Access denied.")


ATM()
