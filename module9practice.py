#Error Handling
#Carlie Peters
#Python

#First we want to use defensive programming.
#Defensive Programming- When we use our existing tools to prevent the user form breaking our program.
#Conditionals and loops are best used with exception handling.
##Exceptions are the errors the compiler throws

#Getting a number example

#This will crash if a number is not given
# my_num = int(input('Please enter a number: '))

# print(f'{my_num} + 1 = {my_num + 1}')

while True:
    try:
        my_num = int(input('Please enter a number: '))
        print(f'100 / {my_num} = {100/my_num}')
        break #end of the loop
    except ValueError:
        print('You did not enter a number. Please try again.\n')
    except ZeroDivisionError:
        print('You cannot divide by zero.')
    except:
        print('Something went wrong.')

question = 'Please enter a number greater than zero: '
print(f'{'- '*len(question)}')

while True:
    try:
        my_num = int(input(question))
        if  my_num < 1:
            raise ValueError('Must enter a number greater than zero.')
        
        print(f'100 / {my_num} = {100/my_num}')
        break #end of the loop
    except ValueError as ex:
        print(f'{ex}\n')
    except ZeroDivisionError:
        print('You cannot divide by zero.')
    except ex:
        print(f'{ex}\n')
        