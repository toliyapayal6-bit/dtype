# 1. Take an integer from the user and check whether it is positive, negative, or zero.
# def fun_name():
#     fun_name = int(input("Enter the num :"))
#     if fun_name> 0:
#         print("Positive")
#     elif fun_name<0:
#         print("negative")
#     else:
#         print("zero")
# fun_name()

# 2. Take a float from the user and check whether it is a whole number or decimal.
# def num():
#     num = float(input("Today whether: "))
#     if  num % 1 ==0:
#         print("whole")
#     else:
#         print("Decimal")
# num()

# 3. Take a character from the user and check whether it is a vowel or consonant.










# 4. Take age from the user and check whether the user is eligible to vote.
# def fun():
#     age = int(input("Enter the age: "))
#     if (age >= 18):
#         print("eligible to vote.")
#     else:
#         print("Not eligible to vote.")
# fun()


# 5. Take three numbers from the user and find the largest number......
# def fun_num():
#     list =[30,22,10]
#     x = list[0]
#     for x in list:
#         if x > list:
#             x = list
#     print(x)
# fun_num()

# 6. Take a number from the user and check whether it is even or odd.
# def num():
#     num = int(input("Enter the num: "))
#     if num %2 == 0:
#         print("Even num ")
#     else:
#         print("Odd num ")
# num()

# 7. Take marks from the user and print grade (A, B, C, or Fail).......
# def marks():
#     marks = int(input("Enter the marks:"))
#     if (marks >= 80):
#         print("A")
#     elif (marks >=70):
#         print("B")
#     elif (marks >= 40):
#         print("C")
#     else:
#         print("Fail")
# marks()

# 8. Take temperature from the user and print Hot, Warm, or Cold using conditions.
# def fun():
#     temp = float(input("Enter the temperature :"))
#     if temp >= 35:
#         print("Hot")
#     elif temp >= 16:
#         print("Wram")
#     else:
#         print("Colde")
# fun()


# 9.Take a password from the user and check whether its length is at least 8 characters.
# def num():
#     num= input("Ente the num:")
#     x = len(num)
#     # print(x)
#     if x == 8:
#         print("Curect Passwor")
#     else:
#         print("Wrong Password")
# num()

# 10. Take a year from the user and check whether it is a leap year...




# 11. Print all even numbers from 1 to 50 using for loop and if condition
# def num():
#     print("Even number :")
#     for x in range(1,50):
#         if (x %2 ==0):
#             print(x, end=",")
# num()


# 12. Take a number from the user and find its factorial using a loop......
# def factorial(n):
#     if n < 0:
#         return 1
#     else:
#         return n * factorial (n-1)
# factorial(5)     

# 13. Take a number from the user and print its multiplication table.
# def fun_num():
#     num = (int(input("Enter the num :")))
#     for i in range(1,11):
#         print(num,"x", i,"=",(num*i))
# fun_num()


# 14. Take list size from the user, create a list using input, and print the sum of all elements.......



# 15. From a list, print only positive numbers using loop and if condition.
# def num():
#     list = [1,4,-5,6,-3,0,9,5,-2,-8,-1]
#     for x in list:
#         if x > 0:
#             print(x, end=" ")  
# num()


# 16. Find the maximum value from a tuple using a loop........
# def max_num():
#     tuple = (10,8,16,4,12,20,9)
#     x = tuple[0]
#     if x > tuple:
#         x = tuple
# print(tuple)
# max_num()

# 17. From a set, print only even numbers
# def fun_num():
#     # set = {input("Enter the num: ")}
#     # print(set)
#     set = {3,6,9,1,10,12,6,12,5,17,22}
#     print("even num")
#     for x in set:
#         if x % 2 ==0:
#             print(x)
# fun_num()


# 18. Store student names and marks in a dictionary and print only passed students.
# def student():
#     dic = {
#         "Ravi":88,
#         "Meet":75,
#         "Dev":50,
#         "Jeel":40
#     }
#     for x in dic:
#         print(x)
# student()

# 19. Count how many vowels are present in a list of characters.

# 20. Check whether a number is prime using loop and condition.

# 21. Create a function to check whether a number is even or odd
# def num(n):
#     if n %2 ==0:
#         print(n,"Even num ")
#     else:
#         print(n, "Odd num")
# num(5)
# num(10)
# num(11)
# num(14)

# 22. Create a function that takes a list and returns the sum of all elements.
# def fun_num():
#     list = [10,5,12,5,9,18,22]
#     a = sum(list)
#     print(a)
# fun_num()


# 23. Create a function that counts how many positive numbers are in a list..........
def fun():
    list = [10,-4,0,-6,12,-3,1,-11,15]
    for x in list:
        if x > 0:
            print(x)
fun()


# 24. Create a function that checks whether a character is uppercase or lowercase.......
def fun(a):
    b = a.upper()
    c = a.lower()
    print(b)
    print(c)
