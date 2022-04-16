from random import randrange


def draw_number(start, end, number_throws):
    """
    :param start: int begging of range to draw
    :param end:  int end of range to draw
    :param number_throws:  int number of throws
    :return: int drawn number between start and end
    """
    score = 0
    for i in range(number_throws + 1):
        score += randrange(start, end+1)
    return score
