income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
savings = income - expenses
int ProjectedSavings = savings * 12 + (savings * 12 * 0.05)

print("Your monthly savings are ", savings,".")
print("Projected savings after one year, with interest, is: $", ProjectedSavings,".")
