import src.constants.decorator as decorator

success_toast_line = f"\n [green][ v ][/green] "
info_toast_line = f"\n [blue][ i ][/blue] "
warning_toast_line = f"\n [yellow][ ! ][/yellow] "
error_toast_line = f"\n [red][ x ][/red] "
empty_toast_line = f"       "

def is_toast(output):
    if isinstance(output, str):
        if decorator.toast_success in output:
            return True
        elif decorator.toast_warn in output:
            return True
        elif decorator.toast_err in output:
            return True
        elif decorator.toast_info in output:
            return True
        else:
            return False
    else:
        return False

def toast_selector(message: str):
    if decorator.toast_success in message:        
        return success_toast_line, message.replace(decorator.toast_success, "")
    elif decorator.toast_warn in message:
        return warning_toast_line, message.replace(decorator.toast_warn, "")
    elif decorator.toast_err in message:
        return error_toast_line, message.replace(decorator.toast_err, "")
    elif decorator.toast_info in message:
        return info_toast_line, message.replace(decorator.toast_info, "")
    else:
        return info_toast_line, message

def remove_and_get_substring(string, start_index, end_index):
    substring = string[start_index:end_index]
    string = string[:start_index] + string[end_index:]
    return string, substring
