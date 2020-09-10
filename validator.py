# PASSWORD VALIDATOR TEMPLATE: REPLACE THIS LINE WITH YOUR FILE HEADER

def validate(password):
    """ Analyzes an input password to determine if it is "Secure", "Insecure", or "Invalid" based on the assignment description criteria.

    Arguments:
        password (string): a string of characters

    Returns:
        result (string): either "Secure", "Insecure", or "Invalid". 
    """
    upper_count = 0
    lower_count = 0
    digits_count = 0
    special_char = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")
    special_char_count = 0



    psswd_list = list(password)
    if len(psswd_list) < 8:
            return "Invalid"
    elif " " in psswd_list or "@" in psswd_list or "#" in psswd_list:
            return "Invalid"

    for i in psswd_list:
        if i.isupper():
            upper_count += 1
        if i.islower():
            lower_count += 1
        if i.isdigit():
            digits_count += 1
        for char in special_char:
            if i == char:
                special_char_count += 1

    if upper_count > 0 and lower_count > 0 and digits_count > 0  and special_char_count > 0:
            return "Secure"
    return "Insecure"

def generate(n):
    """ Generates a password of length n which is guaranteed to be Secure according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.

    Returns:
        secure_password (string): a Secure password of length n. 
    """
    pass

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.
    print(validate("fdslfktertres"))
    print(validate("jfkd s"))
    print(validate("HACKING"))
    print(validate("Passw0rd!"))
    print(validate("helloworld!"))
