# 1.Square Pattern
def square_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

square_pattern(5)

# 2.Rectangle Pattern
def rectangle_pattern(n, width=8):
    for i in range(n):
        for j in range(width):
            print("*", end="")
        print()

rectangle_pattern(5)

# 3.Left Triangle (Half Pyramid)
def left_triangle(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end="")
        print()

left_triangle(5)

# 4.Right Triangle
def right_triangle(n):
    for i in range(n):
        for j in range(n-1-i):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()

right_triangle(5)

# 5.Inverted Left Triangle
def inverted_left_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print()

inverted_left_triangle(5)

# 6.Full Pyramid
def full_pyramid(n):
    for i in range(n):
        # Spaces
        for j in range(n-i-1):
            print(" ", end="")
        # Stars
        for j in range(2*i+1):
            print("*", end="")
        print()

full_pyramid(5)

# 7.Inverted Full Pyramid
def inverted_full_pyramid(n):
    for i in range(n):
        # Spaces
        for j in range(i):
            print(" ", end="")
        # Stars
        for j in range(2*(n-i)-1):
            print("*", end="")
        print()

inverted_full_pyramid(5)

# 8.Hollow Pyramid
def hollow_pyramid(n):
    for i in range(n):
        # Spaces
        for j in range(n-i-1):
            print(" ", end="")
        
        # Stars
        if i == 0 or i == n-1:
            for j in range(2*i+1):
                print("*", end="")
        else:
            print("*", end="")
            for j in range(2*i+1-2):
                print(" ", end="")
            print("*", end="")
        print()

hollow_pyramid(5)

# 9.Full Diamond
def full_diamond(n):
    # Upper half
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        print()
    
    # Lower half
    for i in range(n-2, -1, -1):
        for j in range(i):
            print(" ", end="")
        for j in range(2*(n-i)-1):
            print("*", end="")
        print()

full_diamond(5)

# 10.Hollow Diamond
def hollow_diamond(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        if i == 0 or i == n-1:
            for j in range(2*i+1):
                print("*", end="")
        else:
            print("*", end="")
            for j in range(2*i-1):
                print(" ", end="")
            print("*", end="")
        print()
    
    for i in range(n-2, -1, -1):
        for j in range(i):
            print(" ", end="")
        if i == 0:
            for j in range(1):
                print("*", end="")
        else:
            print("*", end="")
            for j in range(2*i-1):
                print(" ", end="")
            print("*", end="")
        print()

hollow_diamond(5)

# 11.Hollow Square
def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

hollow_square(5)

# 12.Hollow Triangle
def hollow_triangle(n):
    for i in range(n):
        for j in range(i+1):
            if i == n-1 or j == 0 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

hollow_triangle(5)

# 13.Pascal's Triangle (Numbers)
def pascal_triangle(n):
    for i in range(n):
        # Spaces
        for j in range(n-i-1):
            print(" ", end="")
        
        # Numbers
        num = 1
        for j in range(i+1):
            print(num, end=" ")
            num = num * (i-j) // (j+1)
        print()

pascal_triangle(5)

# 14.Floyd's Triangle
def floyd_triangle(n):
    num = 1
    for i in range(1, n+1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

floyd_triangle(5)

# 15.Butterfly Pattern
def butterfly_pattern(n):
    # Upper half
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        for j in range(2*(n-i-1)):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()
    
    # Lower half
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            print("*", end="")
        for j in range(2*(n-i-1)):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()

butterfly_pattern(5)

# 16.Hourglass Pattern
def hourglass_pattern(n):
    # Upper inverted pyramid
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(2*(n-i)-1):
            print("*", end="")
        print()
    
    # Lower pyramid
    for i in range(1, n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        print()

hourglass_pattern(5)

# 17.Zig-Zag Pattern
def zigzag_pattern(n):
    for i in range(n):
        # Spaces
        for j in range(i):
            print(" ", end="")
        # Stars (decreasing)
        for j in range(n-i):
            print("*", end=" ")
        print()

zigzag_pattern(5)
