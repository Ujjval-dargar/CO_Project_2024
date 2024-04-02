
Opcode_type = {
    '0110011': 'R',
    '0000011': 'I',
    '0010011': 'I',
    '1100111': 'I',
    '0010111': 'U',
    '0110111': 'U',
    '1101111': 'J',
    '0100011': 'S',
    '1100011': 'B'
}

Address_Register = {

    '00000': 'zero',
    '00001':  'ra',
    '00010':  'sp',
    '00011':  'gp',
    '00100':  'tp',
    '00101':  't0',
    '00110':  't1',
    '00111':  't2',
    '01000':  's0',
    '01000':  'fp',
    '01001':  's1',
    '01010':  'a0',
    '01011':  'a1',
    '01100':  'a2',
    '01101':  'a3',
    '01110':  'a4',
    '01111':  'a5',
    '10000':  'a6',
    '10001':  'a7',
    '10010':  's2',
    '10011':  's3',
    '10100':  's4',
    '10101':  's5',
    '10110':  's6',
    '10111':  's7',
    '11000':  's8',
    '11001':  's9',
    '11010': 's10',
    '11011': 's11',
    '11100':  't3',
    '11101':  't4',
    '11110':  't5',
    '11111':  't6'
}

register_value = {
    'zero': "00000000000000000000000000000000",
    'ra': "00000000000000000000000000000000",
    'sp': "00000000000000000000000000000000",
    'gp': "00000000000000000000000000000000",
    'tp': "00000000000000000000000000000000",
    't0': "00000000000000000000000000000000",
    't1': "00000000000000000000000000000000",
    't2': "00000000000000000000000000000000",
    's0': "00000000000000000000000000000000",
    'fp': "00000000000000000000000000000000",
    's1': "00000000000000000000000000000000",
    'a0': "00000000000000000000000000000000",
    'a1': "00000000000000000000000000000000",
    'a2': "00000000000000000000000000000000",
    'a3': "00000000000000000000000000000000",
    'a4': "00000000000000000000000000000000",
    'a5': "00000000000000000000000000000000",
    'a6': "00000000000000000000000000000000",
    'a7': "00000000000000000000000000000000",
    's2': "00000000000000000000000000000000",
    's3': "00000000000000000000000000000000",
    's4': "00000000000000000000000000000000",
    's5': "00000000000000000000000000000000",
    's6': "00000000000000000000000000000000",
    's7': "00000000000000000000000000000000",
    's8': "00000000000000000000000000000000",
    's9': "00000000000000000000000000000000",
    's10': "00000000000000000000000000000000",
    's11': "00000000000000000000000000000000",
    't3': "00000000000000000000000000000000",
    't4': "00000000000000000000000000000000",
    't5': "00000000000000000000000000000000",
    't6': "00000000000000000000000000000000"
}

program_counter = [0]
firstRun = [True]
regs = {}
data_memory = dict.fromkeys(range(0, 63, 4), "0" * 32)
