import shutil
from termcolor import colored
import llama_opts
import os

#####    Home Screen     #####


def home():
    title_message = colored("Welcome to LlamaCMD", "white")
    version_message = colored("Version 0.8", "light_grey")
    console_width, _ = shutil.get_terminal_size()
    title_centered = title_message.center(console_width)
    version_centered = version_message.center(console_width)

    llama1 = colored("Menu:", "white", attrs=["bold", "underline"])
    llama2 = colored("1. Re-encode (with optional cut)", "yellow")
    llama3 = colored("2. Mux (with optional cut)", "yellow")
    llama4 = colored("3. Download (not implemented)", "dark_grey")
    llama5 = colored("4. Exit", "light_red")

    llama_home = f"""\
                         g
                       e8lprt
                       led4lmf9
                      jbagph91
                      ia0flo                               {llama1}
                      jb0fqt                               {llama2}
        orppqooo      iabfqt                               {llama3}
     lllmlklllklmmnnnlhadiqt                               {llama4}
    bfgfgaebeghjklllkkhdems                                {llama5}
    abbcgc3cadeegihgjkljjpr
    7a8aegX7770bge2aiihlqq
     hb6TY7bfcabc67338emo
      dab6bg  hhjhd90nr
     gbgdaj       c7eo
     ecgeh        dach
     dbgfe        fbgi
     g9jgj        cdlk
      9gfid        cnk
"""

    print(title_centered)
    print(version_centered)
    print("\n")
    print(llama_home)

    return ""


input_name = ""
trim_choice = ""
trim_start = ""
trim_len = ""
output_name = ""
confirmation = ""
timestamp = ""


def menu_options():
    menu_choice = int(input(colored("Enter option number: ", "light_magenta")))
    print()

    if menu_choice == 1:
        llama_opts.llama_encode(trim_choice, confirmation, timestamp)
    elif menu_choice == 2:
        llama_opts.llama_mux()
    elif menu_choice == 4:
        llama_opts.leave()

    menu_choice = 0


def home_screen():
    os.system('cls')
    print(home())
    print(menu_options())
