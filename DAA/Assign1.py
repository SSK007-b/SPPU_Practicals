
import time

def NonRec(n):
    fibonacci = [0,1]
    count = 1
    start = time.time()
    for i in range(2, n):
        print(f"The Step {count} number1 = {fibonacci[-1]} and number 2 = {fibonacci[-2]}")
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        count += 1
    
    print("The step Count is ", count)
    print("The Fibonacci Series is ", fibonacci)
    print("The Time Required for Non Recursion ", time.time()-start)

def Rec(n, series = [0,1], step = 1):
    if len(series) >= n:
        print("The Step count is ", step)
        return series
    else:
        print(f"The Step {step} number1 = {series[-1]} and number 2 = {series[-2]}")
        series.append(series[-1] + series[-2])
        return Rec(n, series, step+1)

if __name__ == "__main__":

    n = int(input("Enter the Number for Fibonacci Series "))
    NonRec(n)

    start = time.time()
    fibonacci = Rec(n)
    print("The Fibonacci Series is ", fibonacci)
    print("The Time Required for Non Recursion ", time.time()-start)