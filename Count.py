import msvcrt
     
class Counting:
    #everything runs in one function
    #First the program will read from the .txt file and save the number in a variable
    #After that the counting function will run until the quit key has been pressed
    #Finally the program will write the new number to the .txt file

    def write(self,numberInput):
        file_path = "number.txt"

        with open(file_path, 'w') as file:
            file.write(numberInput)

    def read(self, file_path):
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                print("File content: ")
                print(file_content)
                
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("An error occured")

        return file_content


    def Function(self):
        index = 0

        while True:
            #print("initializing function")
            #print("Type a letter (or 'q' to quit)", end = ' ', flush = True)
            char = msvcrt.getch().decode('utf-8')

            if char == 'q':
                print("Exiting loop")
                
                break
            else:
                index = index + 1
                print(index)
        return index

