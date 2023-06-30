import questionary as question
import src.constants.command as command

# Menampilkan opsi utama
def display_main_select(is_show_list: bool, books_length: int):
    options = []
    if is_show_list:
        options.append(command.M2)
        options.append(command.M6)
    else:
        options.append(command.M1)
    options.append(command.M5)
    
    if books_length > 0:
        options.extend([
            command.M7,
            command.M8,
        ])
    options.append(command.S0)

    answer = _question_select(options)
    if answer == None:
        return command.S0
    return answer

# Menampilkan opsi filter
def display_filter_select(page_info):
    options = []

    if page_info.page - 1 != 0:
        options.append(command.C1)
    if page_info.has_more:
        options.append(command.C2)
    options.append(command.C5)
    options.append(command.C3)
    options.append(command.C4)
    options.append(command.S1)

    answer = _question_select(options)
    if answer == None:
        return command.S0
    return answer


def _question_select(options):
    try:
        selected_option = question.select(
            "Menu \n", choices=options, instruction=" ", ).ask()
        if selected_option == None:
            return command.S1
        else:
            return selected_option
    except:
        return command.S1