
OPPONENT_ROCK = "A"
OPPONENT_PAPER = "B"
OPPONENT_SCISSORS = "C"
PLAYER_ROCK = "X"
PLAYER_PAPER = "Y"
PLAYER_SCISSORS = "Z"
LOSE = "X"
DRAW = "Y"
WIN = "Z"

def game_result(opponent : str, player : str) -> int:
    if ((opponent == OPPONENT_ROCK and player == PLAYER_ROCK) or
        (opponent == OPPONENT_PAPER and player == PLAYER_PAPER) or
        (opponent == OPPONENT_SCISSORS and player == PLAYER_SCISSORS)):
        return 3
    
    if ((opponent == OPPONENT_ROCK and player == PLAYER_SCISSORS) or
        (opponent == OPPONENT_PAPER and player == PLAYER_ROCK) or
        (opponent == OPPONENT_SCISSORS and player == PLAYER_PAPER)):
        return 0
            
    if ((opponent == OPPONENT_ROCK and player == PLAYER_PAPER) or
        (opponent == OPPONENT_PAPER and player == PLAYER_SCISSORS) or
        (opponent == OPPONENT_SCISSORS and player == PLAYER_ROCK)):
        return 6

def play_score(opponent : str, player : str) -> int:
    score = 0
    if player == PLAYER_ROCK:
        score = 1
    elif player == PLAYER_PAPER:
        score = 2
    elif player == PLAYER_SCISSORS:
        score = 3

    return score + game_result(opponent, player)

def part2_score(opponent : str, result : str) -> int:
    if result == LOSE:
        score = 0
    elif result == DRAW:
        score = 3
    elif result == WIN:
        score = 6

    # we play rock
    if ((opponent == OPPONENT_ROCK and result == DRAW) or
        (opponent == OPPONENT_PAPER and result == LOSE) or
        (opponent == OPPONENT_SCISSORS and result == WIN)):
        return score + 1

    # we play paper
    if ((opponent == OPPONENT_ROCK and result == WIN) or
        (opponent == OPPONENT_PAPER and result == DRAW) or
        (opponent == OPPONENT_SCISSORS and result == LOSE)):
        return score + 2

    # we play scissors
    if ((opponent == OPPONENT_ROCK and result == LOSE) or
        (opponent == OPPONENT_PAPER and result == WIN) or
        (opponent == OPPONENT_SCISSORS and result == DRAW)):
        return score + 3

def main():
    total_score = 0
    part2 = 0

    file = open('input', 'r')
    str_lines = file.readlines()

    for line in str_lines:
        parts = line.split()
        total_score += play_score(parts[0], parts[1])
        part2 += part2_score(parts[0], parts[1])

    print(f"total score: {total_score}")
    print(f"part2 score: {part2}")

main()