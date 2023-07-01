from rich.console import Console
import src.utils.terminal_into as term
import src.utils.toast as toast


console = Console()


def display_toast(message: str):
    
    toast_type, message = toast.toast_selector(message)
    terminal_width = term.get_terminal_size()
    max_message_length = terminal_width-(terminal_width*10/100)
    message_lenght = len(message)
    
    if message_lenght > max_message_length:
        parts = []
        message_temp = message
        while len(message_temp) > max_message_length:
            message_temp, part = toast.remove_and_get_substring(message_temp)
            parts.append(part)
        is_first = True
        for p in parts:
            if is_first:
                console.print(f"{toast_type}{p}")
            else:
                console.print(f"{toast.empty_toast_line}{p}")
            input()
    else:
        console.print(f"{toast_type}{message}")
        try: 
            input()
        except KeyboardInterrupt as e:
            print()
        

