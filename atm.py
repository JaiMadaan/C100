class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 200000000")

    def withdrawl(self,amount):
        if amount <= 400:
            print("Money insufficient")
            
        else:
            new_amount = 200000000 - amount
            print("you have Withdraw amount "+str(amount) +"  . Your remaining balance is : "+ str(new_amount))

            
        

def main():
    Card_number = input("insert your card number:- ")
    pin_number  = input("enter your pin number:- ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("For Balance Enquriy press 1 ")
    print("For withdraw rupee press 2")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()