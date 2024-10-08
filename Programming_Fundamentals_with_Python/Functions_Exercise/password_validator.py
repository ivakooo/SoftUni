def password_validator(some_password: str) -> list:
    list_with_errors_messages = []
    if len(some_password) < 6 or len(some_password) > 10:
        list_with_errors_messages.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        list_with_errors_messages.append("Password must consist only of letters and digits")
    digit_found = 0
    for current_char in some_password:
        if current_char.isdigit():
            digit_found += 1
    if digit_found < 2:
        list_with_errors_messages.append("Password must have at least 2 digits")
    return list_with_errors_messages


password = input()
error_messages = password_validator(password)
if not error_messages:
    print("Password is valid")
else:
    print("\n".join(error_messages))

