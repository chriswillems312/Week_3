from math import sqrt
length_a = int(input("What is the length of the first side of the triangle?"))
length_b = int(input("WHat is the length of the second side of the triangle?"))
length_c = sqrt(length_a * length_a + length_b * length_b)

print("the length of the third side of the triangle is ")
print(length_c)

from math import sqrt
length_a = int(input("What is the length of the base of the triangle?"))
length_b = int(input("What is the length of the left side of the triangle?"))
length_c = int(input("What is the length of the right side of the triangle?"))

if length_b < length_c :
    print("True")
else :
    print("False")