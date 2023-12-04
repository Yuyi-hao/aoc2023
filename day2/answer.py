# given 
# balls
# 1. 12 red 
# 2. 13 green 
# 3. 14 blue 


# Game 1: 4 red, 1 green, 15 blue; 6 green, 2 red, 10 blue; 7 blue, 6 green, 4 red; 12 blue, 10 green, 3 red
def isPossible(line):
    game_no, game_sets = line.split(":")
    game_no = int(game_no.split(" ")[1])
    DCT = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    game_sets = game_sets.split(";")
    for game in game_sets:
        for i in game.strip().split(","):
            num, ball = i.strip().split(" ")
            if DCT[ball] < int(num):
                return 0
    
    return game_no


def main(input_file):
    ans = 0 
    # isPossible("Game 1: 4 red, 1 green, 15 blue; 6 green, 2 red, 10 blue; 7 blue, 6 green, 4 red; 12 blue, 10 green, 3 red")
    with open(input_file) as file:
        for line in file.readlines():
            ans += isPossible(line)
    return ans

if __name__=="__main__":
    res = main("./input.txt")
    print(res)