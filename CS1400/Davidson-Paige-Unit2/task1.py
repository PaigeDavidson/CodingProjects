# Paige Davidson
# CS1400 - MO1
# Assignment 2

# user input
investmentAmount = eval(input("Enter the Initial Investment Amount: "))
monthlyPaymentAmount = eval(input("Enter the Monthly Payment Amount: "))
annualInterestRate = eval(input("Enter the Annual Interest Rate (ex: 6.75): "))
numberOfYears = eval(input("Enter the Number of Years: "))

# convert annual u=interest rate into monthly interest rate for calculation
monthlyInterestRate = (annualInterestRate / 1200)
# convert number of years to number of months for calculation
numberOfMonths = (numberOfYears * 12)
# calculation
futureValueCalc = (investmentAmount * ((1 + monthlyInterestRate) ** numberOfMonths) +
                   monthlyPaymentAmount * ((((1 + monthlyInterestRate) ** numberOfMonths) - 1) / monthlyInterestRate) *
                   (1 + monthlyInterestRate))
# correct decimal placement
futureValue = (int(futureValueCalc * 100) / 100)

# end code
print("the Future Value is: $" + str(futureValue))
