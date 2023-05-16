import string, numpy, time, random
from PyQt6.QtCore import Qt

def get_password(lowercase: bool, uppercase: bool, numbers: bool, symbols: bool, accepted_symbols: str, length: int) -> str:
    lowercase_str = string.ascii_lowercase
    uppercase_str = string.ascii_uppercase
    numbers_str = string.digits
    symbols_str = accepted_symbols

    unix_timestamp = int(time.time())
    random_number = 0
    for i in range(300):
        random_number += int(random.randint(0, 100))
    
    if random_number > 2**32:
        random_number = 2**32
    
    random_seed = int(unix_timestamp / random_number)

    accepted_chars = ""
    if lowercase:
        accepted_chars += "".join(lowercase_str)

    if uppercase:
        accepted_chars += "".join(uppercase_str)
    
    if numbers:
        accepted_chars += "".join(numbers_str)

    if symbols:
        if symbols_str == "":
            symbols_str = "@%+\/'!#$^?:,(){}[]~`-_."
        accepted_chars += "".join(symbols_str)

    if accepted_chars == "":
        generated_password = "No available characters!"
    
    if accepted_chars != "":
        numpy.random.seed(random_seed)
        generated_password = list(numpy.random.choice(list(accepted_chars), length))
        generated_password = "".join(generated_password)
    
    return generated_password