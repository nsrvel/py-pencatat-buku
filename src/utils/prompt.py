import questionary
import src.constants.decorator as decorator
import src.display.toast as toast
import questionary
import json

def _questionary_input(message: str):
    try:
        try:
            prompt = questionary.text(message)
            answer = prompt.unsafe_ask()
            return answer if answer else ""
        except questionary.keyboard_interrupt_exception as e:
            return e
    except:
        return None
    
def question_input(message: str, tags: list[str] | None):
    answer = _questionary_input(message)
    
    if answer == None:
        return answer
    else:        
        if tags is not None:
            for tag in tags:
                if tag == "required" and not answer:
                    toast.display_toast(f"{decorator.toast_err}Wajib diisi")
                    return question_input(message, tags)
                if "type:" in tag:
                    is_error = False
                    expected_type_raw = tag.replace(" ", "").replace("type:", "")
                    expected_type = expected_type_raw.split(",")
                    for expected in expected_type:
                        if expected_type == "str":
                            answer = str(answer)
                        elif expected == "int":
                            try:
                                answer = int(answer)
                            except:
                                is_error = True
                        elif expected == "float":
                            try:
                                answer = float(answer)
                            except:
                                is_error = True
                        elif expected == "bool":
                            try:
                                answer = bool(answer.lower())
                            except:
                                is_error = True
                                
                    if is_error:
                        toast.display_toast(f"{decorator.toast_err}Input harus berupa {expected_type_raw.replace(',', ' / ')}")
                        return question_input(message, tags)
                    else:
                        return answer

def question_select(options):
    try:
        selected_option = questionary.select(
            "Menu \n", choices=options, instruction=" ", ).ask()
        return selected_option
    except (KeyboardInterrupt):
        return None
    