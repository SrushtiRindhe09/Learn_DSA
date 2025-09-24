#include <iostream>
#include <cstring>
using namespace std;

#define MAX 100

// Stack implementation using array
char stack[MAX];
int top = -1;

// Push operation
void push(char c) {
    stack[++top] = c;
}

// Pop operation
char pop() {
    return stack[top--];
}

// Peek top element
char peek() {
    return stack[top];
}

// Check if stack is empty
bool isEmpty() {
    return top == -1;
}

// Function to check precedence of operators
int precedence(char c) {
    if (c == '^') return 3;
    else if (c == '*' || c == '/') return 2;
    else if (c == '+' || c == '-') return 1;
    else return -1;
}

// Function to convert infix to postfix
void infixToPostfix(char infix[]) {
    char postfix[MAX];
    int k = 0;

    for (int i = 0; i < strlen(infix); i++) {
        char c = infix[i];

        // If character is operand, add to output
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')) {
            postfix[k++] = c;
        }
        // If '(', push to stack
        else if (c == '(') {
            push(c);
        }
        // If ')', pop until '(' is found
        else if (c == ')') {
            while (!isEmpty() && peek() != '(') {
                postfix[k++] = pop();
            }
            pop(); // Remove '('
        }
        // If operator, pop higher or equal precedence operators first
        else {
            while (!isEmpty() && precedence(peek()) >= precedence(c)) {
                postfix[k++] = pop();
            }
            push(c);
        }
    }

    // Pop remaining operators
    while (!isEmpty()) {
        postfix[k++] = pop();
    }

    postfix[k] = '\0'; // Null terminate string

    cout << "\nPostfix Expression: " << postfix << endl;
}

int main() {
    char infix[MAX];
    cout << "Enter Infix Expression: ";
    cin >> infix;

    infixToPostfix(infix);
    return 0;
}
