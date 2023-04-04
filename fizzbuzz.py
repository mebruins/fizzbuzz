# Three different solutions to 'fizzbuzz' problem

def fizzbuzz(num):
    for i in range(1, num):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
               
        elif i % 5 == 0:
            print('Buzz')
            
        elif i % 3 == 0:
            print('Fizz')
            
        else:
            print(i)

# fizzbuzz(51)

#  prof answer

def fizzbuzz2(num):
    for i in range(1, num+1):
        if (i % 3 == 0) and (i % 5 == 0):
            str = 'FizzBuzz'
               
        elif (i % 5 == 0):
            str = 'Buzz'
            
        elif (i % 3 == 0):
            str = 'Fizz'
            
        else:
            str = i

        print(str)

# fizzbuzz2(50)

num = 50
[print("Fizz"*(n % 3 == 0) + "Buzz"*(n % 5 == 0) or n) for n in range(1, num+1)]
