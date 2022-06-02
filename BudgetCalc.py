
#This program is a budget calculator that allows a user to enter a total monthly income amount and then
# as many items as needed.  The program stores all entered amounts in a list and them totals all entries
# It this calculates the difference between the monthly income and all user entries for final balance

#List that will store all entered amounts and then totals them to be used in final amount
totalExpenses = []
totalExpenses = [int(x) for x in totalExpenses]

#This function goes through the list of entries and totals then subtracts from monthly income
def FinalTotal():
    total = 0
    leftoverAmount = 0
    for x in range(0, len(totalExpenses)):
        total = total + totalExpenses[x]
    print("Your total monthly expenses is $" + str(total))
    leftoverAmount = totalMonthly - total
    print("Your remaining available monthly balance is $" + str(leftoverAmount))

#If a user amount is negative, this statement makes user aware and prompts to restart program
    if leftoverAmount < 0:
        print("")
        print("YOU HAVE A NEGATIVE BALANCE, PLEASE RESTART AND CHECK AGAIN")

#This function takes all the entered expenses and adds to the list
def ExpensePrompt():

    expenseName = input("Enter the name of expense: ")
    expenseAmount = input("Enter the amount of expense: $ ")
    expenseAmount = int(expenseAmount)
    totalExpenses.append(expenseAmount)

totalMonthly = input("Enter Total Monthly Income: $ ")
totalMonthly = int(totalMonthly)
print("")

print("Please enter up to all monthly expenses")

#while loop that accepts as many entries as user wants to add
while True:

    ExpensePrompt()

    print("")
    promptRepeat = input("Would you like to enter another expense? (Please Enter Y or N): ")

    if promptRepeat == "Y":
        continue

    elif promptRepeat == "N":
        print()
        FinalTotal()
        break

    else:
        print("Please enter a Y or N")
        promptRepeat = input("Would you like to enter another expense? (Please Enter Y or N): ")
        if promptRepeat == "N":
            print()
            FinalTotal()
            break
        elif promptRepeat != "Y":
            promptRepeat = input("Would you like to enter another expense? (Please Enter Y or N): ")












