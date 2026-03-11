# cli_utils/separators.py

def print_separator():
    print("*" * 30)


def print_char_separator(char):
    print(char * 30)

def print_custom_separator(char, length):
    if length <= 0:
        print("")
        return
    print(char * length)

def print_labeled_separator(label, char="*", width=30):
    print(label.center(width, char))

def print_box(message, char="*"):
    width = len(message) + 4
    border = char * width
    print(border)
    print(f"{char} {message} {char}")
    print(border)


# --- New Elephant Function ---
def print_elephant():
    """
    Prints a full-body colored ASCII elephant.
    Colors:
    - Brown for head
    - Yellow for trunk
    - Green for body
    - Red for legs
    """
    c = {
        "brown": "\033[33m",
        "yellow": "\033[93m",
        "green": "\033[92m",
        "red": "\033[91m",
        "reset": "\033[0m"
    }

    lines = [
        r"       /  \  ____  /  \ ",       # head
        r"      /____\/    \/____\ ",     # head
        r"     (  o o )  (  o o  )",     # eyes
        r"       \_V_/    \_V_/ ",       # head bottom
        r"         ||        || ",       # trunk start
        r"         ||        || ",       # trunk
        r"         ||        || ",       # trunk
        r"        /||\      /||\ ",       # body
        r"       / || \    / || \ ",      # body
        r"      /  ||  \  /  ||  \ ",     # body
        r"     /   ||   \/   ||   \ ",    # body
        r"    /    ||         ||    \ ",  # body
        r"   /     ||         ||     \ ", # body
        r"  |      ||         ||      |", # body
        r"  |      ||         ||      |", # body
        r"  |      ||         ||      |", # body
        r"  |      ||         ||      |", # body
        r"  |      ||         ||      |", # legs start
        r"  |______||_________||______|", # legs
    ]

    for i in range(len(lines)):
        if i <= 3:  # head
            color = c["brown"]
        elif i <= 6:  # trunk
            color = c["yellow"]
        elif i <= 16:  # body
            color = c["green"]
        else:  # legs
            color = c["red"]
        print(f"{color}{lines[i]}{c['reset']}")