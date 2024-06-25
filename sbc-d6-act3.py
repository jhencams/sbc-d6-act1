def print_pattern(num):

    for i in range(num, 1, -1):
        print("*" * i)

    print("*" + " " *(num -2) + "*")

    for x in range(2, num + 1):
        print("*" * x) 

num = int(input("Enter a number: "))

print_pattern(num)

