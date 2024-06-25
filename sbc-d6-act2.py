r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of column: "))

row = 0
column = 0

while row <= r:
    if row == 0 or row == r:
        print('*' * r)
    
    elif column == 0 or column == c:
        print('*' + ' ' * (c - 2) + '*')
    else:
        ...
    row += 1