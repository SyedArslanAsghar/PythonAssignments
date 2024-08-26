class Accounts:


    accountCategory = ["Current", "Saving"]
    Customer = {
        1357: {
            "id": 0,
            "accountTitle": "Syed Arslan",
            "accountCategory": accountCategory[0],
            "balance": 1000,
            "pin": 1357,
            "isActive": "no"
        },
        1234: {
            "id": 1,
            "accountTitle": "Zeeshan Arif",
            "accountCategory": accountCategory[1],
            "balance": 100000,
            "pin": 1357,
            "isActive": "yes"
        }
    }

    # @staticmethod
    def activate(pin):
        if pin in Accounts.Customer:
            Accounts.Customer[pin]["isActive"] = "yes"
            print(f"Account with PIN {pin} is now active.")
        else:
            print("Invalid PIN. Cannot activate account.")
