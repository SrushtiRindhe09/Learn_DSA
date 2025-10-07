'''
Consider a student database of SY computer class (at least 10 records).
Database contains different fields of every student like Roll No, Name and
SGPA. Implement the following using insertion sort
a. Arrange list of students according to roll numbers in ascending order.
b. Organize the list of students alphabetically.
c. Arrange list of students to identify five toppers from a class. 
'''

# -------------------- Student database --------------------
students = [
    {"roll": 5, "name": "Sakshi", "sgpa": 8.9},
    {"roll": 2, "name": "Aditya", "sgpa": 9.1},
    {"roll": 9, "name": "Mohan", "sgpa": 7.8},
    {"roll": 1, "name": "Pooja", "sgpa": 9.5},
    {"roll": 7, "name": "Ravi", "sgpa": 8.1},
    {"roll": 3, "name": "Kiran", "sgpa": 8.7},
    {"roll": 4, "name": "Tina", "sgpa": 9.2},
    {"roll": 8, "name": "Varun", "sgpa": 7.5},
    {"roll": 6, "name": "Divya", "sgpa": 8.3},
    {"roll": 10, "name": "Neha", "sgpa": 8.8}
]

# ---------------Insertion sort function --------------------
def insertion_sort(data, key, reverse=False):
    for i in range(1, len(data)):
        temp = data[i]
        j = i - 1
        while j >= 0 and ((data[j][key] > temp[key]) if not reverse else (data[j][key] < temp[key])):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = temp
    return data

# -------------------- Menu loop --------------------
while True:
    print("\n Student Sorting Menu")
    print("1. Sort by Roll Number (Ascending)")
    print("2. Sort by Name (Alphabetical)")
    print("3. Show Top 5 Students by SGPA")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        sorted_by_roll = insertion_sort(students.copy(), "roll")
        print("\n Students sorted by Roll Number:")
        for s in sorted_by_roll:
            print(s)

    elif choice == "2":
        sorted_by_name = insertion_sort(students.copy(), "name")
        print("\n Students sorted by Name:")
        for s in sorted_by_name:
            print(s)

    elif choice == "3":
        sorted_by_sgpa = insertion_sort(students.copy(), "sgpa", reverse=True)
        print("\n Top 5 Students by SGPA:")
        for s in sorted_by_sgpa[:5]:
            print(s)

    elif choice == "4":
        print("\n Exiting program. Goodbye!")
        break  
    
    else:
        print(" Invalid choice! Please enter 1, 2, 3, or 4.")

'''
Output
Student Sorting Menu
1. Sort by Roll Number (Ascending)
2. Sort by Name (Alphabetical)
3. Show Top 5 Students by SGPA
4. Exit
Enter your choice (1/2/3/4): 1

 Students sorted by Roll Number:
{'roll': 1, 'name': 'Pooja', 'sgpa': 9.5}
{'roll': 2, 'name': 'Aditya', 'sgpa': 9.1}
{'roll': 3, 'name': 'Kiran', 'sgpa': 8.7}
{'roll': 4, 'name': 'Tina', 'sgpa': 9.2}
{'roll': 5, 'name': 'Sakshi', 'sgpa': 8.9}
{'roll': 6, 'name': 'Divya', 'sgpa': 8.3}
{'roll': 7, 'name': 'Ravi', 'sgpa': 8.1}
{'roll': 8, 'name': 'Varun', 'sgpa': 7.5}
{'roll': 9, 'name': 'Mohan', 'sgpa': 7.8}
{'roll': 10, 'name': 'Neha', 'sgpa': 8.8}

Student Sorting Menu
1. Sort by Roll Number (Ascending)
2. Sort by Name (Alphabetical)
3. Show Top 5 Students by SGPA
4. Exit
Enter your choice (1/2/3/4): 2

Students sorted by Name:
{'roll': 2, 'name': 'Aditya', 'sgpa': 9.1}
{'roll': 6, 'name': 'Divya', 'sgpa': 8.3}
{'roll': 3, 'name': 'Kiran', 'sgpa': 8.7}
{'roll': 9, 'name': 'Mohan', 'sgpa': 7.8}
{'roll': 10, 'name': 'Neha', 'sgpa': 8.8}
{'roll': 1, 'name': 'Pooja', 'sgpa': 9.5}
{'roll': 7, 'name': 'Ravi', 'sgpa': 8.1}
{'roll': 5, 'name': 'Sakshi', 'sgpa': 8.9}
{'roll': 4, 'name': 'Tina', 'sgpa': 9.2}
{'roll': 8, 'name': 'Varun', 'sgpa': 7.5}

Student Sorting Menu
1. Sort by Roll Number (Ascending)
2. Sort by Name (Alphabetical)
3. Show Top 5 Students by SGPA
4. Exit
Enter your choice (1/2/3/4): 3

 Top 5 Students by SGPA:
{'roll': 1, 'name': 'Pooja', 'sgpa': 9.5}
{'roll': 4, 'name': 'Tina', 'sgpa': 9.2}
{'roll': 2, 'name': 'Aditya', 'sgpa': 9.1}
{'roll': 5, 'name': 'Sakshi', 'sgpa': 8.9}
{'roll': 10, 'name': 'Neha', 'sgpa': 8.8}

Student Sorting Menu
1. Sort by Roll Number (Ascending)
2. Sort by Name (Alphabetical)
3. Show Top 5 Students by SGPA
4. Exit
Enter your choice (1/2/3/4): 4

 Exiting program. Goodbye!

=== Code Execution Successful ===
'''
