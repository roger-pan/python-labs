'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''

def sum(list):
    agg = 0
    for each in list:
        agg += each
    return agg

print(sum([0,2,3,4]))

