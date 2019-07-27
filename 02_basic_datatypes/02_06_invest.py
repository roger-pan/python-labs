'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

investment_amount = float(input("Investment amount: "))
interest_rate_percetange = float(input("Interest rate: "))
years = float(input("Years: "))
future_value = investment_amount * (1+interest_rate_percetange)**years
print(future_value)

