# Exercise 1 - Python Calculator

def calc (Operator , Value1 , Value2):
    #calc to
    if Operator == "x":
        return (multiply(Value1, Value2))
    elif Operator == "+":
        return (add(Value1, Value2))
    elif Operator == "/":
        return (divide(Value1,Value2))
    elif Operator == "-":
        return (subtract(Value2, Value2))
    else:
        print ("Invalid Operator")


def multiply (x, y):
    return x*y

def add (x,y):
    return x+y

def divide(x,y):
    return x/y

def subtract(x,y):
    return x-y


def executefile (filename):
    f = open(filename, "r")
    list = []
    for line in f:
        list.append(line)
    return list

def Processlist(inputs):
    #loop through items
    total = 0
    for item in inputs:
        x = item.split(" ")

        operator = x[1]
        value1 = int(x[2])
        value2 = int(x[3].strip('\n'))

        #print(calc (operator, value1, value2))
        total = total + calc (operator, value1, value2)
    
    print (total)


def ProcessPart3():

    list = executefile("Step3.txt")

    print (len(list))



#executefile("calcinput.txt")
#parts 1 + 2
Processlist(executefile("calcinput.txt"))

#part3
ProcessPart3()



