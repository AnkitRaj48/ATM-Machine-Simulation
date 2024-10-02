import time 

print("Please insert your Card")

time.sleep(5)
password = 1234

pin = int(input("Please insert your Atm pin"))
balance = 5000

if pin == password:
    print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
            """)
    # while True:
try:
            option = int(input("Please insert your option"))
            if option == 1:
                print(f"Your current balance is {balance}")
            elif option == 2:
                withdraw_amount = int(input("Please insert your withdraw amount"))
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your current balance is {balance}")
            elif option == 3:
                deposit_amount = int(input("Please insert your deposit amount"))
                balance += deposit_amount
                print(f"{deposit_amount} is credited from your account")
                print(f"Your updated current balance is {balance}")
            elif option == 4:
                print("Transaction exited")
                #break
            else:
                print("Invalid option. Please try again.")
except ValueError:
            print("Please enter a valid option")
else:
    print("Wrong pin. Please try again.")
    