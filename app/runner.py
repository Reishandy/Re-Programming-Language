instruction = [
    "NOP",  # No operation, do nothing
    "MEM",  # Add memory space (ex MEM +10; MEM -2) (10 after pointer; 2 before pointer)
    "DEL",  # Delete memory space in pointer (ex DEL) (delete the current pointer)
    "MOV",  # Move the pointer a set amount (ex MOV 2; MOV -4)
    "JMP",  # Jump to a specific memory address (ex JMP *8; JMP *0)
    "SET",  # Set a value into and address (ex SET 5; SET *2 4)
    "CPY",  # Copy a value from one address to another (ex CPY *i *2) (copy from pointer to address 2)
    "ADD",  # Arithmetic addition, add to current pointer value (ex ADD *2; ADD 4)
    "SUB",  # Arithmetic subtraction, subtract from current pointer value (ex SUB *2; SUB 4)
    "MUL",  # Arithmetic multiplication, multiply current pointer value (ex MUL *2; MUL 4)
    "DIV",  # Arithmetic division, divide current pointer value (ex DIV *2; DIV 4)
    "PRN",  # Print the current pointer value
    "DBG"  # Print the entre memory for debugging
]


if __name__ == "__main__":
    # TODO: make a parser class to parse the code from a file into list and catch syntax errors
    code = [
        "MEM 10",
        "SET 5",
        "ADD 5",
        "SUB 3",
        "PRN",
        "MOV 2",
        "SET 10",
        "ADD 2",
        "PRN",
        "MOV -2",
        "SET 'Hello, World!'",
        "PRN",
        "DEL",
        "DBG"
    ]
