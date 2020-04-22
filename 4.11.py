#Question 1 - 5
numbers = [1, 3, 5, 7, 8, 9, -1, -2, -3, -4, -5]
words = ["hoi", "doei", "hallo", "hello", "amsterdam", "almelo", "enschede", "groningen", "sparta", "Sam", "rotterdam"]
counter = 0
evenCount = 0
negativeCount = 0
length = 0
till_even_number = 0
for number in numbers :
    if number % 2 == 1:
        counter += 1

for number in numbers:
    if not number % 2 == 1:
        evenCount += number

for number in numbers:
    if number < 0 :
        negativeCount += number

for word in words:
    if len(word) == 5 :
        length += 1

for number in numbers:
    if number % 2 == 1 :
        till_even_number += number
    elif number % 2 == 0 :
        break
    print(till_even_number)
print("done")

print("The sum of the even numbers is", evenCount)
print("There are", counter, "odd numbers")
print("The sum of the negative numbers is", negativeCount)
print("The amount of words with length 5 is", length)
print(till_even_number)