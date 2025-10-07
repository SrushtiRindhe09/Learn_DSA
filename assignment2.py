'''
Question
Construct Smart Library Management System: Implementation and
Comparison of Linear and Binary Search Algorithms for Locating Books in an
Unsorted Book Database.
'''

# -------------------- Book Database --------------------
books = [
    "Python Programming",
    "Data Structures",
    "Algorithms",
    "Database Management",
    "Operating System",
    "Computer Networks",
    "Artificial Intelligence",
    "Machine Learning",
    "Web Development",
    "Cyber Security"
]

# -------------------- Linear Search --------------------
def linear_search(book_list, target):
    """
    Searches for a book in the list one by one.
    Returns index if found, -1 if not found.
    """
    for i in range(len(book_list)):
        if book_list[i].lower() == target.lower():
            return i
    return -1

# -------------------- Binary Search --------------------
def binary_search(sorted_list, target):
    """
    Searches for a book in a sorted list using binary search.
    Returns index if found, -1 if not found.
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid].lower() == target.lower():
            return mid
        elif target.lower() < sorted_list[mid].lower():
            high = mid - 1
        else:
            low = mid + 1

    return -1

# -------------------- Main Program --------------------
while True:
    print("\n SMART LIBRARY MANAGEMENT SYSTEM ")
    print("1. Search Book using Linear Search")
    print("2. Search Book using Binary Search")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        book_name = input("Enter the book name to search: ")
        index = linear_search(books, book_name)
        if index != -1:
            print(f"Book '{books[index]}' found at position {index + 1}")
        else:
            print(f"Book '{book_name}' not found!")

    elif choice == "2":
        book_name = input("Enter the book name to search: ")
        sorted_books = sorted(books)  
        index = binary_search(sorted_books, book_name)
        if index != -1:
            print(f"Book '{sorted_books[index]}' found at position {index + 1} in sorted list")
        else:
            print(f" Book '{book_name}' not found!")

    elif choice == "3":
        print("Exiting the Library System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")


'''
Output

 SMART LIBRARY MANAGEMENT SYSTEM 
1. Search Book using Linear Search
2. Search Book using Binary Search
3. Exit
Enter your choice (1/2/3): 1
Enter the book name to search: data structures
Book 'Data Structures' found at position 2

 SMART LIBRARY MANAGEMENT SYSTEM 
1. Search Book using Linear Search
2. Search Book using Binary Search
3. Exit
Enter your choice (1/2/3): 2
Enter the book name to search: machine learning
Book 'Machine Learning' found at position 7 in sorted list

 SMART LIBRARY MANAGEMENT SYSTEM 
1. Search Book using Linear Search
2. Search Book using Binary Search
3. Exit
Enter your choice (1/2/3): 2
Enter the book name to search: compter network
 Book 'compter network' not found!

 SMART LIBRARY MANAGEMENT SYSTEM 
1. Search Book using Linear Search
2. Search Book using Binary Search
3. Exit
Enter your choice (1/2/3): 3
Exiting the Library System. Goodbye!

'''
