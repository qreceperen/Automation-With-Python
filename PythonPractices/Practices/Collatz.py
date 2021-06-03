'''Write a function named collatz() that has one parameter named number.
If the number is even, then collatz() should print number // 2 and return this value. If the number is odd, then collatz() should print and return 3 *
number + 1. Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.
The output of this program could look something like this: Enter number: 3 10 5 16 8 4 2 1 '''


# Program should force user to write correct number
def collatz():
    while True: # Force user to write a whole number.
        try:
            number = int(input('Please write a number: '))
            break
        except ValueError:
            print('I did not understand please write a whole number')
            continue

    while number != 1:
        if number %2 == 0:
            number = number //2
            print(number)
        else:
            number = number *3 +1
            print(number)


collatz()
