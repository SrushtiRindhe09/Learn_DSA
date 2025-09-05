// Linear Search in JavaScript

function linearSearch(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) {
            return i; // return index if found
        }
    }
    return -1; // return -1 if not found
}

// Example usage
let numbers = [10, 25, 30, 45, 50];
let target = 30;

let result = linearSearch(numbers, target);

if (result !== -1) {
    console.log(`Element found at index ${result}`);
} else {
    console.log("Element not found");
}


/* Python code for same approah
#Linear Search in Python

def linear_search(arr, target):
    for i in range(len(arr)):
    if arr[i] == target:
    return i
return -1

numbers = [10, 25, 30, 45, 50]
target = 30

result = linear_search(numbers, target)

if result != -1:
    print(f "Element found at index {result}")
else :
    print("Element not found")*/