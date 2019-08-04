'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

x = int(input("Enter a number between 0 and 1,000,000,000: "))
counter = 0
while counter <= 1000000000:
    if counter == x:
        print(x)
        break
    counter += 1