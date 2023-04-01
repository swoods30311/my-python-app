print(type([]))

number = 12
number_second = 17
number_third = 46
number_fourth = 3

numbers = [number, number_second, number_third, number_fourth, 18, 46]
print(numbers)
numbers.append(110)
print(numbers)
numbers.remove(number_third)
print(numbers)
numbers.pop() #110 was popped. Does this mean Pythons list use stack data structure by default?
del numbers[0]
del numbers[1]
numbers.pop()
print(numbers)