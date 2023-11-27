import math

while True:
    # presenting user with choice and asking them to select
    print("investment \t- to calculate the amount of interest you'll earn on your investment")
    print("bond   \t\t- to calculate the amount you'll have to pay on a home loan")

    selection = input("Enter either 'investment' or 'bond' from the meny above to proceed: ").lower()

    # if they select investment they are asked for more data for calculation
    if selection == 'investment':
        while True:
            try:
                initial_deposit = float(input("What is the amount of money you are depositing? "))
                interest_rate = float(input("What is the interest rate? "))
                years_investing = int(input("How long are you planning on investing (in years)? "))
        
            # asking user if the want simple or compound calculation and running the relevant calculation
                interest = input("Do you want the 'simple' or 'compound' interest? ")
                if interest == 'simple':
                    total_amount = initial_deposit *(1 + (interest_rate / 100) * years_investing)
                    print(round(total_amount, 2))
                elif interest == 'compound':
                    total_amount = initial_deposit * math.pow((1+interest_rate / 100),years_investing)
                    print(round(total_amount, 2))
        
            # catching a scenario where user enter wrong input
                else:
                    print("Invalid interest type. Please enter 'simple' or 'compound'.")
                    continue
            except ValueError: # preventing wrong input error
                print("Invalid input. Please enter a numerical value.")
            break
        
    # if user selects bond asking for the relevant information and running the calculation
    elif selection == 'bond':
        while True:
            try:
                house_value = int(input("What is the present value of the house? "))
                interest_rate_bond = float(input("What is the interest rate? "))
                repayment_length = int(input("In how many months are you planning to repay the bond? "))
                total_amount_bond = (((interest_rate_bond / 100) / 12) * house_value) / (1 - (1 + (interest_rate_bond / 100) / 12)**(-repayment_length))
                print(round(total_amount_bond, 2))
                break
            except ValueError: # preventing wrong input error
                print("Invalid input. Please enter a numerical value.")

    # catching a scenario where user enter wrong input
    else:
        print("Invalid selection. Please enter 'investment' or 'bond'.")
        continue
    
    # if the calculation is successful, exit the loop
    break 