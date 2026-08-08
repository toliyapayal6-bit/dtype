list = []
tuple = ("Fiction", "Non-Fiction", "Sci-Fi")
Book_id = set()
# 1. Add a new book
def new_book():
    try:
        id = int(input("Enter the ID: "))
        
        Title = input("Enter The Tital: ")
        
        author = {}
        for categories in tuple:
            author[categories] = input(f"store fixed categories:{tuple}")
                
        dict = {
            "ID":id,
            "Tital":Title,
            "Author":author
            # "book":Book
        }
        print(dict)
        Book = list 
        if Book in list:
            print("Availability")

        else:
            print(" Not Availability")
        
        list.append(dict)
        Book_id.add(id)
        print("Add a new book")
        print(dict)
        
    except:
        print("Invelid ID")
        

new_book()
# 2. Remove a book
def remove_book():
    ID  = int(input("Enter the ID :"))
    ID == Book_id
    for book in list:
        if book == list:
            list.remove(dict)
            # Book_id.pop(id)
    print("Remove a book", dict)        
    
remove_book()

# 3. View all books

def all_Book():
    id = int(input("Enter the BooK ID:"))
    tital = input("Enter the Book Tital:")
    author = {}
    for caracter in tuple:
        author[caracter] = input(f"store fixed categories{tuple}")
    
    dict = {
        "id":id,
        "Tital":tital,
        "Author":author
    }
    print(dict)
all_Book()


# 4. Borrow a book
# def Borrow_Book():
   
# Borrow_Book()
