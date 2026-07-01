# 37. Multiply all numbers in a list.........
list = [2,4,6,7,8,4,10,9]


# 38. Create list of tuples and print elements.......

# 39. Count elements in each tuple.
# tuple = (4,3,2,9,5,4,6,7,1,4)
# a = tuple.count(4)
# print(a)

# 40. Convert list into set and print unique values.
# list = [2,4,7,8,3,2,4,7,8,9,4,6,2]
# a1 = set(list)
# print(a1)

# 41. Count how many numbers are prime in a list.
# list = [2,6,9,8,2,8,4,5,6,0,2,4,6]
# print(list.count(2))


# 42. Find common elements between two lists.
list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8,9]
for x in list1:
    if x in list2:
        print(x)
    
# 43. Count digits and letters in a string.....


# 44.Print multiplication table using a for loop.
# i = int (input("Enter tne number : "))
# for x in range(1, 11):
#     print(i ,"*", x, "=", i*x)
 

# 45. Count words in a sentence.
x = "Today is a friday"
# a = len(x.split()) 
# a = x.split(" ")
# print(a) 
a1 = len(x.split())
print(a1)

# 46. Create a list of student dictionaries and calculate average marks....


# 47 .Find the topper student.
num = [1,2,3,6,77,3,2,7,45,50]
largest = num[0]
for x in num:
    if x > largest:
        largest = x
print(largest)
# dic ={
#     "jeel":75,
#     "ravi":80,
#     "meet":88,
#     "dev":90
# }


# 48. Count pass and fail students.......
# students = int(input("Ener the marks :"))
# if students >= 40:
#     print("PASS")
# else:
#     print("FAIL")
    
# 49. Create nested list and print all elements using nested loops
list = [[1,2,3,4,5],
        [6,7,8,9,10]]
for row in list:
    for num in row:
        print(num) # print(num ,end = " ")
    print() 

list = [[1,2,3],[4,5,6],[7,8,9]]
for row in list:
    for num in row:
        print(num, end=" ")
    print()
    
# 50.Create nested dictionary and print all values.

dic = {
    "student1" :{
        "name":"Ravi",
        "marks":80
    },
    "student2":{
        "name":"Meet",
        "marks":82
    },
    "student3":{
        "name":"Dev",
        "marks":90
    }
}
print(dic)

# 51. Count even and odd numbers in nested list:
list = [[3,12,6,7,10,11,14]]
for x in list:
    for y in x:
        if y % 2 ==0:
            print("even num :",y)
        else:
            print("odd num :",y )
    # if x%2 ==0:
    #     print("Even num")
    # else:
    #     print("odd num")




# num = int(input("Enter the num :"))
# if num %2==0:
#     print(num ,": even num")
# else:
#     print(num, ": odd num:")
# list = [[num]]
# print(list)




# 53.Create grade system using marks (A, B, C, Fail)


# 54. Count uppercase, lowercase, digits, and symbols in a string.....
# str = "Hello_123"
# for x in str:
#     # print(x)
    
# 55.Create a list and print only prime numbers......
# a = [2,3,5,7,11,13]

# 56. Create a dictionary and apply tax based on price....





# 57. Find duplicate elements in a list using a for loop.

# list = [12,4,5,2,12,0,5,3,4]
# a = set(list)
# print(a)
# for x in list:
    
# 58. Create two sets and find common elements using a loop.
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
set = set1.intersection(set2)
for i in set:
    print(i)

# 59.Create list of names and print names starting with a vowel.

list = "HELLO"
print(list.lower())

# 60.Create list of numbers and check palindrome numbers.


# 61. Create a number analyzer (positive, negative, even, odd, zero count).
# num = int(input("Enter the num :"))
# if num > 0:
#     print("Positive num ")
#     if num %2 ==0:
#         print("Even num")
#     else:
#         print("Odd num")
# elif num < 0:
#     print("negative num")
#     if num %2 ==0:
#         print("Even num")
#     else:
#         print("Odd num")
# elif num == 0:
#     print("Zero")

# 62.Create a mini student report system (name, marks, average, result).
Name = input("Enter the Name :")
m1 = float(input("Enter the Maths Marks :"))
m2 = float(input("Enter the Hindi Marks:"))
m3 = float(input("Enter the IT marks:"))
avreage  = (m1 + m2 + m3) / 3
print("Name:", Name)
print("Maths: ",m1)
print("English: ",m2)
print("IT: ",m3)
print("Avreage :",avreage)
if avreage >= 40:
    print("Pass")
else:
    print("Fail")