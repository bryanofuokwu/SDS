class Calculator():
    def addNum(self, num1, num2):
        return num1 + num2
    def multiplyNum(self, num1, num2):
        return num1 * num2
    def subnum(self, num1, num2):
        return num1 - num2
    def dividenum(self, num1, num2):
        return num1//num2
    

if __name__ == "__main__":
    math = Calculator()
    x = 1
    while x == 1:
        operation = input("add, subtract, multiply, or divide?\n")
        numx =  input ("1st number: ")
        numx = int(numx)
        numy =  input ("2nd number: ")
        numy = int(numy)

        if operation == "add":
            print (math.addNum(numx, numy) )
            break 
        elif operation == "subtract":
            print (math.subnum(numx,  numy))
            break
        elif operation == "multiply":
            print (math.multiplyNum(numx, numy))
            break
        elif operation == "divide":
            print(math.dividenum(numx, numy))
            break
        
            


    
