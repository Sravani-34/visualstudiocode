def factorial(n):
    if n == 0:
        breakpoint
        return 1
    else:
        breakpoint
        return n * factorial(n-1)
    
if __name__ == "__main__":
    breakpoint
    n = 5
    print(f"The factorial of {n} is {factorial(n)}")
    print("This is the main program")