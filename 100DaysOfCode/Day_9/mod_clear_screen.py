import os
def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/OS X
        os.system('clear')