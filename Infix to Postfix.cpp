#include <iostream>
using namespace std;

#define SIZE 50

// Stack implementation using array
char stack[SIZE];
int top = -1;

// Push function
void push(char ch) {
    stack[++top] = ch;
}

// Pop function
char pop() {
    return stack[top--];
}

// Peek function
char peek() {
    return stack[top];
}

// Check if stack is empty
bool isEmpty() {
    return (top == -1);
}

// Function to return precedence of operators
int precedence(char ch) {
    if (ch == '^') return 3;
    if (ch == '*' || ch == '/') return 2;
    if (ch == '+' || ch == '-') return 1;
    return 0;
}

// Function to calculate string length (since we are not using <cstring>)
int length(char str[]) {
    int i = 0;
    while (str[i] != '\0') {
        i++;
    }
    return i;
}

// Function to convert infix to postfix
void infixToPostfix(char infix[]) {
    char postfix[SIZE];
    int j = 0;
    int n = length(infix); // get length of input

    for (int i = 0; i < n; i++) {
        char c = infix[i];

        // If operand (letter or digit) → add to postfix
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')) {
            postfix[j++] = c;
        }
        // If '(' → push to stack
        else if (c == '(') {
            push(c);
        }
        // If ')' → pop until '(' is found
        else if (c == ')') {
            while (!isEmpty() && peek() != '(') {
                postfix[j++] = pop();
            }
            pop(); // remove '('
        }
        // If operator → pop higher or equal precedence operators
        else {
            while (!isEmpty() && precedence(peek()) >= precedence(c)) {
                postfix[j++] = pop();
            }
            push(c);
        }
    }

    // Pop remaining operators
    while (!isEmpty()) {
        postfix[j++] = pop();
    }

    postfix[j] = '\0'; // terminate postfix string

    cout << "\nPostfix Expression: " << postfix;
}

int main() {
    char infix[SIZE];
    cout << "Enter infix expression: ";
    cin >> infix;

    infixToPostfix(infix);

    return 0;
}
