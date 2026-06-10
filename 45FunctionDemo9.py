# One Function can call another function

def fun():
    print("Inside fun")

def gun():
    print("Inside gun")

def main():          # one function
    fun()            # another function
    gun()            # another function

if __name__ == "__main__":
    main()
    