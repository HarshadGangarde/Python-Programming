# Accept : Multiple Parameters
# Return : One Value
def Demo_Function1(Value1 , Value2):
    print("Inside Demo_Function1 : ",Value1,Value2)
    return 11

def main():
    Result = None
    Result = Demo_Function1("Python",21)
    print("Return Value is : ",Result)

if __name__ == "__main__":
    main()
    