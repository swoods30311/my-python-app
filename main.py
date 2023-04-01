print(type([]))

number = 12
number_second = 17
number_third = 46
number_fourth = 3

numbers = [number, number_second, number_third, number_fourth, 18, 46]
print(numbers)
numbers.append(110)
print(numbers)
print(len(numbers))
numbers.sort()
print(numbers)
print(110 in numbers)
print(numbers[0])
print(type(numbers[4]))
numbers.clear()
print(numbers)