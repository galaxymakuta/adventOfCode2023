file_path = "./input/input2.txt"

with open(file_path, "r") as file:
    input_lines = file.readlines()

class GameObject: 
    max_cubes = {
        "red" : 12,
        "green" : 13,
        "blue" : 14,
    }
    possible = True

    def __init__(self, game_number) -> None:
        self.number = game_number
    
    def get_colors(self, game_set):
        for set in game_set:
            set_array = set.split(" ")
            set_array = list(filter(None, set_array))
            for index in range(0, len(set_array), 2):
                color = set_array[index+1].replace("\n", "")
                amount = set_array[index]

                if self.max_cubes[color] < int(amount):
                    self.possible = False
                    return


game_list = []

for game in input_lines:
    splittet_string = game.split(" ")
    
    # create gameobject with number
    game_number = splittet_string[1].replace(":", "")
    new_game_object = GameObject(game_number=game_number)
    # format sets array
    game_sets = splittet_string[2:]
    game_sets = " ".join(game_sets).replace(",", "")

    current_set_list = game_sets.split(";")
    new_game_object.get_colors(game_set=current_set_list)
    game_list.append(new_game_object)

result = 0
for obj in game_list:
    if obj.possible:
        result += int(obj.number)

print(result)
