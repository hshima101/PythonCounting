import msvcrt

class Testing:
    def keypress(self):
        index = 0
        while True:
            print("initializing function")
            print("Type a letter (or 'q' to quit)", end = ' ', flush = True)
            char = msvcrt.getch().decode('utf-8')

            if char == 'q':
                print("Exiting loop")
                break
            else:
                print(f"You typed {char}")
                index = index + 1
                print(index)

    def write(file, data):
        try:
            with open(file, 'w') as file:
                for item in data:
                    file.write(str(item) + '\n')
            print(f"data written to {file} successfully")
        except Exception as e:
            print(f'Error writing to {file}')

    def load(filename):
        try:
            with open(filename, 'r') as file:
                data = [int(line.strip()) for line in file]
            return data
        except Exception as e:
            print(f'Error loading data from {file}: {str(e)}')
            return []


