# ------------------------------------------------------------------ #
# ------------ Huffman Compressor Application ---------------------- #
# ------------ HEPIA 2018-2019 ITI 1 ------------------------------- #
# ------------------------------------------------------------------ #
# ---- File Module ----- Sergey PLATONOV & Dylan MPACKO ------------ #
# ------------------------------------------------------------------ #

# ------------------------------ Assets ---------------------------- #
import sys
import json
import time
import hashlib
import argparse
import os
from prettytable import PrettyTable

# ----------------------- Function Definitions --------------------- #
def read_user_input():
    filenames = []
    args = sys.argv
    if len(args) == 4:
        filenames.append(args[1])
        filenames.append(args[2])
        filenames.append(args[3])
        return filenames
    else:
        raise Exception('Please provide the name of the Input and Output files! (2 arguments)')

def bytes_2_array(filename): # -> bytearray()
    output_array = []
    with open(filename, "rb") as f:
        byte = f.read(1).hex()
        output_array.append(byte)
        while byte:
            byte = f.read(1)
            if not byte:
                break
            i = byte.hex()
            output_array.append(i)
    f.close()
    return output_array

def write_2_binary(byte_array, filename):
    x = bytes([int(x, 0) for x in byte_array])
    #x += b''
    f = open(filename, "wb")
    f.write(x)
    f.close()

def update_bar(pbar, processname):
    time.sleep(0.1)
    pbar.update(1)
    pbar.set_description(processname, refresh=True)

def strip_zeros(byte_array):
    binary_string = ""
    qty_zeros = int(byte_array[0], 16)
    byte_array.pop(0)

    for i in range(len(byte_array)):
        val = format(int(byte_array[i], 16), '08b')
        binary_string += val
    return binary_string if qty_zeros == 0 else binary_string[: -qty_zeros]

def json_2_dict(filename):
    with open(filename, 'r') as outfile:
        dict = json.load(outfile)
        outfile.close()
    return dict

def retranslate(binary_string, dict):
    position = 0
    hex_array = []
    key = binary_string[0]
    while position < len(binary_string):
        if key in dict.keys():
            hex_array.append(hex(int(dict[key], 16)))
            position += 1
            if position < len(binary_string):
                key = binary_string[position]
        else:
            position += 1
            if position < len(binary_string):
                key += binary_string[position]
    return hex_array

def hashOriginal(filename):
    with open(filename, "rb") as f:
        byte = f.read()
        m = hashlib.sha256(byte).hexdigest()
    f.close()
    return m

def check_hashes(filename):
    this_hash = hashOriginal(filename)
    hash_input = input("\033[94m\033[1mHash of the original:\t\033[0m")

    return (this_hash == hash_input)

def decompressor_display(file_2_write):
    arrow = '\u2192'
    print('\n')
    _green_bold = "\033[92m\033[1m"
    _red_bold = "\033[91m\033[1m"
    _output = ""
    is_match = check_hashes(file_2_write)

    if is_match:
        _output = _green_bold + "File Intact!"
    else:
        _output = _red_bold + "File Corrupted!"

    print('\n', _output, '\n')


def hepia_print():
    line = [""] * 14
    line[0] = "MMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMM"
    line[1] = "MMMMMMMMMMMMMMMMMMMMMO:;OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx,;OMMMMMMMMMMMMMMMMMMMMMMMMMM"
    line[2] = "MMMMMMMMMMMMMMMMMMMMMd  oX00XWMMMMMMMMMMMMMWK0O0NMMMMMMMMMMMMMNKXNKO0NMMMMMMMMMMMMWkcl0MMMMMMMMMMMWN0OOKNMMMMMMMM"
    line[3] = "MMMMMMMMMMMMMMMMMMMMMd  ';...xWMMMMMMMMMMM0:.',.'xNMMMMMMMMMMWd..,;..,OWMMMMMMMMMMWo.'kMMMMMMMMMMNd'.,'.,kWMMMMMM"
    line[4] = "MMMMMMMMMMMMMMMMMMMMMd  cKd. ;XMMMMMMMMMMX; .xO; .OMMMMMMMMMMWl  cKx. :XMMMMMMMMMMWl .xMMMMMMMMMMXd:d0o. :NMMMMMM"
    line[5] = "MMMMMMMMMMMMMMMMMMMMMd  oMO. ;XMMMMMMMMMM0' .;c;':0MMMMMMMMMMWl  dM0' ,KMMMMMMMMMMWl .xMMMMMMMMMMNkc;:,  :NMMMMMM"
    line[6] = "MMMMMMMMMMMMMMMMMMMMMd  oMO. ;XMMMMMMMMMMK, 'OXxcoXMMMMMMMMMMWl  oWO. ;XMMMMMMMMMMWl .xMMMMMMMMMMk. :Kk. :NMMMMMM"
    line[7] = "MMMMMMMMMMMMMMMMMMMMMd. dMO. :XMMMMMMMMMMWx. ,;..lNMMMMMMMMMMWl  .;. .xWMMMMMMMMMMWl .xMMMMMMMMMMO' .c;. :XMMMMMM"
    line[8] = "MMMMMMMMMMMMMMMMMMMMMXkkXMNOx0WMMMMMMMMMMMWKkddx0WMMMMMMMMMMMWl .lkdxKWMMMMMMMMMMMWKxkXMMMMMMMMMMWKxdx0OxONMMMMMM"
    line[9] = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd.'kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
    line[10] ="MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN..WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
    line[11] ="MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNXXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
    line[12] ="\033[91mMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\033[0mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
    line[13] ="\033[91mMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\033[0mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n"

    for i in range(len(line)):
        for j in range(len(line[i])):
            if j < (len(line[i])-1):
                print(line[i][0:j], end = "\r")
            else:
                print(line[i][0:j], end = "\n")
        time.sleep(0.01)


