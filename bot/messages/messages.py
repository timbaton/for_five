import enum

help_message = 'Для того, чтобы изменить текущее состояние пользователя, ' \
               f'отправь команду "/setstate x", где x - число от 0 до 3.\n' \
               'Чтобы сбросить текущее состояние, отправь "/setstate" без аргументов.'

start_message = 'Добрый день, дорогой студент! 🤓\n\n' \
                'Мы группа поддержки написания всех видов работ, ' \
                'начиная от эссе и контрольных, заканчивая дипломами и диссертациями. За плечами имеем 5-ти летний стаж ' \
                'выполнения работ любой сложности и на любую тематику. \n\n' \
                'На данный момент в нашей команде уже более ' \
                '30 человек, готовые приступить к твоей работе уже сегодня! \n\n' \
                'Наши преимущества:\n' \
                '- высокая оригинальность;\n' \
                '- оперативность;\n' \
                '- круглосуточная поддержка;\n' \
                '- доступные цены;\n' \
                '- отличные авторы.\n\n'

choose_job_message = 'Выбирай вид работы и переходи на следующую страницу 👌'

invalid_key_message = 'Ключ "{key}" не подходит.\n' + help_message
state_change_success_message = 'Текущее состояние успешно изменено'
state_reset_message = 'Состояние успешно сброшено'
current_state_message = 'Текущее состояние - "{current_state}", что удовлетворяет условию "один из {states}"'

MESSAGES_DICT = {
    'start': start_message,
    'help': help_message,
    'invalid_key': invalid_key_message,
    'state_change': state_change_success_message,
    'state_reset': state_reset_message,
    'current_state': current_state_message,
}


class MESSAGES(enum.Enum):
    start = start_message
    help = help_message
    choose_job = choose_job_message
    invalid_key = invalid_key_message
    state_change = state_change_success_message
    state_reset = state_reset_message
    current_state = current_state_message
