def factorial(number):
  factorial = 1

  if number == 0:
    print('The factorial is 1')
  else:
    for i in range(1,number+1):
      factorial = factorial*i
    print(f'The factorial of {number} is {factorial}')


factorial(number)
# The factorial of 5 is 120