import sys
from simulator_constants import *
from simulator_functions import *

input = sys.argv[-2]
output = sys.argv[-1]

setupDataMem()

with open(input) as input_file:
    input_lines = input_file.readlines()


# instrution_count = 1
while True:
    line_num = program_counter[0] // 4
    line = input_lines[line_num].strip()

    if line == "":
        continue

    # Virtual Halt
    if line == "00000000000000000000000001100011":
        appendReg(output)
        break

    opcode = line[-7:]
    instruction_type = Opcode_type[opcode]

    # print(instruction_type, instrution_count, line_num)

    if instruction_type == "R":
        R_type(line)
        program_counter[0] += 4

    elif instruction_type == "I":
        I_type(line)

        line = line[::-1]
        opcode = line[0:7][::-1]
        funct3 = line[12:15][::-1]

        if not (funct3 == "000" and opcode == "1100111"):
            program_counter[0] += 4

    elif instruction_type == "S":
        S_type(line)
        program_counter[0] += 4

    elif instruction_type == "B":

        prev_program_counter = program_counter[0]
        B_type(line)

        # No condition was true
        if prev_program_counter == program_counter[0]:
            program_counter[0] += 4

    elif instruction_type == "U":
        U_type(line)
        program_counter[0] += 4

    elif instruction_type == "J":
        J_type(line)

    elif instruction_type == "bonus":
        ans = bonus_type(line)
        if ans:
            break
        program_counter[0] += 4

    # Reset zero-reg
    register_value["zero"] = "0" * 32

    # Write registers to file
    # instrution_count += 1
    appendReg(output)

# Write data memory to file
appendDataMemory(output)
