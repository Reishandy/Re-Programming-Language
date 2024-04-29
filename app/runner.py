from app.program import Program

instruction_list = [
    "NOP",  # No operation, do nothing
    "MEM",  # Add memory space (ex MEM 10) (10 after pointer)
    "DEL",  # Delete memory space in pointer (ex DEL) (delete the current pointer)
    "MOV",  # Move the pointer a set amount (ex MOV 2; MOV -4)
    "JMP",  # Jump to a specific memory address (ex JMP *8; JMP *0)
    "SET",  # Set a value into and address (ex SET 5)
    "CPY",  # Copy a value from one address to another (ex CPY *2) (copy from address 2 to current pointer)
    "ADD",  # Arithmetic addition, add to current pointer value (ex ADD *2; ADD 4)
    "SUB",  # Arithmetic subtraction, subtract from current pointer value (ex SUB *2; SUB 4)
    "MUL",  # Arithmetic multiplication, multiply current pointer value (ex MUL *2; MUL 4)
    "DIV",  # Arithmetic division, divide current pointer value (ex DIV *2; DIV 4)
    "PRN",  # Print the current pointer value
    "DBG"  # Print the entre memory for debugging
]

global program


def run_file(file_path: str) -> None:
    with open(file_path, "r") as file:
        instructions = [line.strip() for line in file if line.strip() != ""]

    run(instructions)


def run(instructions: list) -> None:
    global program
    program = Program()

    for line in instructions:
        if " " not in line:
            line += " "

        try:
            instruction, argument = line.split(" ")
        except ValueError:
            instruction, *argument = line.split(" ")

        match instruction:
            case "NOP":
                continue
            case "DBG":
                print(program)
            case "PRN":
                print(program.get())
            case "MEM":
                mem_handler(argument)
            case "DEL":
                program.remove()
            case "MOV":
                mov_handler(argument)
            case "JMP":
                jmp_handler(argument)
            case "SET":
                set_handler(argument)
            case "CPY":
                cpy_handler(argument)
            # TODO: implement ADD, SUB, MUL, DIV
            case _:
                raise SyntaxError(f"Invalid instruction: {instruction}")


def cpy_handler(argument: str) -> None:
    global program

    if argument == "":
        raise SyntaxError("CPY requires an argument")
    elif argument[0] != "*" or not argument[1:].isdigit():
        raise SyntaxError(f"Invalid CPY usage: CPY {argument}")

    program.copy(int(argument[1:]))


def set_handler(argument: str) -> None:
    global program

    if argument == "":
        raise SyntaxError("SET requires an argument")

    negative = False
    if argument[0] == "-":
        negative = True

    if isinstance(argument, list):
        argument = " ".join(argument)
    elif argument.isdigit():
        argument = int(argument) * -1 if negative else int(argument)
    elif argument.isdecimal():
        argument = float(argument) * -1 if negative else float(argument)

    program.set(argument)


def jmp_handler(argument: str) -> None:
    global program

    if argument == "":
        raise SyntaxError("JMP requires an argument")
    elif argument[0] != "*":
        raise SyntaxError(f"Invalid JMP usage: JMP {argument}")
    elif not argument[1:].isdigit():
        raise SyntaxError(f"Invalid JMP usage: JMP {argument}")

    program.jump(int(argument[1:]))


def mov_handler(argument: str) -> None:
    global program

    if argument == "":
        raise SyntaxError("MOV requires an argument")
    elif argument[0] == "-":
        if not argument[1:].isdigit():
            raise SyntaxError(f"Invalid MOV usage: MOV {argument}")
    elif not argument.isdigit():
        raise SyntaxError(f"Invalid MOV usage: MOV {argument}")

    program.move(int(argument))


def mem_handler(argument: str) -> None:
    global program

    if argument == "":
        program.add()
    elif not argument.isdigit():
        raise SyntaxError(f"Invalid MEM usage: MEM {argument}")
    else:
        program.bulk_add(int(argument))


if __name__ == "__main__":
    run_file("../example")
