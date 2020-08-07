class BonusCalculator:
    def __init__(self, balance):
        self.balance = balance
        self.current_interest = 0.05

    def add_interest(self, amount):
        """Add amount to current total interest rate

        Parameters:
            amount (float): The interest amount which is to be added to the current total interest
        """
        self.current_interest += amount

    def show_total(self):
        """Return the total interest dollar amount and current total interest rate

        Returns:
        output (str): formated print showing the dollar amount and total interest rate
        """

        # calculating annual interest and returning the value
        add_amount = self.balance * (self.current_interest/100)
        
        # using f-formating to print out the result
        print(f'S${add_amount:,.2f} @ {self.current_interest:.2f}% p.a.')


def insert_balance():
    # A function to request for the user's balance
    # Loop until correct input is provided.
    while True:
        try:
            balance = float(input('Balance: '))
            print()
            return balance
        except:
            print('Invalid input. Please try again.')
            print()

def choice():
    # A function to request for user's choice of card spending

    # Print out the user interface
    print('Select your estimated monthly card spending:')
    print("""
    (1) Less than S$500
    (2) S$500 to S$1,999
    (3) S$2,000 or greater
    """)

    # Loop till user inputs a valid option
    while True:
        option = input('Option 1, 2 or 3?: ')
        if option not in ['1', '2', '3']:
            print('Invalid Input. Please select again.')
        else:
            print()
            return int(option)
    
def salary_credit():
    # A function for users to select a boolean option for salary credit 

    # Print out the user interface
    print('Would your monthly salary credit be S$3,000 or more?')
    print("""
    (1) Yes
    (2) No
    """)

    # Loop till user inputs a valid option
    while True:
        choice = input('Option 1 or 2?: ')
        if choice not in ['1', '2']:
            print('Invalid Input. Please select again.')
        else:
            print()
            break
    
    if choice == '1':
        return True
    else:
        return False

def invest():
    # A function for users to select a boolean option for invest 

    # Print out the user interface
    print('Would you insure or invest in eligible products?')
    print("""
    (1) Yes
    (2) No
    """)

    # Loop till user inputs a valid option
    while True:
        choice = input('Option 1 or 2?: ')
        if choice not in ['1', '2']:
            print('Invalid Input. Please select again.')
        else:
            print()
            break
    
    if choice == '1':
        return True
    else:
        return False

def insure():
    # A function for users to select a boolean option for insure

    # Print out the user interface
    print('Would you insure or invest in eligible products?')
    print("""
    (1) Yes
    (2) No
    """)

    # Loop till user inputs a valid option
    while True:
        choice = input('Option 1 or 2?: ')
        if choice not in ['1', '2']:
            print('Invalid Input. Please select again.')
        else:
            print()
            break
    
    if choice == '1':
        return True
    else:
        return False

def bill_payment():
    # A function for users to select a boolean option for bill payment

    # Print out the user interface
    print('Would you make at least 3 bill payments online?')
    print("""
    (1) Yes
    (2) No
    """)

    # Loop till user inputs a valid option
    while True:
        choice = input('Option 1 or 2?: ')
        if choice not in ['1', '2']:
            print('Invalid Input. Please select again.')
        else:
            print()
            break
    
    if choice == '1':
        return True
    else:
        return False


def main():
    # The main user interface

    print("Enter your estimated Bonuse$aver average daily balance:")
    # balance = float(input())
    balance = insert_balance()

    # ----- Step 1 (Specify Balance) ------
    account = BonusCalculator(balance)

    # ----- Step 2 (Spending Options) ------
    selection = choice()
    if selection == 1: # do nothing
        pass
    elif selection == 2: # add 0.25% interest rate
        account.add_interest(0.25)
        print()

    elif selection == 3: # add 0.75% interest rate
        account.add_interest(0.75)
        print()

    # ----- Step 3 (Salary Credit) ------
    # If Salary Credit is True, add 0.40% interest rate. Else, do nothing
    salary_credit_status = salary_credit()
    if salary_credit_status:
        account.add_interest(0.40)

    # ----- Step 4 (Invest) ------    
     # If Invest is True, add 0.85% interest rate. Else, do nothing
    invest_status = invest()
    if invest_status:
        account.add_interest(0.85)

    # ----- Step 5 (Insure) ------    
     # If Invest is True, add 0.85% interest rate. Else, do nothing
    insure_status = insure()
    if insure_status:
        account.add_interest(0.85)

    # ----- Step 6 (Bill Payment) ------    
     # If Invest is True, add 0.10% interest rate. Else, do nothing
    bill_status = bill_payment()
    if bill_status:
        account.add_interest(0.10)


    print('Your estimated annual interest')
    account.show_total()
    print()
    

main()
