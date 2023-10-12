from Count import Testing

def main():
    print("Main has been invoked")
    obj = Testing()
    #obj.keypress()
    loaded = obj.load('number.txt')
    print(loaded)

if __name__ == "__main__":
    main()