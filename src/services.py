def detect_hourly_rate_column(headers: list):
    """ Опреледение как именно называется поле с часовой ставкой """
    # Возможные варианты названий столбца
    possible_names = ['salary', 'rate', 'hourly_rate']

    for name in possible_names:
        if name in headers:
            return name

    raise Exception('Нет поля с часовой ставкой')


def calculate_max_length_of_fields(data: list) -> int:
    """ Вычисление максимальной длины среди полей """
    max_length = 0
    for row in data:
        for value in row.values():
            max_length = max(max_length, len(value))

    return max_length
