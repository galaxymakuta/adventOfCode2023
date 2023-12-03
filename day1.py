import re

file_path = "input/input_day1.txt"

with open(file_path, "r") as file:
    input_lines = file.readlines()

result = 0

num_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
def replace_numbers(value):
    for index in range(3 ,len(value)):
        for key in range(1, len(num_dict)+1):
            replaced_part = value[:index]
            if num_dict[key] in replaced_part:
                replaced_part = replaced_part.replace(num_dict[key], str(key))
                rest_of_string = value[index:]
                return replace_numbers(replaced_part+rest_of_string)
    
    return value

#new_values = [replace_numbers(value) for value in input_lines]  

number_list = []

for index in range(0, len(input_lines)):
    numbers_in_string = re.findall(r'\d+', input_lines[index])
    numbers = ''.join(numbers_in_string)
    if len(numbers) == 1:
        result += int(numbers_in_string[0])
        number_list.append(numbers_in_string[0])
        print(numbers_in_string[0])
    if len(numbers) > 1:
        result += int(numbers[0] + numbers[-1])
        number_list.append(numbers[0] + numbers[-1])
        print(int(numbers[0] + numbers[-1]))
    
print(result)

#! versuch mal nochmal den ersten teil hinzubekommen