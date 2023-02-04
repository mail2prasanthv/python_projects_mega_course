def add(num1, num2):
    return num1+num2

def multiply(num1, num2):
    return num1*num2

if  __name__ == "__main__": #executes only if it invokes independently
    print("---outside the function----")
    print("Value of __name__is :" , __name__)
    # value of variable __name__ is __main__ if we run this file independently
    # value of variable __name__ is filename if rerence any of the method from another file
