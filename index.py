def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

operator = {
    '+':add,
    '-':sub,
    '*':mul,
    '/':div,
}


num1 = float(input("Enter a first number: "))

should_continue = False
while not should_continue:
    for keys in operator:
        print(keys)
    operation = input('Please select a operation: ')
    
    num2= float(input('Enter next number: '))
    calculation = operator[operation]
    c1=calculation(num1,num2)
    print(f"{num1} {operation} {num2} = {c1}")
    
    con = input(f"do you want to contineus calculation with {c1} answer ? type 'yes' or 'no' ")
    
    if con == 'no':
        should_continue =True
    else:
        num1=c1
    