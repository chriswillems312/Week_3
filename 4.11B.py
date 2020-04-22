#Question 6 - 14
numbers = [1, 3, 5, 7, 8, 9, 12, 17, 222]
words = ["hoi", "doei", "hallo", "hello", "amsterdam", "almelo", "enschede", "groningen", "sparta", "Sam", "rotterdam"]
words_without_sam = 0
sqrt_number_sum = 0
from math import sqrt

for word in words:
    if word != "Sam" :
        words_without_sam += 1
    elif word == "Sam" :
        break
print("done")

print("there are", words_without_sam, "words without Sam before Sam is found")

for number in numbers :
    print("better", sqrt(number))

for triangle in [1, 2, 3, 4, 5]:
    print(triangle, "\t", ((triangle * (triangle + 1))// 2), "\n")

for number in numbers :
    sqrt_number_sum += sqrt(number)

for number in numbers :
    print(sqrt(number))

print("the sum of the squared numbers is", sqrt_number_sum)