#initial empty lists, sets and dictionary.
books_list=[]
authors_set=set()
books_dict={}

books_list.append("Python Programming")
authors_set.add("John smith")
books_dict["Python programming"]="John Smith"

books_list.append("Python Fundamentals")
authors_set.add("John Smith")
books_dict["Python Fundamentals"]="John Smith"

books_list.append("Data strucutre and Algorithm")
authors_set.add("Jane Doe")
books_dict["Data structure and Algorithm"]="Jane Doe"

books_list.append("Machine Learning Basics")
authors_set.add("Alice Johnson")
books_dict["Machine Learning Basics"]="Alice Johnson"

#search for books
search_title=input("Enter the title of the book to search:")
if search_title in books_list:
    print(f"Book found! The author of the book '{search_title}' is {books_dict[search_title]}")
else:
    print("Books not found!")


#remove a book from the list, set and dictionary:
remove_title=input("Entter the title of the book to remove else enter to skip")
if remove_title in books_list:
    remove_author=books_dict[remove_title]
    books_list.remove(remove_title)
    del books_dict[remove_title]

    if remove_author not in books_dict.value(): #check if the author has any other boks in the dictionary
        authors_set.remove(remove_author)

    print("Books removed successfully!")
    print("Books availabe along with their authors:",books_dict)
    print("Just available books:", books_list)
    print("JUst available authors:", authors_set)

else:
    print("Book not found!") 

    
