
file_path = "input/input_day1-1.txt"

file = open(file_path, "r")
input = file.readlines()

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

def replace_string_rek(line, index):
    if index < 1:
        return line
    else:
        new_line = line.replace(num_dict[index], str(index))
        index -= 1
        return replace_string_rek(new_line, index)


for i in range(0, len(input)):
    nums_in_line = []
    currnt_line = replace_string_rek(input[i], 9)
    
    for j in range(0, len(currnt_line)):
        value = currnt_line[j]
        try:
            value = int(value)
            nums_in_line.append(value)
        except:
            next

    if len(nums_in_line) == 1:
        result += int(str(nums_in_line[0]) + str(nums_in_line[0]))
    if len(nums_in_line) > 1:
        result += int(str(nums_in_line[0]) + str(nums_in_line[-1]))

print(result)