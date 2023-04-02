import os


def clear_console():

    """
    Tool to clear the terminal of all text
    """
    os.system("cls" if os.name == "nt" else "clear")