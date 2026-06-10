import Module

print("Inside Client : ",__name__)
print("Value of PI is : ",Module.PI)

Result = 0

Result = Module.Add(11,10)
print("Addition is : ",Result)

Result = Module.Sub(11,10)
print("Subtraction is : ",Result)