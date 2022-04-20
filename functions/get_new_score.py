from functions.draw_number import draw_number


def get_new_score(current_score, game, end_draw):
    """
    :param current_score: int current score
    :param game: int game round
    :param end_draw: int end draw
    :return: int new game score
    """
    start_draw = 1
    new_draw = 0
    new_draw += draw_number(start_draw, end_draw)

    if game > 1:
        if new_draw == 7:
            new_score = current_score // 7
        elif new_draw == 11:
            new_score = current_score * 11
        else:
            new_score = current_score + new_draw
    else:
        new_score = current_score + new_draw
    return new_score
