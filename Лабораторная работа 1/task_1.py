numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
new_array = []

for number in numbers:
    if not number is None:
        new_array.append(number)

count_elements = len(numbers)

average = round(sum(new_array)/count_elements,2)

numbers[numbers.index(None)] = average

print("Измененный список:", numbers)
