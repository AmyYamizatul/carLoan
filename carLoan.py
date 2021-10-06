st.header("Welcome to the RBA Car Loan Calculator.\n\n")

while True:

    totalAmount = st.write("Please enter the total amount")
    try:
        totalAmount = int(totalAmount)
        break

    except ValueError:
        st.write("Please enter a number")

# Part2 : Store the downPayment

while True:

    downPayment = st.write("Please enter the down payment")
    try:
        downPayment = int(downPayment)
        break
    
    except ValueError:
        st.write("Please enter a number")
    


# Part3 : Store the interestRate
# guna float sbb ada decimal point

while True:

    interestRate = st.write("Please enter the interest rate")
    try:
        interestRate = float(interestRate)
        break
    
    except ValueError:
        st.write("Please enter a number")
      
    
# Part4 : Store the loanPeriod

while True:

    loanPeriod = st.write("Please enter the loan period")
    try:
        loanPeriod = float(loanPeriod)
        break
    
    except ValueError:
        st.write("Please enter a number")
