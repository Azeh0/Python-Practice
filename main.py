#Question 1 Number classification even/odd    if( Num % 2 == 0 )
print("Question 1")
NumA = int(input("Input Number: "))

if NumA % 2 ==0:
    print("Number is even")
else:
    print("Number is odd")

#Question 2 Number classification as positive/zero/negative

print("Question 2")

NumB = int(input("Input Number: "))

if NumB > 0:
    print("Number is Positive")

elif NumB < 0:
    print("Number is negative")

elif NumB == 0:
    print("Number is 0")

#Question 3 Determine if A is a multiple of B

print("Question 3")

NumC = int(input("Input Number 1: "))

NumD = int(input("Input Number 2: "))

if NumC % NumD == 0:
    print("Number 1 is a multiple of number 2" )

else:
    print("Number 1 is not a multiple of number 2")

# Question 4 Input 2 numbers output the bigger

print("Question 4")

NumE = int(input("Input Number 1: "))

NumF = int(input("Input Number 2: "))

if NumE > NumF:
    print("Number 1 is greater than number 2")

else:
    print("Number 1 is smaller than number 2")

#Question 5 input a Mark and output if it is pass or fail

print("Question 5")

mark = int(input("Input mark: "))

if mark >= 50:
    print("Good job you pass!")

else:
    print("You Failed!")

#Question 6 Range determination
#Input 10 numbers, count the number of numbers within //each range ( 0-49, 50-59, 60-70, 80+)

print("Question 6")

range_num = int(input("Input Number: "))

if range_num >= 0 and range_num <=49:
    print("The number is between 0-49")

elif range_num >= 50 and range_num <=59:
    print("The number is between 50-59")

elif range_num >= 60 and range_num <=70:
    print("The number is between 60-70")

elif range_num >= 80 and range_num <=999:
    print("The number is between 80+")


