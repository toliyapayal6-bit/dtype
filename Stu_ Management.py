Students =[]
sub =("Math", "Science", "English")
stu_ids = set()

# 1. Add a new student
def add_stu(): 
    try:
        stu_id = int(input("Enter the ID : "))
            # if stu_id in stu_id:
            #     return
        
        name = input("Enter the name : ")
        marks = []
        for subject in sub:
            mark = int(input(f"Enter marks for {subject}: "))
            marks.append(mark)
            
        dict = {
            "ID": stu_id,
            "Name":name,
            "Marks":marks
        }
        print(dict)
        Students.append(dict)
        stu_ids.add(stu_id)
        print("Student id succesfully!")
    
    except ValueError:
        print("invalid input, ")
           
add_stu()

# 2. Display all students
def display():
    print(Students)
display()

# 3. Search for a student by ID

def search_stu():
    try:
        ID = int(input("Serch Student id: "))
        for dict in Students:
            if dict['ID'] == ID:
                print("Student Found")
                print(Students)
                return
        raise LookupError("Student not found")
    
    except LookupError as e:
        print("Error",e)
search_stu()


# 4. Update student marks
def updat(): 
    try:
        stu_id = int(input("Updat Stu_ID : "))
            # if stu_id in stu_id:
            #     return
        
        name = input("Enter the name : ")
        new_marks = []
        for subject in sub:
            mark = int(input(f"Enter new_marks for {subject}: "))
            new_marks.append(mark)
            
        dict= {
            "ID": stu_id,
            "Name":name,
            "Marks":new_marks
        }
        print(dict)
        Students.append(dict)
        print(Students)
    
    except ValueError as e:
        print("Error",e)
updat()

# 5. Delete a student
def delete_stu():
    try:
        id = int(input("Enter the Id :"))
        for dict in Students:
            if id == dict["ID"]:
                Students.remove(dict)   
                print("Delet student:")
                return
            print(Students)
           
        raise("Invelid ID")    
    except ValueError as e:
        print("Error",e)
                    
delete_stu()

# 6. Exit


while True:
    # print("-----Student-------")
    print("\n1. Add Student")
    print("2. Disply Student")
    print("3. Serch Student")
    print("4. Update Student")
    print("5. Delet Student")
    print("6. Exit")
    n = int(input("Enter the index"))
    
    if n == "1":
        add_stu()
    elif n == "2":
        display()
    elif n == "3":
        search_stu()
    elif n == "4":
        updat()
    elif n == "5":
        delete_stu()
    elif n == "6":
        print("END")
        break
    else:
        print("Invelid Choice")
    


    

