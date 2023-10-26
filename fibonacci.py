def main():
    limit = input("Enter the upper limit of the series: ")
    while not limit.isdigit():
        print("Please enter a digit")
        limit = input("Enter the upper limit of the series: ")
    print("Here is the Fibonacci Series till "+limit+":")
    fibonacci(int(limit))

def fibonacci(n:int):
    a, b = 0, 1
    while b <=n:
        series = b
        b += a
        a = series
        if b <=n:
            print(b)
    
if __name__=="__main__":
    main()