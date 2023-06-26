
# * String Validator
def validate_string_not_empty(str):
	if isinstance(str) and str.strip():
		return True
	else:
		return False
