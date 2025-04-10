
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transact = []
    
    def deposit(self,amount, record_transaction = True):
        #added a record_transaction argument to this function, to choose if we want to append this transaction to self.transact
        if amount > 0:
            self.balance += amount #this is an easy way to apply a operator to a attribute, without needing to do "balance = balance + amount"
            if record_transaction == True:
                self.transact.append(f"Deposited:RM{amount}, Balance: RM{self.balance}")

        else:
            print("Please input a positive number")
            
    def withdraw(self,amount,record_transaction = True):
        if amount > 0:
            self.balance -= amount
            if record_transaction == True:
                self.transact.append(f"Withdraw:RM{amount}, Balance: RM{self.balance}")

        else:
            print("Insufficient Funds or Invalid Amount")


    def transfer(self,amount,recipient_account):
        if amount >0 and amount <= self.balance:
            self.withdraw(amount,False)
            recipient_account.deposit(amount,False)
            self.transact.append(f"Transferred: RM{amount} to {recipient_account.name}")
        else:
            print("Insufficient Funds or Invalid Format")



    def get_balance(self):
        print(f"{self.name} Account Balance: RM{self.balance}")


#using .join to "remove" the square brackets
#Concept: self.transact is current in square brackets, meaning it is a list
#.join CONCATENATES each element in the list, separated by a specified operator. In this case, we put " ", so it is just a blank space
#"\n" will join each element in the list by a \n, meaning each element will start in a newline
#the output of .join is a STRING
#strings can be printed without having the square braces
    def get_transact_history(self):
        print("\n".join(self.transact))


call1 = BankAccount("Calvin",0)
call2 = BankAccount("Mike",2000)

call1.deposit(5000,True)
call1.withdraw(2000,True)
call1.transfer(1000,call2)

call1.get_transact_history()
call1.get_balance()

