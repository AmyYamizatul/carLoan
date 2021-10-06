print("Welcome to the RBA Car Loan Calculator.\n\n")

while True:

    totalAmount = input("Please enter the total amount")
    try:
        totalAmount = int(totalAmount)
        break

    except ValueError:
        print("\nPlease enter a number.")

# Part2 : Store the downPayment

while True:

    downPayment = input("Please enter the down payment.\n")
    try:
        downPayment = int(downPayment)
        break
    
    except ValueError:
        print("\nPlease enter a number.")
    


# Part3 : Store the interestRate
# guna float sbb ada decimal point

while True:

    interestRate = input("Please enter the interest rate.\n")
    try:
        interestRate = float(interestRate)
        break
    
    except ValueError:
        print("\nPlease enter a number.")
      
    
# Part4 : Store the loanPeriod

while True:

    loanPeriod = input("Please enter the loan period.\n")
    try:
        loanPeriod = float(loanPeriod)
        break
    
    except ValueError:
        print("\nPlease enter a number.")
