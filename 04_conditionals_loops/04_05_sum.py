'''
Take two numbers from the user, an upper and lower bound.
Using a loop, calculate the sum of all numbers from the lower bound to the upper bound.

For example, if a user enters 1 and 100, the output should be:

The sum is: 5050
'''

lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

sum = 0
for i in range(lower_bound,upper_bound+1):
    sum += i
print(sum)