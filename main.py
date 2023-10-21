from Count import Counting

def main():
    print("Main has been invoked")

    b = Counting()

    # Read the content of 'number.txt' and convert it to an integer
    try:
        with open('number.txt', 'r') as file:
            numbers = int(file.read())
    except (ValueError, FileNotFoundError):
        print("Error: 'number.txt' does not contain a valid integer.")
        return

    print(numbers)

    # Perform your calculations on the integer
    print("Press any key to add numbers")
    print("Press 'q' to quit")

    #Function from the Counting class will run until the q key is pressed
    convertedNum = numbers + b.Function()
    print("Final Number:", convertedNum)

    # Convert the result back to a string and write it to the file
    final = str(convertedNum)
    with open('number.txt', 'w') as file:
        file.write(final)

if __name__ == "__main__":
    main()
