import random

# Makes a random list of numbers between one and one hundred
numbers = [random.randint(1, 100) for i in range(10)]

print(numbers)

iterations = 0


# Checks to see if the list is sorted or not
def check_if_sorted():
    for i in range(len(numbers) - 1):
        j = i + 1
        if numbers[i] > numbers[j]:
            return False
    return True


# Does one iteration of bubble sort
def bubble_sort():
    # Makes sure that function widens its scope to global for this variable
    global iterations

    for i in range(len(numbers) - (iterations + 1)):
        j = i + 1

        chicken = numbers[i]  # "chicken" serves as a placeholder value

        # Switches numbers if the left number is greater than the right number
        if numbers[i] > numbers[j]:
            numbers[i] = numbers[j]
            numbers[j] = chicken

    # Reiterates bubble sort if list is not sorted yet
    if check_if_sorted() == False:
        iterations = iterations + 1
        bubble_sort()


bubble_sort()
print(numbers)

print("here for commit")
