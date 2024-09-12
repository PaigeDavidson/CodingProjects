# Paige Davidson
# CS1400 - MO1
# Assignment 2

# user input
employeeName = input("Enter employee's name: ")
hoursWorked = eval(input("Enter number of hours worked in a week: "))
hourlyPay = eval(input("Enter hourly pay rate: "))
federalTax = eval(input("Enter federal tax withholding rate (ex. 0.12): "))
stateTax = eval(input("Enter state tax withholding rate (ex. 0.06): "))

# create variables
grossPay = (hoursWorked * hourlyPay)
federalWithholding = (federalTax * grossPay)
stateWithholding = (stateTax * grossPay)
totalDeduction = (federalWithholding + stateWithholding)
netPay = (grossPay - totalDeduction)

# format variables
itemWidth = ">30"
titleWidth = "^40"
numberWidth = ">10.2f"

# formatting
result = "\n"
result += format((employeeName + " pay information").upper(), titleWidth)
result += "\n"
result += "\n"
result += format("Pay", titleWidth)
result += "\n"
result += format("Hours Worked:  ", itemWidth)
result += format(hoursWorked, ">10")
result += "\n"
result += format("Pay Rate: $", itemWidth)
result += format(hourlyPay, numberWidth)
result += "\n"
result += format("Gross Pay: $", itemWidth)
result += format(grossPay, numberWidth)
result += "\n"
result += "\n"
result += format("Deductions", titleWidth)
result += "\n"
result += format("Federal Withholding (11.0%): $", itemWidth)
result += format(federalWithholding, numberWidth)
result += "\n"
result += format("State Withholding (7.0%): $", itemWidth)
result += format(stateWithholding, numberWidth)
result += "\n"
result += format("Total Deduction: $", itemWidth)
result += format(totalDeduction, numberWidth)
result += "\n"
result += "\n"
result += format("Net Pay: $", itemWidth)
result += format(netPay, numberWidth)

# print output
print(result)
