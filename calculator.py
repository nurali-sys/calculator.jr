operator = input('Choose an operator(+ - * /): ')
def oper(operator):
   if operator not in ("+" or '-' or '*' or "/"):
      print('Operator is not defined')
      exit()

num1 = int(input("Enter your 1st number: "))
num2 = int(input('Enter your 2nd number: '))

def calculator(operator, num1, num2):
   if operator == '+':
    sum = num1 + num2
    print(f'{num1} + {num2} = {sum}')
   elif operator == '-':
    sum = num1 - num2
    print(f'{num1} - {num2} = {sum}')
   elif operator == '*':
    sum = num1 * num2
    print(f'{num1} * {num2} = {sum}')
   elif operator == '/':
    sum = num1 / num2
    print(f'{num1} / {num2} = {sum}')

oper(operator)
calculator(operator, num1, num2)
