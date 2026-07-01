name = str(input("Enter the student name:"))
Marks1 = float(input("Enter the student English: "))
Marks2 = float(input("Enter the student Maths: "))
Marks3 = float(input("Enter the student IT: "))
Marks4 = float(input("Enter the student Hindi: "))
Marks5 = float(input("Enter the student SSE: "))

list =[Marks1,Marks2,Marks3,Marks4,Marks5]
# print(list)

# Convert to tuple
tuple = tuple(list)
print(tuple)

# 4. grade based on average:

Total = sum(tuple)
Average = Total /len(tuple)
# print(Total)
print(Average)


if Average >= 75:
    Grade ="A"
elif Average>=60:
    Grade ="B"
elif Average >=50:
    Grade ="C"
else:
    Grade ="Fail"
    

# 5. Store result in dictnoray
dict = {
    "Name":name,
    "Marks":tuple,
    "Total":Total,
    "Average":Average,
    "Grade":Grade
}
print(dict)


# 6. set remove duplicat marks
set =set(tuple)
print(set)


#  Bool variabal
if Average >= 50:
    print(bool("PASS"))
# else:
#     print(bool)


