# List : [],chang,indexing,duplicate

# 1. Create a list of 5 colors and print it.
color = ['red','pink','blue','bleck','green']
print(color)

# 2. Add a new item to a list using append().
color = ['red','pink','blue','black','green']
color.append("yellow")
print(color)

# 3. Remove an item from a list using remove().
color = ['red','pink','blue','black','green']
color.remove('pink')
print(color)


# 4. Find the length of a list using len()
color = ['red','pink','blue','black','green']
print(len(color))


# 5. Print the first and last element of a list
color = ['red','pink','blue','black','green']
print(color[0],color[-1])


# 6. Replace the third element in a list with a new value
color = ['red','pink','blue','black','green']
color[3] = "yellow"
print(color)

# 7. Sort a list of numbers
color = ['red','pink','blue','black','green','pink']
color.sort()
print(color.sort())

# 8. Count how many times a value appears in a list.
color = ['red','pink','blue','black','green','pink']
a = color.count('pink')
print(a)

# 9. Create a list of 5 numbers and print the maximum number.
a = [15,2,30,6,16]
print(max(a))

# 10. Reverse a list without using slicing.
color = ['red','blue','black','green','pink']
color.reverse()
print(color)


# Tuple

# 1. Create a tuple of 5 fruits and print it.
fruits = ('apple','mengo','orange,','banan','cherry')
print(fruits)


# 2. Print the second and fourth element of a tuple
fruits = ('apple','mengo','orange,','banan','cherry')
print(fruits[1:4:2])

# 3. Find the length of a tuple
fruits = ('apple','mengo','orange,','banan','cherry')
print(len(fruits))

# 4. Check if a value exists in a tuple.
fruits = ('apple','mengo','orange,','banan','cherry')
print("apple" in fruits)
print("papaya" in fruits)


# 5. Convert a tuple into a list.
fruits =  ('apple','mengo','orange,','banan','cherry')
a1 =list(fruits)
print(a1)

# 6. Convert a list into a tuple
color = ['red','pink','blue','bleck','green']
b1 = tuple(color)
print(b1)

# 7. Find the index of an element in a tuple
fruits =  ('apple','mengo','orange,','banan','cherry')
p1 = fruits.index('mengo')
print(p1)

# 8. Count how many times a value appears in a tuple
fruits =  ('apple','mengo','orange,','banan','cherry')
p1 = fruits.count("banan")
print(p1)

# 9. Join two tuples together.
fruits =  ('apple','mengo','orange,','banan','cherry')
color = ('red','pink','blue','bleck','green')
a = color + fruits
print(a)

# 10. Print the last element of a tuple using negative indexing.
fruits =  ('apple','mengo','orange,','banan','cherry')
print(fruits[-1])



#  Set  : {}, unorder, unchangeble, unindexd

# 1. Create a set of 5 unique numbers.
num = {10,3,7,22,15}
print(type(num))
print(num)

# 2. Add a new element to a set using add().
num = {10,3,7,22,15}
num.add(9)
print(num)

# 3. Remove an element from a set using remove().
num = {10,3,7,22,15}
num.remove(22)
print(num)

# 4. Check if a value exists in a set.
num = {10,3,7,22,15}
print(10 in num)

# 5. Create two sets and find their union
num1 = {10,3,7,22,15}
num2 = {5,9,6,12,8}
num = num1.union(num2)
print(num)

# 6. Find the intersection of two sets.
num1 = {10,3,7,22,15}
num2 = {5,9,3,12,8,3}
num =num1.intersection(num2)
print(num)

# 7. Create a set and convert it to a list.
num1 = {10,3,7,22,15}
a1 = list(num1)
print(a1)

# 8. Remove all elements from a set using clear().
num = {10,3,7,22,15}
print(num.clear())


# 9. Find the difference between two sets.
num1 ={"apple","banan","cherry"}
num2 = {"google","microsoft","apple"}
z = num1.difference(num2)
print(z)

# 10. Add multiple elements to a set using update().
num1 = {10,3,7,22,15}
num2 = {15,2,7,4,9}
num1.update(num2)
print(num1)

# DICTIONARY

# 1. Create a dictionary with 3 key-value pairs and print it.
a1 = {'name':'lana','Age':22,'country':"US"}
print(a1)
print(type(a1))

# 2. Add a new key-value pair to a dictionary.
a1 = {'name':'lana','Age':22,'country':"US"}
a1.update({'city':'New york'})
print(a1)

# 3.Remove a key from a dictionary using pop().
a1 = {'name':'lana','Age':22,'country':"US"}
a1.pop('Age')
print(a1)

# 4. Print all keys of a dictionary.
a1 = {'name':'lana','Age':22,'country':"US"}
a = a1.keys()
print(a)

# 5. Print all values of a dictionary.
a1 = {'name':'lana','Age':22,'country':"US"}
print(a1.values())

# 6. Update the value of an existing key.
a1 = {'name':'lana','Age':22,'country':"US"}
a1.update({"city":"new york"})
print(a1)

# 7. Check if a key exists in a dictionary.
a1 = {'name':'lana','Age':22,'country':"US"}
print("name" in a1)


# 8. Create a dictionary and print the number of items.
a1 = {'name':'lana','Age':22,'country':"US"}
print(len(a1))

a1 = {'name':'lana','Age':22,'country':"US"}
a = len(a1)
print("the number of items: ", a)


# 9. Create a dictionary and print only the keys.
a1 = {'name':'lana','Age':22,'country':"US"}
a = a1.keys()
print(a)

# 10. Merge two dictionaries into one.
# a1 = {'name':'lana','Age':22,'country':"US"}
# a2 = {'name': 'bela','Age':24,'country':'US'}
# a = a1.update(a2)
# print(a)