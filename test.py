
# test.py

from cli_utils import (
    print_separator,
    print_char_separator,
    print_custom_separator,
    print_labeled_separator,
    print_box,
    print_elephant
)

print_separator()
print_char_separator("-")
print_char_separator("=")
print_custom_separator("~", 50)
print_custom_separator("#", 20)
print_custom_separator("*", -5)
print_labeled_separator("START")
print_labeled_separator("DONE", char="-", width=40)
print_box("Hello, World!")
print("\n--- Full Elephant ---")
print_elephant ()