data = [] 



def input_data():
    global data
    nums = input("Enter data for a 1D array (separated by spaces): ")
    data = list(map(int, nums.split()))
    print("Data has been stored successfully!")



def display_summary():
    if not data:
        print("No data available. Please input data first.")
        return

    total = len(data)
    minimum = min(data)
    maximum = max(data)
    total_sum = sum(data)
    average = total_sum / total

    print("Data Summary:")
    print(f"- Total elements: {total}")
    print(f"- Minimum value: {minimum}")
    print(f"- Maximum value: {maximum}")
    print(f"- Sum of all values: {total_sum}")
    print(f"- Average value: {average:.2f}")



def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def calculate_factorial():
    num = int(input("Enter a number to calculate its factorial: "))
    if num < 0:
        print("Factorial not defined for negative numbers.")
    else:
        print(f"Factorial of {num} is: {factorial(num)}")



def filter_data():
    if not data:
        print("No data available. Please input data first.")
        return

    threshold = int(input("Enter a threshold value: "))
    filtered = list(filter(lambda x: x >= threshold, data))

    print("\nFiltered Data (values >= threshold):")
    print(", ".join(map(str, filtered)) if filtered else "No values found.")



def sort_data():
    if not data:
        print("No data available. Please input data first.")
        return

    print("Choose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = input("Enter your choice: ")

    if choice == "1":
        sorted_data = sorted(data)
        print("Sorted Data in Ascending Order:")
        print(", ".join(map(str, sorted_data)))

    elif choice == "2":
        sorted_data = sorted(data, reverse=True)
        print("Sorted Data in Descending Order:")
        print(", ".join(map(str, sorted_data)))
    else:
        print("Invalid choice.")



def dataset_statistics():
    if not data:
        print("No data available. Please input data first.")
        return

    minimum = min(data)
    maximum = max(data)
    total_sum = sum(data)
    average = total_sum / len(data)

    return minimum, maximum, total_sum, average


def display_statistics():
    stats = dataset_statistics()
    if stats:
        minimum, maximum, total_sum, average = stats
        print("Dataset Statistics:")
        print(f"- Minimum value: {minimum}")
        print(f"- Maximum value: {maximum}")
        print(f"- Sum of all values: {total_sum}")
        print(f"- Average value: {average:.2f}")


def main():
    while True:
        print("Welcome to the Data Analyzer and Transformer Program")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")


        choice = input("Please enter your choice: ")


        if choice == "1":
            input_data()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            calculate_factorial()
        elif choice == "4":
            filter_data()
        elif choice == "5":
            sort_data()
        elif choice == "6":
            display_statistics()
        elif choice == "7":
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
                
main()