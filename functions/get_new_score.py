from functions.draw_number import draw_number


def get_new_score(current_score, game):
    """
    :param current_score: int current score
    :param game: int game round
    :return: int new game score
    """
    start_draw = 1
    end_draw = 6
    throws = 2
    new_draw = draw_number(start_draw, end_draw, throws)
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
