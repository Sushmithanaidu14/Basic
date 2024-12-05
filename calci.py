class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackCalculator:
    def __init__(self):
        self.top = None

    def push(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print("Element pushed successfully.")

    def display(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print("Stack elements are:")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

    def pop(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print(f"Popped element: {self.top.data}")
            self.top = self.top.next
            print("Element popped successfully.")

    def count(self):
        count = 0
        temp = self.top
        while temp:
            count += 1
            temp = temp.next
        return count

    def average(self):
        if self.top is None:
            print("Stack is empty. Average cannot be performed.")
        else:
            total = 0
            temp = self.top
            while temp:
                total += temp.data
                temp = temp.next
            print(f"Average is: {total / self.count():.2f}")

    def add(self):
        if self.top is None:
            print("Stack is empty. Addition cannot be performed.")
        else:
            total = 0
            temp = self.top
            while temp:
                total += temp.data
                temp = temp.next
            print(f"Sum is: {total}")

    def subtract(self):
        if self.top is None or self.top.next is None:
            print("Stack does not have enough elements for subtraction.")
        else:
            result = self.top.data
            temp = self.top.next
            while temp:
                result -= temp.data
                temp = temp.next
            print(f"Subtraction result is: {result}")

    def multiply(self):
        if self.top is None or self.top.next is None:
            print("Stack does not have enough elements for multiplication.")
        else:
            result = self.top.data
            temp = self.top.next
            while temp:
                result *= temp.data
                temp = temp.next
            print(f"Multiplication result is: {result}")

    def divide(self):
        if self.top is None or self.top.next is None:
            print("Stack does not have enough elements for division.")
        else:
            result = self.top.data
            temp = self.top.next
            try:
                while temp:
                    result /= temp.data
                    temp = temp.next
                print(f"Division result is: {result:.2f}")
            except ZeroDivisionError:
                print("Division by zero encountered!")

def main():
    calculator = StackCalculator()
    while True:
        print("\n============= Calculator using Stack ==============")
        print("1. Push")
        print("2. Display")
        print("3. Pop")
        print("4. Addition")
        print("5. Subtraction")
        print("6. Average")
        print("7. Division")
        print("8. Multiplication")
        print("9. Exit")
        try:
            choice = int(input("Your option: "))
            if choice == 1:
                calculator.push()
            elif choice == 2:
                calculator.display()
            elif choice == 3:
                calculator.pop()
            elif choice == 4:
                calculator.add()
            elif choice == 5:
                calculator.subtract()
            elif choice == 6:
                calculator.average()
            elif choice == 7:
                calculator.divide()
            elif choice == 8:
                calculator.multiply()
            elif choice == 9:
                print("\nCode Exited.")
                break
            else:
                print("Invalid choice, please select between 1-9.")
        except ValueError:
            print("Please enter a valid numeric option.")

        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont not in ('yes', 'y'):
            print("Exiting program. Thank you!")
            break

if __name__ == "__main__":
    main()