fun("Ravi")
fun("jeel")

# 25. Create a function to find the maximum number from three numbers.
# def fun_num(a,b,c):    
# fun_num()
    
    
# 26. Create a function that checks whether a number is palindrome.

# 27. Create a function that takes a tuple and prints only odd numbers.
# def fun():
#     tuple = (10,4,7,9,2,4,11,2,12,8,1)
#     for x in tuple:
#         if(x%2 !=0):
#             print(x)
# fun()

# 28. Create a function that accepts a dictionary and prints keys having value greater than 50.....

# 29. Create a function that takes a list and removes duplicate values using set.
# def fun():
#     list = [10,2,5,7,10,2,5,8,7,3,8]
#     a = set(list)
#     print(a)
# fun()

# 30. Create a function to calculate simple interest using user input.
# def fun_num():
#     P = float(input("Enter the num :"))
#     R = float(input("Enter the rant :"))
#     T = float(input("Entet the Time: "))
#     intrest = (P* R *T)/100
#     print(intrest)
    
# fun_num()

# 31. Use try-except to handle division by zero error.
# try:
#     a = int(input("Enter the num :"))
#     print(a / 0)
# except:
#     a = 10 # a = int(input("Enter the num:"))
#     print(a / 2)


# 32. Take input and handle invalid integer input using try-except.
# try:
#     num = int(input("Enter the integer num: "))
#     print(num)
# except:
#     num = float(input("Enter the float num:"))
#     print(num)

# 33. Create a program using try-except-else-finally to divide two numbers.

# try:
#     a = int(input("Enter the num:"))
#     b = int(input("Enter the num: "))
#     print(a / b)
# except:
#     a = float(input("Enter the num = "))
#     b = float(input("Enter the num = "))
#     print(a / b)
# else:
#     print("Output integer and float num")
# finally:
#     print("Complete")
    
    

# 34. Handle index error when accessing list elements using try-except.



# 35. Handle key error while accessing dictionary values using try-except.
try:
    dic ={
        "name":"ravi",
        "age":22
    }
    print(dic("city"))
except :
    print(dic)


# 36. Take list input from user and inside loop check even and odd numbers using if-else.......

# list = list(int(input("Enter the num: ")))
# print(list)
# for x in list:
#     if x % 2 == 0:
#         print("Even num",x)
#     else:
#         print("Odd num",x)

# 37. Inside if condition, run a loop to print numbers from 1 to given number........


# 38. Inside loop, take user input and store values in list, then check max value......
# list = [9,8,12,11,4,5,16,3]
# for x in list:
#     # print(x, end=" ")
#     x = list[0]
#     if x > list:
#         x = list
# print(x)


# 39. Inside function, use loop and if to count even numbers from list.......
# def function():
#     list = [1,2,3,4,5,6,7,8,9]
#     for x in list:
#         if x % 2 == 0:
#             print(x)
#             # print(len(x))
# function()

# 40. Inside function, use try-except to handle invalid input and return result.

# def function():
#     try:
#         num = int(input("Enter the int num:"))
#         print(num)
#     except:
#         num= input("Enter the num: ")
#         print(num)
# function()


# 41. Create a program where user enters marks of 5 subjects, store in list, and calculate average............

# def sum():
#     # marks = [50,20,70,75,89]
#     list = [int(input("Enter the marks :"))]
#     print(list)
    
        
# sum()


# 42. Check if all values in a tuple are positive using loop and if.
def tuple():
    tuple =(12,-1,2,-4,5-6,4,9,3,-14,5,-3)
    for x in tuple:
        if x > 0:
            print(x)
tuple()

# 43. Convert list into set and print unique values.
def fun():
    list = [12,3,6,8,4,12,5,6,8,0,12,8,3,0]
    num = set(list)
    print(num)
fun()

# 44. Create dictionary from two lists (keys and values) using loop.
dic = {
    "name":["ravi","meet","jeel","dev"],
    "age":[20,19,23,21]
}
print(dic.keys())
print(dic.values())


# 45. Count frequency of each character in a string using dictionary.

str = "HelloWorld"
freq = {}
for a in str:
    if a in freq:
        freq[a] += 1
    else:
        freq[a] = 1
print(freq)

# 46. Create menu-driven program using while loop (add, subtract, multiply, divide).

# 47. Create login system where user gets only 3 attempts using loop and if.
# 48. Check whether all numbers in list are prime using nested loop and if.
# 49. Create function that returns square of only even numbers from list.
# 50. Create function that accepts set and returns list of sorted elements.
# 51. Create program to reverse a number using loop.
# 52. Check whether a string is palindrome using loop and if.
# 53. Create dictionary of product and price, then print products above price 500.
# 54. Create function that finds common elements between two lists using set.
# 55. Use try-except-finally to open a file and handle file not found error.
# 56. Create function that validates user age using exception handling.
# 57. Create program where inside function you use list, loop, if-else, and try-except together.







