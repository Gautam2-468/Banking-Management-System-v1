from datetime import datetime 
import random
import json

class Account():
    def __init__(self,balance,account_number,password):
        self.balance=balance
        self.account_number=account_number
        self.password=password
        self.load_balance()
        self.load_password()
    
    def verify_password(self):
        entered = input("Enter password: ")
        if entered == self.password:
            return True
        else:
            return False
        
    def Change_password(self):
        current_password = input("Enter Current password : ")
        if current_password == self.password:
            self.password = input("Enter new password: ")
            self.save_password()
            print("Password successfully changed")
        else:
            print("Password incorrect please try again") 

    def load_password(self):
        with open("password.txt","r")as f:
            data = f.read().strip()
            if data:
             self.password = data 

    def save_password(self):
        with open("password.txt","w")as f:
            f.write(self.password)

    
    def load_balance(self):
        with open("balance.txt","r")as f:
            data = f.read() 
            self.balance = float(data)
            print("loading balance.....")

    def save_balance(self):
        with open("balance.txt","w")as f:
             f.write(str(self.balance))

    def transcation_history(self,message):
        with open("History.txt","a")as f:
            current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            f.write(str(current_time)+"   "+ message +"\n")
            print('Transaction History Saved.')
           
    def deposit(self,amount):
        if self.verify_password():
            self.balance+=amount
            print("Amount deposited:",amount)
            print("Deposited Successful.")
            print("New balance:",self.balance)
            self.save_balance()
            self.transcation_history(f"Deposited {amount}")
        else:
            print("Incorrect password. Deposit failed.")
    def withdraw(self,amount):
        if self.verify_password():
            if self.balance >= amount:
                self.balance -= amount
                print("Amount withdrawn:",amount)
                print("Withdraw successful.")
                print("Remaining balance:",self.balance)
                self.save_balance()
                self.transcation_history(f"Withdraw {amount}")
            else:
                print("Insufficient balance")
        else:
            print("Incorrect password. Withdrawal failed.")

    def display_balance(self):
        if self.verify_password():
            print("Current balance:",self.balance)
        else:            
            print("Incorrect password. Cannot display balance.")

    
acc1 = Account(1000, 12345, "123")
while True:
     print("1. Display Balance")
     print("2. Deposit")
     print("3. Withdraw")
     print("4. Transaction History")
     print("5. Change Password")
     print("6. Exit")
     choice = int(input("Enter your choice: "))
     if choice == 1:
        acc1 .display_balance()
     elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        acc1.deposit(amount)
     elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        acc1.withdraw(amount)
     elif choice == 4:
        if acc1.verify_password():
            with open("History.txt","r")as f:
                data = f.read()
                print(data)
     elif choice == 5:
        acc1.Change_password()
     elif choice == 6:
        break
     else:
        print("Invalid choice. Please try again.")
