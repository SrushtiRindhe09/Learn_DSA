/*Implement a ticket booking system where customers join a queue. The queue
is served in the order they arrive (FIFO).
a) Enqeue: New customer books a ticket.
b) Dequeue: Customer is served.
c) Display Queue: Show customers waiting.*/

#include <iostream>
using namespace std;

#define SIZE 10

string queueArr[SIZE];
int front = -1, rear = -1;

void enqueue(string name) {
    if (rear == SIZE - 1) {
        cout << "Queue is full.\n";
    } else {
        if (front == -1) front = 0;
        queueArr[++rear] = name;
        cout << "Ticket booked for " << name << endl;
    }
}

void dequeue() {
    if (front == -1 || front > rear) {
        cout << "No customers in queue.\n";
    } else {
        cout << queueArr[front] << " is served.\n";
        front++;
    }
}

void display() {
    if (front == -1 || front > rear) {
        cout << "No customers waiting.\n";
    } else {
        cout << "Customers in queue: ";
        for (int i = front; i <= rear; i++) {
            cout << queueArr[i] << " ";
        }
        cout << endl;
    }
}

int main() {
    int choice;
    string name;

    while (true) {
        cout << "\n--- Ticket Booking System ---\n";
        cout << "1. Enqueue (Book Ticket)\n";
        cout << "2. Dequeue (Serve Customer)\n";
        cout << "3. Display Queue\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter customer name: ";
                cin >> name;
                enqueue(name);
                break;
            case 2:
                dequeue();
                break;
            case 3:
                display();
                break;
            case 4:
                return 0;
            default:
                cout << "Invalid choice.\n";
        }
    }
}

/*
-------Output--------
--- Ticket Booking System ---
1. Enqueue (Book Ticket)
2. Dequeue (Serve Customer)
3. Display Queue
4. Exit
Enter your choice: 1
Enter customer name: pqr
Ticket booked for pqr

--- Ticket Booking System ---
1. Enqueue (Book Ticket)
2. Dequeue (Serve Customer)
3. Display Queue
4. Exit
Enter your choice: 1
Enter customer name: abc
Ticket booked for abc

--- Ticket Booking System ---
1. Enqueue (Book Ticket)
2. Dequeue (Serve Customer)
3. Display Queue
4. Exit
Enter your choice: 2
pqr is served.

--- Ticket Booking System ---
1. Enqueue (Book Ticket)
2. Dequeue (Serve Customer)
3. Display Queue
4. Exit
Enter your choice: 3
Customers in queue: abc 

--- Ticket Booking System ---
1. Enqueue (Book Ticket)
2. Dequeue (Serve Customer)
3. Display Queue
4. Exit
Enter your choice: 4


=== Code Execution Successful ===

*/
