from functions.get_new_score import get_new_score

if __name__ == '__main__':
    FINISH_GAME_SCORE = 2002
    player_score = 0
    computer_score = 0
    game_round = 0
    while True:
        game_round += 1
        draw = input("To draw the number, please push enter")
        player_score = get_new_score(player_score, game_round)
        computer_score = get_new_score(computer_score, game_round)
        if player_score >= FINISH_GAME_SCORE or computer_score >= FINISH_GAME_SCORE:
            if player_score > computer_score:
                print(f"You won with {player_score} points. Computer had {computer_score} points")
            else:
                print(f"Computer won with {computer_score} points.You had {player_score} points")
            break
        print(f"Your current points: {player_score}")
        print(f"Computer current points: {computer_score}")
