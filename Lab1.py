# ex1 
radius = float(input("Enter radius circle: ")) 
area =3.14*radius*2 
area = round(area , 2 )
print("Circle area = ", area) 

#ex2 
c =float(input("Enter tempeture in Celisus :"))
f = c* 9/5 + 32 
print("Convert to F :",f) 


#ex3 
n = int(input("Enter a number? "))

is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is a NOT prime number")

#ex4
n = int(input("Enter a number? "))

sum_divisors = 0

for i in range(1, n):
    if n % i == 0:
        sum_divisors += i

if n > 0 and sum_divisors == n:
    print(n, "is a perfect number")
else:
    print(n, "is a NOT perfect number")

#ex5 
colors = ["Blue", "Yellow", "Black", "Red", "White"]

favorite_color = input("What is your favorite color? ")

if favorite_color in colors:
    index = colors.index(favorite_color)
    print("Your color is at index", index, "in my list")
else:
    print("Sorry, I could not find your color")

#ex6 
range1 = range(0, 7)
range2 = range(1, 11, 3)
range3 = range(5, 0, -1)
range4 = range(6, -3, -2)

print("range1:", list(range1))
print("range2:", list(range2))
print("range3:", list(range3))
print("range4:", list(range4))

#ex7 
def remove_dollar_sign(s):
    new_string = s.replace("$", "")
    return new_string

text = input("Enter a string: ")

result = remove_dollar_sign(text)

print(result)
#ex8
def extract_even(l):
    result = []

    for number in l:
        if number % 2 == 0:
            result.append(number)

    return result

#ex9 
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result
#ex10 
def get_divisors(n):
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors

#ex11 
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("Distance =", distance)

#ex12
def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
