#Task 1
'''
Fibonacci sequence a series of numbers in which each number,
is the sum of the two that precede it
'''

#NoOfTerms = int(input(" Enter a number between "))

def fnc_fib(n):
    if n <= 1:
        return n
    else:
        return(fnc_fib(n-1) + fnc_fib(n-2))

#NoOfTerms = 10
NoOfTerms = int(input(" Enter an n'th element "))

if NoOfTerms <= 0:
    print("Please enter a positive integer")
else:
    print("Your chosen Fibonacci sequence")
    for i in range(NoOfTerms):
        print(fnc_fib(i))

    


