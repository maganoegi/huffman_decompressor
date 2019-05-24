# ------------------------------------------------------------------ #
# ------------ Huffman Decompressor Application -------------------- #
# ------------ HEPIA 2018-2019 ITI 1 ------------------------------- #
# ------------------------------------------------------------------ #
# ------- Main --------- Sergey PLATONOV & Dylan MPACKO ------------ #
# ------------------------------------------------------------------ #

# ------------------------------ Assets ---------------------------- #
from decomp_lib import *
from tqdm import tqdm
import time
import os

# --------------------------- Main --------------------------------- #
os.system('cls' if os.name == 'nt' else 'clear')
hepia_print()
print("\n")
bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
with tqdm(total=6, ncols=80, bar_format=bar_format) as pbar:

    # --- Initialization ---------------- #
    filenames = read_user_input()
    update_bar(pbar, 'Open File  ')

    file_2_read = filenames[0]
    json_name = filenames[1]
    file_2_write = filenames[2] 

    # --- File Binary to Binary Array --- #
    byte_array = bytes_2_array(file_2_read) # -> string[] 8 bit Hex (no prefix)
    update_bar(pbar, 'File->Array')

    dict = json_2_dict(json_name) # -> Dictionary { key: binString -> value: hexString }
    update_bar(pbar, 'Json Read  ')

    byte_string_no_zeros = strip_zeros(byte_array) # -> binString
    update_bar(pbar, 'Strip Zeros')

    retranslated_byte_array = retranslate(byte_string_no_zeros, dict) # -> string[] 8 bit Hex (0x prefix)
    update_bar(pbar, 'Retranslate')

    write_2_binary(retranslated_byte_array, file_2_write)
    update_bar(pbar, 'Done       ')

    time.sleep(0.1)
    pbar.close()

    decompressor_display(file_2_write)






