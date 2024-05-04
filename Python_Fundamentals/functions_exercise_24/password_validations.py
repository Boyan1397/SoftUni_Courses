def is_pass_valid(pass_input):
    digits_counter = 0

    if not 6 <= len(pass_input) and len(pass_input) <= 10:
        print("Password must be between 6 and 10 characters")

    if not pass_input.isalnum():
        print("Password must consist only of letters and digits")

    for num in pass_input:
        if num.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
    if 6 <= len(pass_input) and len(pass_input) <= 10 and pass_input.isalnum() and digits_counter >= 2:
        print("Password is valid")



password = input()
is_pass_valid(password)
