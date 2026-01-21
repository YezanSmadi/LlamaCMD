try:
    from termcolor import colored
except ImportError:
    def colored(text, color=None, attrs=None):
        return text
from pathlib import Path
import shlex
import llama_menu
import sys
import os

input_name = ""
trim_choice = ""
trim_start = ""
trim_len = ""
output_name = ""
confirmation = ""

global encode_passthru
global encode_trim_passthru
global mux_passthru
global mux_trim_passthru


def get_ffmpeg_path():
    if getattr(sys, 'frozen', False):
        # Running in a PyInstaller bundle
        bundle_dir = sys._MEIPASS
    else:
        # Running in normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(bundle_dir, 'ffmpeg.exe')


mux = shlex.split(
    'ffmpeg -ss {trim_start} -i "{input_name}" -t {trim_len} -map 0 -c copy -avoid_negative_ts make_zero "{output_name}"')


#####   Message For Exiting LlamaCMD    #####
def leave_llama():
    print(colored("Pleasure working with you!", "cyan"))
    print(colored("See ya later!", "cyan"))
    print()
    exit()


#####   Validate File Input     #####
def input_valid():
    while True:
        global input_name
        input_name = input(
            colored("What's our input file's name?: ", "light_magenta")).strip()
        input_path = Path(f'{Path.cwd()}/{input_name}')
        print()
        print(input_path)
        if input_path.is_file():
            print(colored("File has been found in directory.", "green"))
            print()
            break
        else:
            print(colored(
                "This file doesn't exist in this directory. Check if the file was spelled correctly and try again.", "light_red"))
            print()
    return (input_name)


#####   FFMPEG Commands  #####
def encode_passthru(output_name):
    encode_input = f'"{get_ffmpeg_path()}" -vsync -1 -i "{input_name}" -crf 16 -c:v libx264 -profile:v high10 -level:v 4.0 -c:a copy -movflags +faststart "{output_name}"'
    return encode_input


def encode_trim_passthru(output_name, trim_start, trim_len):
    encode_trim_input = f'"{get_ffmpeg_path()}" -vsync -1 -ss {trim_start} -i "{input_name}" -to {trim_len} -crf 16 -c:v libx264 -profile:v high10 -level:v 4.0 -c:a copy -movflags +faststart "{output_name}"'
    return encode_trim_input


def mux_passthru(output_name):
    mux_input = f'"{get_ffmpeg_path()}" -i "{input_name}" -map 0 -c copy -avoid_negative_ts make_zero "{output_name}"'
    return mux_input


def mux_trim_passthru(output_name, trim_start, trim_len):
    mux_trim_input = f'"{get_ffmpeg_path()}" -ss {trim_start} -i "{input_name}" -t {trim_len} -map 0 -c copy -avoid_negative_ts make_zero "{output_name}"'
    return mux_trim_input


#####   Message For When FFMPEG is Done With File   #####
def file_done():
    print()
    print(colored("All done!", "light_green"))
    print()
    while True:
        confirmation = input(
            colored("Would you like to go back to the ", "light_magenta") + colored("Main Menu ", "light_yellow") + colored("or ", "light_magenta") + colored("Exit", "light_red") + colored("? ", "light_magenta"))
        if confirmation.lower() == "main menu":
            llama_menu.home_screen()
            break
        elif confirmation.lower() == "exit":
            print()
            leave_llama()
        elif confirmation.lower() != "main menu" or "exit":
            print()
            print(
                colored('Input invalid: Type either "Main Menu" or "Exit"', "light_red"))
            print()
