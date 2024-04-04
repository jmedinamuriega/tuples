# 2.

# Task 1:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
def add_books():
    bookshelf=list(library)
    add_book=input("What book do you want to add?")
    author=input("Please introduce the name of the author")
    new_list=[add_book,author]
    new_list=tuple(new_list)
    if new_list in bookshelf:
        print("We already have that book")
    else:
        bookshelf.append(tuple(new_list))
        library2=tuple(bookshelf)
        print(library2)
add_books()



        
        
    
    
    
   
    
    