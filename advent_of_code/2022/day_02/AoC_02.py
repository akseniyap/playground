data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip())

game = {
    "rock rock": "draw", "rock paper": "win", "rock scissors": "lose",
    "paper rock": "lose", "paper paper": "draw", "paper scissors": "win",
    "scissors rock": "win", "scissors paper": "lose", "scissors scissors": "draw",
}
player_1_opts = {"A": "rock", "B": "paper", "C": "scissors"}
player_2_opts = {"X": "rock", "Y": "paper", "Z": "scissors"}
sign_points = {"X": 1, "Y": 2, "Z": 3}
game_points = {"lose": 0, "draw": 3, "win": 6}

def part_one(data):
    result = 0
    for line in data:
        player_1, player_2 = line.split(' ')
        result += sign_points[player_2]
        result += game_points[game[' '.join([player_1_opts[player_1], player_2_opts[player_2]])]]

    return result

print(part_one(data))


game = {
    "rock draw": "rock", "rock win": "paper", "rock lose": "scissors",
    "paper lose": "rock", "paper draw": "paper", "paper win": "scissors",
    "scissors win": "rock", "scissors lose": "paper", "scissors draw": "scissors",
}
player_1_opts = {"A": "rock", "B": "paper", "C": "scissors"}
game_result = {"X": "lose", "Y": "draw", "Z": "win"}
sign_points = {"rock": 1, "paper": 2, "scissors": 3}
game_points = {"X": 0, "Y": 3, "Z": 6}

def part_two(data):
    result = 0
    for line in data:
        player_1, end_result = line.split(' ')
        player_2 = game[' '.join([player_1_opts[player_1], game_result[end_result]])]

        result += sign_points[player_2]
        result += game_points[end_result]

    return result

print(part_two(data))
