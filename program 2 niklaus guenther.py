#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: Niklaus Guenther     
Program Title: weekly loan calculator
Description: Program 2
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    amountBorrowed = float(input("How much money are you borrowing? "))
    interestRate = float(input("What is the interest rate (in %)? "))
    years = float(input("How many years will you pay back the loan? "))

#Calculates i
    i = interestRate / 5200

#Calculates weekly payment using the formula
    weeklyPayment = (i * amountBorrowed) / (1 - (1 + i) ** (-52 * years))


    print("Your weekly payment will be: ${weeklyPayment:}")
    #Your code ends on the line above

#Do not change any of the code below!
main()