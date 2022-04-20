from functions.get_new_score import get_new_score
from random import sample

if __name__ == '__main__':
    FINISH_GAME_SCORE = 2002
    player_score = 0
    computer_score = 0
    DICE_TYPES = {"D3": 3,
                  "D4": 4,
                  "D6": 6,
                  "D8": 8,
                  "D10": 8,
                  "D12": 12,
                  "D20": 20,
                  "D100": 100,
                  }
    dice_types_list = [key for key in DICE_TYPES]
    game_round = 1
    while True:
        user_dice_1 = input(f"To draw the number 1, please write draw type from list {dice_types_list}")
        user_dice_1 = user_dice_1.upper()
        if user_dice_1 not in dice_types_list:
            print("Your draw does not exist in the list")
            continue
        user_dice_2 = input(f"To draw the number 2, please write draw type from list {dice_types_list}")
        user_dice_2 = user_dice_2.upper()

        if user_dice_2 not in dice_types_list:
            print("Your draw does not exist in the list")
            continue
        end_draws = [DICE_TYPES[user_dice_1], DICE_TYPES[user_dice_2]]
        for end_draw in end_draws:
            player_score = get_new_score(player_score, game_round, end_draw)

        computer_dice_1 = sample(DICE_TYPES.keys(), 1)[0]
        computer_dice_2 = sample(DICE_TYPES.keys(), 1)[0]
        end_draws = [DICE_TYPES[computer_dice_1], DICE_TYPES[computer_dice_2]]
        for end_draw in end_draws:
            computer_score = get_new_score(computer_score, game_round, end_draw)

        if player_score >= FINISH_GAME_SCORE or computer_score >= FINISH_GAME_SCORE:
            if player_score > computer_score:
                print(f"You won with {player_score} points. Computer had {computer_score} points")
            else:
                print(f"Computer won with {computer_score} points.You had {player_score} points")
            break
        print(f"Your current points: {player_score}")
        print(f"Computer current points: {computer_score}")
        game_round += 1
