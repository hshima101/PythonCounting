from Count import Testing
from Count import FileWrite
from Count import Counting

def main():

    print("Main has been invoked")
    #a = FileWrite()
    #a.write()
    #a.read('number.txt')

    b = Counting()
    
    numbers = b.read('number.txt')
    print("Number from file: ", numbers)

    try:
        convertedNum = int(numbers)
    except ValueError:
        print("Error: The content of the 'number.txt' is not a valid integer.")
        return
    
    #int and string type collision error. fix
    convertedNum = convertedNum + b.Function()
    print("Final Number: ",convertedNum)
    #final = str(convertedNum)
    #b.write(final)
    #write(numbers)
    


if __name__ == "__main__":
    main()