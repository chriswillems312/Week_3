numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
for number in numbers :
    if number >= 75 :
        print("First")
    elif number >= 70 and number < 75 :
        print("Upper second")
    elif number >= 60 and number < 70 :
        print("Second")
    elif number >= 50 and number < 60:
        print("Third")
    elif number >= 45 and number < 50 :
        print("F1 supp")
    elif number >= 40 and number < 45 :
        print("F2")
    elif number < 40 :
        print("F3")