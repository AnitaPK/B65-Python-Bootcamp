def division():
    try:
        x = 10/0
    except ZeroDivisionError:
        print("Can't divide by zero")

division()

def divByZero():
    x = 10/0

# divByZero()


def divisionOne():
    
    try:
        num1 = int(input("Enter number : "))
        num2 = int(input("Enter number 2 "))

        x = num1/num2
        print(x,' This is result ')
    except ZeroDivisionError:
        print("You can not divide by zero")
    except ValueError:
        print("Please enter valid number")
    finally:
        print("*** End of the division ***")
# divisionOne()


def readHelloFile():
    try:
        f = open('hello.py', 'r')
        content = f.read()
        print(content)
    except FileNotFoundError:
        print('File is not there')
    finally:
        print('********* End *******')

# readHelloFile()

try:
    print('Hello...')
    x = 10/0
except Exception as error:
    print('You got this error', error)


def student_marks():
    try:
        marks = int(input('Enter marks between 0 to 100 : '))
        if marks < 0 or marks >100:
            raise ValueError('Enter Marks between 0 - 100')
        print('Entered marks', marks)

    except ValueError:
        print('Please inter valid value')
    finally:
        print('End')
# student_marks()


def valid_amount():
    try:
        balance = 50000
        amount = int(input("Enter amount to withdraw: "))
       
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
       
        if amount <= balance:
            balance -= amount
            print("Withdraw successful!")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance!")
           
    except ValueError as e:
        print(" Error:", e)
       
    finally:
        print("Thank you for using the ATM.")
 
valid_amount()