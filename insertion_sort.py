# Edwin Urena
# 10/15/25
import random

numbers = [random.randint(0, 66) for i in range(10)]
print(numbers)

iterations = 0



for i in range(len(numbers) - 1):
    j = i - 1

    i = 1

    if numbers[i] > numbers[j]:
        numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)
