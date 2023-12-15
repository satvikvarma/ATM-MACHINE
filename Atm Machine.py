print("welcome to Z bank")
pin = 8987
chances = 3
balance = 1000
while chances != 0:
    user_pin = int(input("Please enter the four digit pin"))
    if user_pin != pin:
        chances -= 1
        print("Wrong pin number")
        print(f"You have {chances} number chances left")
    else:
        user_choice = input("B : balance, D : deposit, W : withdraw")
        
        if user_choice == "B":
            print(f"Your total balance is {balance}")

        if user_choice == "D":
            deposit_user = int(input("Enter the amount that you would like to deposit: "))
            total_balance = deposit_user + balance
            print(F"You have deposited Rs.{deposit_user}")
            print(f"Your total balance is Rs.{total_balance}")

        if user_choice == "W":
            withdraw_user = int(input("Enter the amount you want to withdraw :"))
            total_balance = balance - withdraw_user
            print(f"you have withdrawn Rs.{total_balance}")
            print(f"Your total balance is Rs.{total_balance}")
            
    user_exit = input("Would you like to exit ? YES/NO:")
    if user_exit == "Yes":
        print("Thankyou for using Z bank !!")
        break
    else:
        continue

