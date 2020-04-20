import operations
def display():
    choice = int(input("1.Add two numbers\n2.Subtract two numbers\n3.Multlipy"))
    return choice

def operate(choice):
    if choice==1:
        number_1=input("\nEnter First number")
        number_2=input("\Enter second number")
        result = "Sum of "+number_1+'and'+number_2+'is:'+str(operations.add(int(float(number_1)),int(float(number_2))))
        return result
    if choice==2:
            number_1=input("\nEnter First number")
            number_2=input("\Enter second number")
            result = "Sum of"+number_1+'and'+number_2+'is:'+str(operations.subtract(int(float(number_1)),int(float(number_2))))
            return result
    if choice==3:
            number_1=input("\nEnter First number")
            number_2=input("\Enter second number")
            result = "Sum of"+number_1+'and'+number_2+'is:'+str(operations.multiplication(int(float(number_1)),int(float(number_2))))
if __name__ == "__main__":
            print("enter your choice")
            choice = display()
            result=operate(choice)
            print("\n",result)
            
    