# ======================================================
# Name: Yu, Zong Lin
# ID: 1614934
# Course: CMPUT 274
# Term: Fa20
# Assignment: Weekly Assignment 1 -- Password Validator
# =======================================================

from random import randint, random

def validate(password):
    """ Analyzes an input password to determine if it is "Secure", "Insecure", or "Invalid" based on the assignment description criteria.

    Arguments:
        password (string): a string of characters

    Returns:
        (string): either "Secure", "Insecure", or "Invalid". 
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
       	password (string): a Secure password of length n. 
    """
    spec_char_list = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")
    upper_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower_list = list("abcdefghijklmnopqrstuvwxyz")

  
    if n >= 8:
        upper_count = 0
        lower_count = 0
        digits_count = 0
        spec_char_count = 0
        password = ""
        for i in range(n):
            index = chance(upper_count, lower_count, digits_count, spec_char_count, n)
            if index == 0:
                char = upper_list[randint(0, len(upper_list)-1)]
                upper_count += 1
            elif index == 1:
                char = lower_list[randint(0, len(lower_list)-1)]
                lower_count += 1
            elif index == 2:
                char = str(randint(0, 9))
                digits_count += 1
            else:
                char = spec_char_list[randint(0, len(spec_char_list)-1)]
                spec_char_count += 1

            password += char
	
        return password
    	




def chance(count_0, count_1, count_2, count_3, n):
    """ Helps deciding on the next character, ensuring that at least one character from each type is chosen
    This is better than relying solely on randint(), as that does not guarantee that all the possible types are picked.
    chance() takes in the count of each type of allowed characters, and reduces the relative chance that the character is reselected, 
    ensuring that the other characters are selected.

    Arguments:
        count_0 (int): the number of times item 0 has been chosen
	count_1 (int): the number of times item 1 has been chosen
	count_2 (int): the number of times item 2 has been chosen
	count_3 (int): the number of times item 3 has been chosen
	n (int): the number of characters in the string

    Returns:
        max_element (int): an integer 0 - 3 inclusive used to select the type of character to input next.

    """
    chance_0 = ((n-count_0)/n)**20
    chance_1 = ((n-count_1)/n)**20
    chance_2 = ((n-count_2)/n)**20
    chance_3 = ((n-count_3)/n)**20

    chances = [chance_0, chance_1, chance_2, chance_3]
    for i in range(len(chances)):
        chances[i] = chances[i] * random()

    max_element = chances.index(max(chances))

    return max_element

    









if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.
    pass
