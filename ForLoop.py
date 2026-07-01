# 1.Create a list of integers and find the sum using a for loop.
# list = [10,4,5,8,2,4]
# for i in list:
#     print(i)

# 2.Print all even numbers from a list.
# for i in range(0,100,2):
#     print(i)

# 3.Print all odd numbers from a list.
# for i in range(1,100,2):
#     print(i)
    
# 4.Count numbers greater than 50 in a list.

# for i in range(101):
#     if i >= 50:
#         print(i)

# 5. Find the maximum number in a list.

# list = [10,4,6,12,9]
# print(max(list))

# 6.Find the minimum number in a list.
# list = [10,4,6,20,3]
# print(min(list))

# 7. Count positive and negative numbers in a list................................
# i = [10,-3,5,-8,9,2,-5,3,8]
# if i > 0:
#     print( i)
# elif i < 0:
#     print( i)

# 8.Print elements of a tuple using a for loop.
# tuple = (1,4,7,10,4,7,2)
# for i in tuple:
#     print(i)
#     # print(i , end =", ")
    
# 9. Count numbers less than 20 in a tuple
# tuple = (4,16,10,18,29,20,4,22,45,39,2)
# for i in tuple:
#     if i < 20:
#         print(i)

# 10.Find the sum of tuple elements..................

# tuple = (4,16,10,18,29,20,4,22,45,39,2)
# sum = sum(tuple)
# print(sum)

# 11.Take a string and count vowels.......
# str = "Hello"
# s = str.count("l")
# print(s)

# 12.Count consonants in a string............



# 13.Print each character of a string.
# str = "character"
# for i in str:
#     print(i)
    
# 14.Count uppercase letters in a string
# str = "Application"
# a = str.upper()
# print(a)
# # print(str.upper())


# 15.Count lowercase letters in a string
# str = "AppliCatIon"
# print(str.lower())

# 16.Create a set and print unique elements.
# set = {4,2,8,1,4,2,1,4,8,1,9,10}
# print(set)

# 17.Count numbers greater than 100 in a set.
# set = (10,123,456,98,245,200,50,350,3,75,83,64,28,100)
# for i  in set:
#     if i >= 100:
#         print(i, end=" ")
        

# 18.Print all keys of a dictionary.
# dic = {
#     "Name":"ravi",
#     "Age":22,
#     "City":"Delhi"
# }
# print(dic.keys())

# 19.Print all values of a dictionary.
# dic = {
#     "Name":"Ravi",
#     "Age":22,
#     "City":"Delhi"
# }
# print(dic.values())

# 20. Check pass/fail based on marks using if-else
# Marks = int(input("Enter the Marks: "))
# if Marks>= 40:
#     print("Pass")
# else:
#     print("Fail")
    
# 21.Count even and odd numbers in a list............
list = [2,5,7,0,1,6,20]
for i in list:
    if i %2 == 0:
        print(i , "Even", end=" ")
    else:
        print(i , "odd", end=" ")
        
        
# 22.Find average of numbers in a list.
# list = [24,29,10,16,8,20,13]
# ave = sum(list)|len(list)
# print(ave)

# 23.Separate positive and negative numbers into two lists........
# list = [1,-5,9,-3,10,2,-9,4,5,-8,5,2,-7,5,8,-7]


# 24.Count numbers divisible by 5
# num = int(input("Enter tne num :"))
# a = num / 5
# print(a)

# 25. Reverse a string using a for loop..........
# str = ("happy")
# for x in str:
#     print(str[::-1])


# 26. Count frequency of characters in a string.
# str = "helloooo"
# for i in str:
#     print(i ,":",str.count(i))


# 27. Find second largest number in a list.
# list = [14,80,87,23,45,68,90]
# largest = list[0]
# for num in list:
#     if num > largest:
#         largest = num
# print(largest)
# for i in list:
#     if i < largest:
#         largest = i
#         print(i)


# 28. Merge two lists and print elements.
# list1 = [12,2,3,5,6,7,8]
# list2 = [8,9,3,4,11,6,3]
# list1.extend(list2)
# print(list1)
# list = list1 + list2
# print(list)


# 29. Count numbers between 10 and 50.
# for i in range(10,51):
#     print(i)


# 30.Remove duplicates from a list using a set........
# list1 = [2,3,6,4,9,8,2,3,4,9,2,3]
# a1 = set(list1)
# print(a1)


# 31. Create a list of floats and find their sum.
# list = [3.6, 12.5, 6.2, 9.5, 10, 8.5]
# print(sum(list))


# 32. Count vowels in a list of words.........


# 33. Create a dictionary of students and print passed students.........
# dic = {
#     "ravi":75,
#     "meet":55,
#     "jeel":45
# }
# for i in dic:
#     print(i)




# 34.Apply discount on product prices using dictionary........



# 35. Find highest value in a dictionary.........
# dic = {"list" :[3,4,6,7,9,2,1,10]}
# large = dic[0]
# for i in dic:
#     if i > large:
#         large = i
# print(large)
   
   
# 36.Find lowest value in a dictionary.......