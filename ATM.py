import Accounts as File
class ATM(File.Accounts):
    pin = ""
    attempts = 0

    def validate(self):
        self.attempts = self.attempts + 1
        try:
            self.pin = int(input("enter your 4 digit pin"))
        except ValueError:
            print("Pin Should be Integer")
    def hasAccount(self):
        available = 0
        self.validate()


        for key in File.Accounts.Customer.keys():
            if key == self.pin:
                available = 1

        if available == 1:
            if File.Accounts.Customer[self.pin]["isActive"] == "yes":
                self.mainManu()
            elif File.Accounts.Customer[self.pin]["isActive"] == "no":
                print("Activate your Account")
                File.Accounts.activate(self.pin)
                # self.mainMenu()
            else:
                print("Contact your bank or our help line 01100011100")
        else:
            # if the user enters wrong pin 3 time, he/she should not be allowed to proceed furthur.
            if self.attempts < 3:
                print("your pin is incorrect")
                self.hasAccount()
            else:

                print("You have entered wrong pin Excessively, contact you bank")


    def mainManu(self):

        print("1: Balance Inquiry")
        print("2: Cash Widrawl")
        opt = int(input("Enter the desire value:"))
        if opt == 1:
            self.balanceInquiry()
        elif opt == 2:
            self.cashWidhrwal()
        else:
            print("you have entered wrong value")
            self.mainManu()

    def balanceInquiry(self):
        print("your current balance is", File.Accounts.Customer[self.pin]["balance"])
        val = input("Would you like to another transation \n1: Yes\n2: no")
        if val == "1":
            self.mainManu()
        else:
            pass



    def cashWidhrwal(self):

        try:
            amount = int(input("Enter Amount"))
        except ValueError:
            print("The value should be numeric.")
            self.cashWidhrwal()
        if amount <= File.Accounts.Customer[self.pin]["balance"]:
            if amount%500==0:
                oldBalance = File.Accounts.Customer[self.pin]["balance"]
                newBalance = oldBalance - amount
                print("Thank you for using our bank \n Please collect your ammount", amount)
                File.Accounts.Customer[self.pin]["balance"] = newBalance

                self.balanceInquiry()
            else:
                print("Amount should be a multiple of 500 \nExample: 500, 1000, 1500")
                self.cashWidhrwal()
        else:
            print("You have insufficient balance. Please enter less amount")
            self.cashWidhrwal()

x = ATM()

# print("pin = ", x.pin)
x.hasAccount()