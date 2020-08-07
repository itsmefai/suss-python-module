# Done by Muhammad Al-Fairuz Bin Mohd Baser J2010990

class BonusCalculator:
    """
    A class used to represent Standard Chartered's Bonus$aver Calculator

    ...

    Attributes
    ----------

    amount : float
        the interest amount to be added to the current total

    Methods
    -------
    add_interest(amount)
        adds in the interest to the current total based on the input amount

    show_total()
        prints out the total dollar value and interest amount
    
    insert_balance()
        assigns the user input balance to the class variable balance

    choice()
        prints out the user interface for "spending" category and will continuously loop till a valid input is provided. Converts input choice to int and returns the value

    salary_credit()
        prints out the user interface for "salary credit" category and will continuously loop till a valid input is provided. Converts input choice to boolean and returns the value

    invest()
        prints out the user interface for "invest" category and will continuously loop till a valid input is provided. Converts input choice to boolean and returns the value

    insure()
        prints out the user interface for "insure" category and will continuously loop till a valid input is provided. Converts input choice to boolean and returns the value

    bill_payment()
        prints out the user interface for "bill payment" category and will continuously loop till a valid input is provided. Converts input choice to boolean and returns the value
    """

    def __init__(self):
        self.balance = 0
        self.current_interest = 0.05
        self.spend_interest = 0
        self.salary = 0
        self.investment = 0
        self.insurance = 0
        self.bill = 0

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

        print("SUMMARY")

        # calculating annual interest
        yr_amount = self.balance * (self.current_interest/100)

        # calculating monthly interest 
        month_amount = yr_amount / 12

        # calculating the breakdown
        from_base = self.balance * (0.05/100)
        from_spending = self.balance * (self.spend_interest/100)
        from_salary = self.balance * (self.salary/100)
        from_investment = self.balance * (self.investment/100)
        from_insurance = self.balance * (self.insurance/100)
        from_bill = self.balance * (self.bill/100)

        
        # using formated print to output the float results (2 significant figures)
        print(f'Your estimated annual interest:\t S${yr_amount:,.2f} @ {self.current_interest:.2f}% p.a.')
        print(f'Your estimated monthly interest: S${month_amount:,.2f} @ {self.current_interest:.2f}% p.a.')
        print()
        print("BREAKDOWN")
        print(f'Amount from Base Interest:\t S$ {from_base:,.2f} (0.05% interest)')
        print(f'Amount from Spending Interest:\t S$ {from_spending:,.2f} ({self.spend_interest:,.2f}% interest)')
        print(f'Amount from Salary Credit:\t S$ {from_salary:,.2f} ({self.salary:,.2f}% interest)')
        print(f'Amount from Investing:\t\t S$ {from_investment:,.2f} ({self.investment:,.2f}% interest)')
        print(f'Amount from Insurance:\t\t S$ {from_insurance:,.2f} ({self.insurance:,.2f}% interest)')
        print(f'Amount from Bill Payment:\t S$ {from_bill:,.2f} ({self.bill:,.2f}% interest)')

    def insert_balance(self):
        # A function to request for the user's balance

        # Loop until correct input is provided.
        while True:
            try:
                print()
                balance = float(input('Enter your estimated Bonuse$aver average daily balance: S$ '))
                print('----------------------------------------------')
                self.balance = balance
                break
            except:
                print()
                print('Invalid input. Please try again.')
                print()

    def choice(self):
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
                print()
            else:
                print('----------------------------------------------')
                return int(option)
        
    def salary_credit(self):
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
                print()
            else:
                print('----------------------------------------------')
                break
        
        if choice == '1':
            return True
        else:
            return False

    def invest(self):
        # A function for users to select a boolean option for invest 

        # Print out the user interface
        print('Would you invest in eligible products?')
        print("""
        (1) Yes
        (2) No
        """)

        # Loop till user inputs a valid option
        while True:
            choice = input('Option 1 or 2?: ')
            if choice not in ['1', '2']:
                print('Invalid Input. Please select again.')
                print()
            else:
                print('----------------------------------------------')
                break
        
        if choice == '1':
            return True
        else:
            return False

    def insure(self):
        # A function for users to select a boolean option for insure

        # Print out the user interface
        print('Would you insure in eligible products?')
        print("""
        (1) Yes
        (2) No
        """)

        # Loop till user inputs a valid option
        while True:
            choice = input('Option 1 or 2?: ')
            if choice not in ['1', '2']:
                print('Invalid Input. Please select again.')
                print()
            else:
                print('----------------------------------------------')
                break
        
        if choice == '1':
            return True
        else:
            return False

    def bill_payment(self):
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
                print()
            else:
                print('----------------------------------------------')
                break
        
        if choice == '1':
            return True
        else:
            return False    


def main():
    # The main user interface

    account = BonusCalculator()
    
    # ----- Step 1 (Specify Balance) ------
    balance = account.insert_balance()

    # ----- Step 2 (Spending Options) ------
    selection = account.choice()
    if selection == 1: # do nothing
        pass
    elif selection == 2: # add 0.25% interest rate
        account.add_interest(0.25)
        account.spend_interest = 0.25

    elif selection == 3: # add 0.75% interest rate
        account.add_interest(0.75)
        account.spend_interest = 0.75

    # ----- Step 3 (Salary Credit) ------
    # If Salary Credit is True, add 0.40% interest rate. Else, do nothing
    salary_credit_status = account.salary_credit()
    if salary_credit_status:
        account.add_interest(0.40)
        account.salary = 0.40

    # ----- Step 4 (Invest) ------    
     # If Invest is True, add 0.85% interest rate. Else, do nothing
    invest_status = account.invest()
    if invest_status:
        account.add_interest(0.85)
        account.investment = 0.85

    # ----- Step 5 (Insure) ------    
     # If Invest is True, add 0.85% interest rate. Else, do nothing
    insure_status = account.insure()
    if insure_status:
        account.add_interest(0.85)
        account.insurance = 0.85

    # ----- Step 6 (Bill Payment) ------    
     # If Invest is True, add 0.10% interest rate. Else, do nothing
    bill_status = account.bill_payment()
    if bill_status:
        account.add_interest(0.10)
        account.bill = 0.10

    # ----- Step 7 (Summary) ------ 
    account.show_total()
    print('----------------------------------------------')


if __name__ == "__main__": 
    main()
