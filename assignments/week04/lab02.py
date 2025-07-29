"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    even_numbers = []
    odd_numbers = []
    above_average = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        number = int(input(f"Enter the number of {i+1} : "))
        numbers.append(number)
    
    # Display original list
    print(f"Original numbers: {numbers}\n")
    
    # Create filtered lists
    for i in range(10):
        if numbers[i] % 2 == 0 :
            even_numbers.append(numbers[i])
        else :
            odd_numbers.append(numbers[i])
    
    # Calculate average
    average = sum(numbers) / 10 # Your code here
    
    # Numbers greater than average
    for i in range(10):
        if numbers[i] > average:
            above_average.append(numbers[i])
    
    # Display results
    print(numbers)
    print(even_numbers)
    print(odd_numbers)
    print(above_average)
    print(max(numbers))
    print(min(numbers))


if __name__ == "__main__":
    number_operations()