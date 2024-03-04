# Initialize empty lists,sets,and dictionary
books_list = []
authors_set =set()
books_dict = {}

# add books 
books_list.append("python programming")
authors_set.add("jhon smith")
books_dict["python programming"] = "john smith"

books_list.append("data structure and algorithms")
authors_set.add("jane doe")
books_dict["data structure and algorithms"] = "jane doe"

books_list.append("machine learning basics")
authors_set.add("alice johnson")
books_dict["machine learning basics"] = "alice johnson"

# search for a book
search_title = input("enter the title of the book to search: ")
if search_title in books_list:
    print(f"book found! author: {books_dict[search_title]}")
else:
    print("book not found!")  

# Display all books 
print("list of books:")   
for book in books_list:
    print(book)

# Remove a book
remove_title  = input("enetr the title of the book to remove or else enetr to skip: ") 
if remove_title in books_list:
    remove_author = books_dict[remove_title] 
    books_list.remove(remove_title)  
    authors_set.remove(remove_author)
    del books_dict[remove_title] 
    print("book remove sucessfully!")    
    print("books avialable: ", books_list)   
else:
    print("book not found!")       
